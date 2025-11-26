from tkinter import *
from tkinter import ttk

from MyTasks.Task4.Controllers.My_Tasks_4Controller import MovieController
from MyTasks.Task4.Views.UpdateRatindView import UpdateRatindView

class MovieView(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Просмотр фильмов")
        self.geometry('800x500')

        # Добавить фильм
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8,10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_movie_title = ttk.Label(self.add_frame, text = "Добавить фильм")
        self.add_movie_title.pack()

        # Название фильма
        self.name_film = ttk.Label(self.add_frame, text="Введите название фильма")
        self.name_film.pack()
        self.name_film_input = ttk.Entry(self.add_frame)
        self.name_film_input.pack()

        # Год выпуска фильма
        self.year_film = ttk.Label(self.add_frame, text="Введите Год выпуска фильма")
        self.year_film.pack()
        self.year_film_input = ttk.Entry(self.add_frame)
        self.year_film_input.pack()

        # Кнопка
        self.add_film_button = ttk.Button(self.add_frame, text="Добавить фильм")
        self.add_film_button["command"] = self.add_film
        self.add_film_button.pack()

        # Поставить оценку
        self.rating_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.rating_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_rating = ttk.Label(self.rating_frame, text='Введите id фильма и его новый рейтинг')
        self.title_rating.pack()
        self.id_input = ttk.Entry(self.rating_frame)
        self.id_input.pack()
        self.rating_input = ttk.Entry(self.rating_frame)
        self.rating_input.pack()
        self.rating_button = ttk.Button(self.rating_frame, text='Изменить рейтинг')
        self.rating_button["command"] = self.update_rating
        self.rating_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    ######################ТАБЛИЦА########################
        columns = ('id', 'title', 'year', 'rating', 'watched')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table() # Обновить таблицу фильмов
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускать окно для изменения рейтинга при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0] # Получить строку
        self.film = self.tree.item(self.item, "values")[0] # Из строки получаем id фильма
        print(self.item)
        print(self.film)
        window_update_rating = UpdateRatindView(self.film)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Получить список фильмов из БД
        films = MovieController.get()
        list_films = []
        for film in films:
            if film.watched:
                watched = 'Просмотрен'
            else:
                watched = 'НЕ просмотрен'
            list_films.append(
                (film.id,
                film.title,
                film.year,
                film.rating,
                watched)
            )
        # Заголовки для таблицы
        self.tree.heading('title', text='Название фильма')
        self.tree.heading('year', text='Год выпуска фильма')
        self.tree.heading('rating', text='Рейтинг фильма')
        self.tree.heading('watched', text='Статус фильма')
        #Добавить данные в таблицу
        for film in list_films:
            self.tree.insert('',END, values=film)


    def update_rating(self):
        self.id = self.id_input.get()   # id фильма
        self.rating = self.rating_input.get() # новый рейтинг
        if not self.id or not self.rating: # проверка на пустые поля
            self.title_rating['text'] = 'Введите id фильма и рейтинг'
        elif not self.id.isdigit(): # Проверка на целое число
            self.title_rating['text'] = 'id фильма и рейтинг должны быть числами'
        try:
            float(self.rating)
        except ValueError:
            self.title_rating['text'] = 'id фильма и рейтинг должны быть числами'
            return
        else:
            MovieController.rating_update(
                id=self.id,
                rating=self.rating
            )
        self.id_input.delete(0, 'end')
        self.rating_input.delete(0, 'end')
        self.table() # Обновить таблицу фильмов

    def add_film(self):
        self.name = self.name_film_input.get()
        self.year = self.year_film_input.get()
        if self.name == '' or self.year == '':
            self.add_movie_title['text'] = 'Введите название и год выпуска фильма'
        else:
            MovieController.add(
            title=self.name,
            year=self.year
            )
            self.name_film_input.delete(0,'end')
            self.year_film_input.delete(0,'end')
        self.table() # Обновить таблицу фильмов