from tkinter import *
from tkinter import ttk
from MyTasks.Task6.Controllers.My_Tasks_6Controller import ExpensesController


class MyTasks_6_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Учет личных расходов")
        self.geometry('1000x500')

        # Добавить расход
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_expense_title = ttk.Label(self.add_frame, text="Добавить расход")
        self.add_expense_title.pack()

        # Количество расходов
        self.amount_expense = ttk.Label(self.add_frame, text="Введите количество расходов")
        self.amount_expense.pack()
        self.amount_expense_input = ttk.Entry(self.add_frame)
        self.amount_expense_input.pack()

        # Категория расхода
        self.category_expense = ttk.Label(self.add_frame, text="Введите Название категории")
        self.category_expense.pack()
        self.category_expense_input = ttk.Entry(self.add_frame)
        self.category_expense_input.pack()

        # Кнопка
        self.add_expense_button = ttk.Button(self.add_frame, text="Добавить расход")
        self.add_expense_button["command"] = self.add_expense
        self.add_expense_button.pack()

        # Изменить описание
        self.description_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.description_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_description = ttk.Label(self.description_frame, text='Введите id расхода и его описание')
        self.title_description.pack()
        self.id_input = ttk.Entry(self.description_frame)
        self.id_input.pack()
        self.description_input = ttk.Entry(self.description_frame)
        self.description_input.pack()
        self.description_button = ttk.Button(self.description_frame, text='Изменить описание')
        self.description_button["command"] = self.update_description
        self.description_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()
    #############################ТАБЛИЦА##############################
        columns = ('id', 'amount', 'category', 'date', 'description')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу расходов
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения описания при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.expense = self.tree.item(self.item, "values")[0]  # Из строки получаем id Расхода
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.expense)
        # window_update_grade = UpdateRatindView(self.expense)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список расходов из БД
        expenses = ExpensesController.get()
        list_expenses = []
        for expense in expenses:
            if expense.description:
                description = ''
            else:
                description = ''
            list_expenses.append(
                (expense.id,
                expense.amount,
                expense.category,
                expense.date,
                expense.description)
            )

        # Заголовки для таблицы
        self.tree.heading('amount', text='Количество')
        self.tree.heading('category', text='Категория')
        self.tree.heading('date', text='Дата')
        self.tree.heading('description', text='Описание')
        # Добавить данные в таблицу
        for student in list_expenses:
            self.tree.insert('', END, values=student)

    def update_description(self):
        self.id = self.id_input.get()   # id студента
        self.description = self.description_input.get() # новое описание
        if not self.id or not self.description: # проверка на пустые поля
            self.title_description['text'] = 'Введите id Расхода и Описание'
        # elif not self.id.isdigit(): # Проверка на целое число
        #     self.title_description['text'] = 'id студента и оценка должны быть числами'
        # try:
        #     self.description
        # except ValueError:
        #     self.title_description['text'] = 'id студента и оценка должны быть числами'
            return
        else:
            ExpensesController.description_update(
                id=self.id,
                description=self.description
            )
        self.id_input.delete(0, 'end')
        self.description_input.delete(0, 'end')
        self.table() # Обновить таблицу расходов

    def add_expense(self):
        self.amount = self.amount_expense_input.get()
        self.category = self.category_expense_input.get()
        if self.amount == '' or self.category == '':
            self.add_expense_title['text'] = 'Введите Количество и категорию расхода'
        else:
            ExpensesController.add(
            amount=self.amount,
            category=self.category
            )
            self.amount_expense_input.delete(0,'end')
            self.category_expense_input.delete(0,'end')
        self.table() # Обновить таблицу расходов
