from tkinter import *
from tkinter import ttk
from MyTasks.Task10.Controllers.My_Tasks_10Controller import My_Tasks_10Controller


class MyTasks_10_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Учет сотрудников")
        self.geometry('1000x600')

        # Добавить приём пищи
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_meal_title = ttk.Label(self.add_frame, text="Добавить сотрудника")
        self.add_meal_title.pack()

        # Название приёма пищи
        self.meal_meal = ttk.Label(self.add_frame, text="Введите Название приёма пищи")
        self.meal_meal.pack()
        self.meal_meal_input = ttk.Entry(self.add_frame)
        self.meal_meal_input.pack()

        # Название еды
        self.position_meal = ttk.Label(self.add_frame, text="Введите должность сотрудника")
        self.position_meal.pack()
        self.position_meal_input = ttk.Entry(self.add_frame)
        self.position_meal_input.pack()

        # Количество калорий
        self.department_meal = ttk.Label(self.add_frame, text="Введите отдел сотрудника")
        self.department_meal.pack()
        self.department_meal_input = ttk.Entry(self.add_frame)
        self.department_meal_input.pack()

        # Время приёма пищи
        self.time_meal = ttk.Label(self.add_frame, text="Введите отдел сотрудника")
        self.time_meal.pack()
        self.time_meal_input = ttk.Entry(self.add_frame)
        self.time_meal_input.pack()

        # Кнопка
        self.add_staff_button = ttk.Button(self.add_frame, text="Добавить сотрудника")
        self.add_staff_button["command"] = self.add_staff
        self.add_staff_button.pack()
