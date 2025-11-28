from tkinter import *
from tkinter import ttk
from MyTasks.Task10.Controllers.My_Tasks_10Controller import My_Tasks_10Controller


class MyTasks_10_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Учет Дневник питания")
        self.geometry('1000x600')

        # Добавить приём пищи
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_meal_title = ttk.Label(self.add_frame, text="Добавить приём пищи")
        self.add_meal_title.pack()

        # Название приёма пищи
        self.meal_meal = ttk.Label(self.add_frame, text="Введите Название приёма пищи")
        self.meal_meal.pack()
        self.meal_meal_input = ttk.Entry(self.add_frame)
        self.meal_meal_input.pack()

        # Название еды
        self.food_meal = ttk.Label(self.add_frame, text="Введите Название еды")
        self.food_meal.pack()
        self.food_meal_input = ttk.Entry(self.add_frame)
        self.food_meal_input.pack()

        # Количество калорий
        self.calories_meal = ttk.Label(self.add_frame, text="Введите Количество калорий")
        self.calories_meal.pack()
        self.calories_meal_input = ttk.Entry(self.add_frame)
        self.calories_meal_input.pack()

        # Время приёма пищи
        self.time_meal = ttk.Label(self.add_frame, text="Введите Время приёма пищи")
        self.time_meal.pack()
        self.time_meal_input = ttk.Entry(self.add_frame)
        self.time_meal_input.pack()

        # Кнопка
        self.add_meal_button = ttk.Button(self.add_frame, text="Добавить приём пищи")
        self.add_meal_button["command"] = self.add_meal
        self.add_meal_button.pack()

        # Изменить количество калорий
        self.calories_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.calories_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_calories = ttk.Label(self.calories_frame, text='Введите id приёма пищи и количество калорий')
        self.title_calories.pack()
        self.id_input = ttk.Entry(self.calories_frame)
        self.id_input.pack()
        self.calories_input = ttk.Entry(self.calories_frame)
        self.calories_input.pack()
        self.calories_button = ttk.Button(self.calories_frame, text='Изменить калории')
        self.calories_button["command"] = self.calories_update
        self.calories_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()
