from tkinter import *
from tkinter import ttk
from MyTasks.Task8.Controllers.My_Tasks_8Controller import StaffController


class MyTasks_8_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Учет сотрудников")
        self.geometry('1000x500')

        # Добавить сотрудника
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_staff_title = ttk.Label(self.add_frame, text="Добавить сотрудника")
        self.add_staff_title.pack()

        # Имя сотрудника
        self.name_staff = ttk.Label(self.add_frame, text="Введите Имя сотрудника")
        self.name_staff.pack()
        self.name_staff_input = ttk.Entry(self.add_frame)
        self.name_staff_input.pack()

        # Должность сотрудника
        self.position_staff = ttk.Label(self.add_frame, text="Введите должность сотрудника")
        self.position_staff.pack()
        self.position_staff_input = ttk.Entry(self.add_frame)
        self.position_staff_input.pack()

        # Отдел сотрудника
        self.department_staff = ttk.Label(self.add_frame, text="Введите отдел сотрудника")
        self.department_staff.pack()
        self.department_staff_input = ttk.Entry(self.add_frame)
        self.department_staff_input.pack()

        # Кнопка
        self.add_staff_button = ttk.Button(self.add_frame, text="Добавить сотрудника")
        self.add_staff_button["command"] = self.add_staff
        self.add_staff_button.pack()

        # Изменить(увеличить) зарплату
        self.salary_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.salary_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_salary = ttk.Label(self.salary_frame, text='Введите id сотрудника и его зарплату')
        self.title_salary.pack()
        self.id_input = ttk.Entry(self.salary_frame)
        self.id_input.pack()
        self.salary_input = ttk.Entry(self.salary_frame)
        self.salary_input.pack()
        self.salary_button = ttk.Button(self.salary_frame, text='Изменить зарплату')
        self.salary_button["command"] = self.update_salary
        self.salary_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    #############################ТАБЛИЦА##############################
        columns = ('id', 'name', 'position', 'salary', 'department')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу сотрудников
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения зарплаты при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.staff = self.tree.item(self.item, "values")[0]  # Из строки получаем id сотрудника
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.staff)
        # window_update_grade = UpdateRatindView(self.staff)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список сотрудников из БД
        staffs = StaffController.get()
        list_staffs = []
        for staff in staffs:
            list_staffs.append(
                (staff.id,
                 staff.name,
                 staff.position,
                 staff.salary,
                 staff.department)
            )

        # Заголовки для таблицы
        self.tree.heading('name', text='Имя сотрудника')
        self.tree.heading('position', text='Должность')
        self.tree.heading('salary', text='Зарплата')
        self.tree.heading('department', text='Отдел')
        # Добавить данные в таблицу
        for staff in list_staffs:
            self.tree.insert('', END, values=staff)

    def update_salary(self):
        self.id = self.id_input.get()   # id сотрудника
        self.salary = self.salary_input.get() # новое описание
        if not self.id or not self.salary: # проверка на пустые поля
            self.title_salary['text'] = 'Введите id сотрудника и зарплату'
        elif not self.id.isdigit(): # Проверка на целое число
            self.title_salary['text'] = 'id сотрудника и зарплата должны быть числами'
        try:
            self.salary
        except ValueError:
            self.title_salary['text'] = 'id сотрудника и зарплата должны быть числами'
            return
        else:
            StaffController.salary_update(
                id=self.id,
                salary=self.salary
            )
        self.id_input.delete(0, 'end')
        self.salary_input.delete(0, 'end')
        self.table() # Обновить таблицу сотрудников

    def add_staff(self):
        self.name = self.name_staff_input.get()
        self.position = self.position_staff_input.get()
        self.department = self.department_staff_input.get()
        if self.name == '' or self.position == '' or self.department == '':
            self.add_staff_title['text'] = 'Введите имя, должность и отдел сотрудника'
        else:
            StaffController.add(
                name=self.name,
                position=self.position,
                department=self.department
            )
            self.name_staff_input.delete(0, 'end')
            self.position_staff_input.delete(0, 'end')
            self.department_staff_input.delete(0, 'end')
        self.table()  # Обновить таблицу сотрудников


