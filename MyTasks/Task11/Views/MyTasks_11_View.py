from tkinter import *
from tkinter import ttk
from MyTasks.Task11.Controllers.My_Tasks_11Controller import EventsController


class MyTasks_11_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Планировщик событий")
        self.geometry('1000x600')

        # Добавить сотрудника
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_event_title = ttk.Label(self.add_frame, text="Добавить событие")
        self.add_event_title.pack()

        # Название события
        self.title_event = ttk.Label(self.add_frame, text="Введите Название события")
        self.title_event.pack()
        self.title_event_input = ttk.Entry(self.add_frame)
        self.title_event_input.pack()

        # Дата события
        self.date_event = ttk.Label(self.add_frame, text="Введите Дату события")
        self.date_event.pack()
        self.date_event_input = ttk.Entry(self.add_frame)
        self.date_event_input.pack()

        # Время события
        self.time_event = ttk.Label(self.add_frame, text="Введите Время события")
        self.time_event.pack()
        self.time_event_input = ttk.Entry(self.add_frame)
        self.time_event_input.pack()

        # Описание события
        self.description_event = ttk.Label(self.add_frame, text="Введите описание события")
        self.description_event.pack()
        self.description_event_input = ttk.Entry(self.add_frame)
        self.description_event_input.pack()

        # Кнопка
        self.add_event_button = ttk.Button(self.add_frame, text="Добавить сотрудника")
        self.add_event_button["command"] = self.add_event
        self.add_event_button.pack()

        # Изменить описание события
        self.description_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.description_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_description = ttk.Label(self.description_frame, text='Введите id события и его описания')
        self.title_description.pack()
        self.id_input = ttk.Entry(self.description_frame)
        self.id_input.pack()
        self.description_input = ttk.Entry(self.description_frame)
        self.description_input.pack()
        self.description_button = ttk.Button(self.description_frame, text='Изменить описание события')
        self.description_button["command"] = self.update_description
        self.description_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    ############################ТАБЛИЦА##############################
        columns = ('id', 'title', 'date', 'time', 'description')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу событий
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения описания при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.event = self.tree.item(self.item, "values")[0]  # Из строки получаем id события
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.event)
        # window_update_grade = UpdateRatindView(self.event)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список сотрудников из БД
        events = EventsController.get()
        list_events = []
        for event in events:
            list_events.append(
                (event.id,
                 event.name,
                 event.position,
                 event.salary,
                 event.department)
            )

        # Заголовки для таблицы
        self.tree.heading('title', text='Название события')
        self.tree.heading('date', text='Дата события')
        self.tree.heading('time', text='Время события')
        self.tree.heading('description', text='Описание')
        # Добавить данные в таблицу
        for event in list_events:
            self.tree.insert('', END, values=event)

    def update_description(self):
        self.id = self.id_input.get()  # id события
        self.description = self.description_input.get() # новое описание
        if not self.id or not self.description: # проверка на пустые поля
            self.title_description['text'] = 'Введите id события и его Описание'
            return
        else:
            EventsController.description_update(
                id=self.id,
                description=self.description
            )
        self.id_input.delete(0, 'end')
        self.description_input.delete(0, 'end')
        self.table() # Обновить таблицу событий

    def add_event(self):
        self.title = self.title_event_input.get()
        self.date = self.date_event_input.get()
        self.time = self.time_event_input.get()
        self.description = self.description_event_input.get()
        if self.title == '' or self.date == '' or self.time == '' or self.description =='':
            self.add_event_title['text'] = 'Введите имя, должность и отдел сотрудника'
        else:
        EventsController.add(
                title=self.title,
                date=self.date,
                time=self.time,
                description=self.description
            )
            self.title_event_input.delete(0, 'end')
            self.date_event_input.delete(0, 'end')
            self.time_event_input.delete(0, 'end')
            self.description_event_input.delete(0, 'end')
        self.table()  # Обновить таблицу сотрудников