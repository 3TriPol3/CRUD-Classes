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