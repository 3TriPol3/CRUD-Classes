# from tkinter import *
# from tkinter import ttk
# from MyTasks.Task1.Controllers.My_Tasks_1Controller import My_Tasks_1Controller
#
# class MyTasks_1_View(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Простой список дел")
#         self.geometry('1500x500')
#
#         # Раздел Добавить
#         self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
#         self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
#
#         self.add_title = ttk.Label(self.fram_add, text="Добавить задачу")
#         self.add_title.pack()
#
#         #task - название задачи
#         self.task = ttk.Label(self.fram_add, text="Введите название задачи")
#         self.task.pack()
#
#         # Окно ввода данных(task)
#         self.input_task = ttk.Entry(self.fram_add)
#         self.input_task.pack()
#
#         #completed - выполнена задача или нет
#         self.completed = ttk.Label(self.fram_add, text="Выполнена или не выполнена задача?")
#         self.completed.pack()
#
#         # Окно ввода данных(completed)
#         self.input_completed = ttk.Entry(self.fram_add)
#         self.input_completed.pack()
#
#         # Кнопка
#         self.add_button = ttk.Button(self.fram_add, text="", command=self.add_task)
#         self.add_button.pack()
#         #Вывод
#         #Таблица
#         self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
#         self.frame_table.pack(anchor='center', fill=X, padx=10, pady=10)
#
#
#         columns = ('task', 'completed')
#         self.tree = ttk.Treeview(self.frame_table, columns=columns, show='headings')
#         self.tree.pack(fill=BOTH, expand=1)
#         self.table()
#
#     def table(self):
#         # Очистить таблицу
#         for item in self.tree.get_children():
#             self.tree.delete(item)
#         # список задач
#         pets = My_Tasks_1Controller.get()
#         list_tasks = [] # сюда будут передаваться кортежи с описанием задач
#         for task in pets:
#             list_tasks.append(
#                 (
#                     task['task'],
#                     task['completed']
#                  )
#             )
#         # перевести на русский язык названия столбцов
#         self.tree.heading('task', text="Название задачи")
#         self.tree.heading('completed', text="Выполнена или нет")
#
#         for task in list_tasks:
#             self.tree.insert("",END,values=task)
#
#     def add_task(self):
#         My_Tasks_1Controller.add(
#             task=self.input_task.get(),
#             completed=self.input_completed.get()
#         )
#         self.table()

from tkinter import *
from tkinter import ttk
from MyTasks.Task1.Controllers.My_Tasks_1Controller import TaskController

class MyTasks_1_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Простой список дел")
        self.geometry('1000x600')

        # Добавить задачу
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_task_title = ttk.Label(self.add_frame, text="Добавить задачу")
        self.add_task_title.pack()

        # Название задачи
        self.name_task = ttk.Label(self.add_frame, text="Введите название задачи")
        self.name_task.pack()
        self.name_task_input = ttk.Entry(self.add_frame)
        self.name_task_input.pack()

        # Кнопка
        self.add_task_button = ttk.Button(self.add_frame, text="Добавить задачу")
        self.add_task_button["command"] = self.add_task
        self.add_task_button.pack()

        # Изменить статус
        self.completed_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.completed_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_completed = ttk.Label(self.completed_frame, text='Введите id задачи и её статус')
        self.title_completed.pack()
        self.id_input = ttk.Entry(self.completed_frame)
        self.id_input.pack()
        self.completed_input = ttk.Entry(self.completed_frame)
        self.completed_input.pack()
        self.completed_button = ttk.Button(self.completed_frame, text='Изменить статус')
        self.completed_button["command"] = self.update_completed
        self.completed_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    #############################ТАБЛИЦА##############################
        columns = ('id', 'task', 'completed')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу задач
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения зарплаты при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.task = self.tree.item(self.item, "values")[0]  # Из строки получаем id задачи
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.task)
        # window_update_grade = UpdateRatindView(self.task)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список задач из БД
        tasks = TaskController.get()
        list_tasks = []
        for task in tasks:
            list_tasks.append(
                (task.id,
                 task.task,
                 task.completed)
            )
        # Заголовки для таблицы
        self.tree.heading('task', text='Название задачи')
        self.tree.heading('completed', text='статус задачи')
        # Добавить данные в таблицу
        for task in list_tasks:
            self.tree.insert('', END, values=task)

    def update_completed(self):
        self.id = self.id_input.get()   # id задачи
        self.completed = self.completed_input.get() # новое описание
        if not self.id or not self.completed: # проверка на пустые поля
            self.title_completed['text'] = 'Введите id задачи и статус'
            return
        else:
            TaskController.completed_update(
                id=self.id,
                completed=self.completed
            )
        self.id_input.delete(0, 'end')
        self.completed_input.delete(0, 'end')
        self.table() # Обновить таблицу задач

    def add_task(self):
        self.task = self.name_task_input.get()
        if self.task == '':
            self.add_task_title['text'] = 'Введите название задачи'
        else:
            TaskController.add(
                task=self.task,
            )
            self.name_task_input.delete(0, 'end')
        self.table()  # Обновить таблицу сотрудников

