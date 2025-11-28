from tkinter import *
from tkinter import ttk
from MyTasks.Task10.Controllers.My_Tasks_10Controller import MealsController


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
        self.calories_button["command"] = self.update_calories
        self.calories_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    #############################ТАБЛИЦА##############################
        columns = ('id', 'meal', 'food', 'calories', 'time')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу приёмов пищи
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения калорий при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.meal = self.tree.item(self.item, "values")[0]  # Из строки получаем id приёма пищи
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.meal)
        # window_update_grade = UpdateRatindView(self.meal)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список сотрудников из БД
        meals = MealsController.get()
        list_meals = []
        for meal in meals:
            list_meals.append(
                (meal.id,
                 meal.meal,
                 meal.food,
                 meal.calories,
                 meal.time)
            )

        # Заголовки для таблицы
        self.tree.heading('meal', text='Название приёма пищи')
        self.tree.heading('food', text='Название еды')
        self.tree.heading('calories', text='Калории')
        self.tree.heading('time', text='Время приёма пищи')
        # Добавить данные в таблицу
        for meal in list_meals:
            self.tree.insert('', END, values=meal)

    def update_calories(self):
        self.id = self.id_input.get()   # id приёма пищи
        self.calories = self.calories_input.get() # новое описание
        if not self.id or not self.calories: # проверка на пустые поля
            self.title_calories['text'] = 'Введите id приёма пищи и калории'
        elif not self.id.isdigit(): # Проверка на целое число
            self.title_calories['text'] = 'id приёма пищи и калории должны быть числами'
        try:
            self.calories
        except ValueError:
            self.title_calories['text'] = 'id приёма пищи и калории должны быть числами'
            return
        else:
            MealsController.calories_update(
                id=self.id,
                calories=self.calories
            )
        self.id_input.delete(0, 'end')
        self.calories_input.delete(0, 'end')
        self.table() # Обновить таблицу приёмов пищи


    def add_meal(self):
        self.meal = self.meal_meal_input.get()
        self.food = self.food_meal_input.get()
        self.calories = self.calories_meal_input.get()
        self.time = self.time_meal_input.get()
        if self.meal == '' or self.food == '' or self.calories == '' or self.time == '':
            self.add_meal_title['text'] = 'Введите имя, должность и отдел сотрудника'
        else:
            MealsController.add(
                meal=self.meal,
                food=self.food,
                calories=self.calories,
                time=self.time
            )
            self.meal_meal_input.delete(0, 'end')
            self.food_meal_input.delete(0, 'end')
            self.calories_meal_input.delete(0, 'end')
            self.time_meal_input.delete(0, 'end')
        self.table()  # Обновить таблицу приёмов пищи
