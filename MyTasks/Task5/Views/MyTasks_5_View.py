from tkinter import *
from tkinter import ttk

from MyTasks.Task5.Controllers.My_Tasks_5Controller import StudentsController


class MyTasks_5_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Список студентов")
        self.geometry('800x500')

        # Добавить студента
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_student_title = ttk.Label(self.add_frame, text="Добавить студента")
        self.add_student_title.pack()

        # Имя студента
        self.name_student = ttk.Label(self.add_frame, text="Введите имя студента")
        self.name_student.pack()
        self.name_student_input = ttk.Entry(self.add_frame)
        self.name_student_input.pack()

        # Количество лет
        self.age_student = ttk.Label(self.add_frame, text="Введите Количество лет студента")
        self.age_student.pack()
        self.age_student_input = ttk.Entry(self.add_frame)
        self.age_student_input.pack()

        # Кнопка
        self.add_student_button = ttk.Button(self.add_frame, text="Добавить студента")
        self.add_student_button["command"] = self.add_student
        self.add_student_button.pack()

        # Изменить оценку
        self.grade_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.grade_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_grade = ttk.Label(self.grade_frame, text='Введите id студента и его новую оценку')
        self.title_grade.pack()
        self.id_input = ttk.Entry(self.grade_frame)
        self.id_input.pack()
        self.grade_input = ttk.Entry(self.grade_frame)
        self.grade_input.pack()
        self.grade_button = ttk.Button(self.grade_frame, text='Изменить рейтинг')
        self.grade_button["command"] = self.update_grade
        self.grade_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    #############################ТАБЛИЦА##############################
        columns = ('id', 'name', 'age', 'grade')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу студентов
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения оценки при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.student = self.tree.item(self.item, "values")[0]  # Из строки получаем id Студента
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.student)
        # window_update_grade = UpdateRatindView(self.student)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список студентов из БД
        students = StudentsController.get()
        list_students = []
        for student in students:
            list_students.append(
                (student.id,
                student.name,
                student.age,
                student.grade)
            )

        # Заголовки для таблицы
        self.tree.heading('name', text='Имя студента')
        self.tree.heading('age', text='Количество лет')
        self.tree.heading('grade', text='Оценка')
        # Добавить данные в таблицу
        for student in list_students:
            self.tree.insert('', END, values=student)

    def update_grade(self):
        self.id = self.id_input.get()   # id студента
        self.grade = self.grade_input.get() # новая оценка
        if not self.id or not self.grade: # проверка на пустые поля
            self.title_grade['text'] = 'Введите id студента и оценку'
        # elif not self.id.isdigit(): # Проверка на целое число
        #     self.title_grade['text'] = 'id студента и оценка должны быть числами'
        # try:
        #     self.grade
        # except ValueError:
        #     self.title_grade['text'] = 'id студента и оценка должны быть числами'
            return
        else:
            StudentsController.grade_update(
                id=self.id,
                grade=self.grade
            )
        self.id_input.delete(0, 'end')
        self.grade_input.delete(0, 'end')
        self.table() # Обновить таблицу студентов

    def add_student(self):
        self.name = self.name_student_input.get()
        self.age = self.age_student_input.get()
        if self.name == '' or self.age == '':
            self.add_student_title['text'] = 'Введите имя и количество лет студента'
        else:
            StudentsController.add(
            name=self.name,
            age=self.age
            )
            self.name_student_input.delete(0,'end')
            self.age_student_input.delete(0,'end')
        self.table() # Обновить таблицу студентов