from tkinter import *
from tkinter import ttk
from MyTasks.Task2.Controllers.My_Tasks_2Controller import PhoneController


class MyTasks_2_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Телефонная книга")
        self.geometry('1000x600')

        # Добавить запись в телефонную книгу
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_phone_title = ttk.Label(self.add_frame, text="Добавить запись")
        self.add_phone_title.pack()

        # Имя
        self.name_phone = ttk.Label(self.add_frame, text="Введите Имя")
        self.name_phone.pack()
        self.name_phone_input = ttk.Entry(self.add_frame)
        self.name_phone_input.pack()


        # Телефон
        self.phone_phone = ttk.Label(self.add_frame, text="Введите Телефон")
        self.phone_phone.pack()
        self.phone_phone_input = ttk.Entry(self.add_frame)
        self.phone_phone_input.pack()


        # Электронная почта
        self.email_phone = ttk.Label(self.add_frame, text="Введите должность сотрудника")
        self.email_phone.pack()
        self.email_phone_input = ttk.Entry(self.add_frame)
        self.email_phone_input.pack()

        # Кнопка
        self.add_phone_button = ttk.Button(self.add_frame, text="Добавить сотрудника")
        self.add_phone_button["command"] = self.add_phone
        self.add_phone_button.pack()

        # Изменить телефон
        self.phone_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.phone_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_phone = ttk.Label(self.phone_frame, text='Введите id записи и телефон')
        self.title_phone.pack()
        self.id_input = ttk.Entry(self.phone_frame)
        self.id_input.pack()
        self.phone_input = ttk.Entry(self.phone_frame)
        self.phone_input.pack()
        self.phone_button = ttk.Button(self.phone_frame, text='Изменить телефон')
        self.phone_button["command"] = self.update_phone
        self.phone_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()
    ######################################ТАБЛИЦА###########################################
        columns = ('id', 'name', 'phone', 'email')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу телефонных записей
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускать окно для изменения телефона при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.phone = self.tree.item(self.item, "values")[0]  # Из строки получаем id телефонной записи
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.phone)
        # window_update_rating = UpdateRatindView(self.phone)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список телефонных записей из БД
        phones = PhoneController.get()
        list_phones = []
        for phone in phones:
            list_phones.append(
                (phone.id,
                 phone.name,
                 phone.phone,
                 phone.email)
            )

        # Заголовки для таблицы
        self.tree.heading('name', text='Имя контакта')
        self.tree.heading('phone', text='Телефонный номер')
        self.tree.heading('email', text='Электронная почта')
        # Добавить данные в таблицу
        for phone in list_phones:
            self.tree.insert('', END, values=phone)

    def update_phone(self):
        self.id = self.id_input.get()  # id сотрудника
        self.phone = self.phone_input.get()  # новое описание
        if not self.id or not self.phone:  # проверка на пустые поля
            self.title_phone['text'] = 'Введите id записи и телефон'
        elif not self.id.isdigit():  # Проверка на целое число
            self.title_phone['text'] = 'id записи и телефон должны быть числами'
        try:
            self.phone
        except ValueError:
            self.title_phone['text'] = 'id записи и телефон должны быть числами'
            return
        else:
            PhoneController.phone_update(
                id=self.id,
                phone=self.phone
            )
        self.id_input.delete(0, 'end')
        self.phone_input.delete(0, 'end')
        self.table()  # Обновить таблицу телефонных записей

    def add_phone(self):
        self.name = self.name_phone_input.get()
        self.phone = self.phone_phone_input.get()
        self.email = self.email_phone_input.get()
        if self.name == '' or self.phone == '' or self.email == '':
            self.add_phone_title['text'] = 'Введите имя, телефон и электронную почту'
        else:
            PhoneController.add(
                name=self.name,
                phone=self.phone,
                email=self.email
            )
            self.name_phone_input.delete(0, 'end')
            self.phone_phone_input.delete(0, 'end')
            self.email_phone_input.delete(0, 'end')
        self.table()  # Обновить таблицу телефонных записей