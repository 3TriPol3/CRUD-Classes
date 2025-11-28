from tkinter import *
from tkinter import ttk
from MyTasks.Task9.Controllers.My_Tasks_9Controller import GamesController


class MyTasks_9_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Учет сотрудников")
        self.geometry('1000x600')

        # Добавить игру
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_game_title = ttk.Label(self.add_frame, text="Добавить игру")
        self.add_game_title.pack()

        # Название игры
        self.title_game = ttk.Label(self.add_frame, text="Введите Название игры")
        self.title_game.pack()
        self.title_game_input = ttk.Entry(self.add_frame)
        self.title_game_input.pack()

        # Жанр игры
        self.genre_game = ttk.Label(self.add_frame, text="Введите Жанр игры")
        self.genre_game.pack()
        self.genre_game_input = ttk.Entry(self.add_frame)
        self.genre_game_input.pack()

        # Платформа игры
        self.platform_game = ttk.Label(self.add_frame, text="Введите Платформу игры")
        self.platform_game.pack()
        self.platform_game_input = ttk.Entry(self.add_frame)
        self.platform_game_input.pack()

        # Кнопка
        self.add_game_button = ttk.Button(self.add_frame, text="Добавить игру")
        self.add_game_button["command"] = self.add_game
        self.add_game_button.pack()

        # Изменить статус прохождения игры
        self.completed_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.completed_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_completed = ttk.Label(self.completed_frame, text='Введите id игры и её статус')
        self.title_completed.pack()
        self.id_input = ttk.Entry(self.completed_frame)
        self.id_input.pack()
        self.completed_input = ttk.Entry(self.completed_frame)
        self.completed_input.pack()
        self.completed_button = ttk.Button(self.completed_frame, text='Изменить статус прохождения')
        self.completed_button["command"] = self.update_completed
        self.completed_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    #############################ТАБЛИЦА##############################
        columns = ('id', 'title', 'genre', 'platform', 'completed')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу игр
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения статуса при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.game = self.tree.item(self.item, "values")[0]  # Из строки получаем id игры
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.game)
        # window_update_grade = UpdateRatindView(self.game)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список игр из БД
        games = GamesController.get()
        list_games = []
        for game in games:
            list_games.append(
                (game.id,
                 game.title,
                 game.genre,
                 game.platform,
                 game.completed)
            )

            # Заголовки для таблицы
            self.tree.heading('title', text='Название игры')
            self.tree.heading('genre', text='Жанр игры')
            self.tree.heading('platform', text='Платформа')
            self.tree.heading('completed', text='Статус прохождения')
            # Добавить данные в таблицу
            for game in list_games:
                self.tree.insert('', END, values=game)

    def update_completed(self):
        self.id = self.id_input.get()   # id сотрудника
        self.completed = self.completed_input.get() # новое описание
        if not self.id or not self.completed: # проверка на пустые поля
            self.title_completed['text'] = 'Введите id игры и её статус'
            return
        else:
            GamesController.update_completed(
                id=self.id,
                completed=self.completed
            )
        self.id_input.delete(0, 'end')
        self.completed_input.delete(0, 'end')
        self.table() # Обновить таблицу игр

    def add_game(self):
        self.title = self.title_game_input.get()
        self.genre = self.genre_game_input.get()
        self.platform = self.platform_game_input.get()
        if self.title == '' or self.genre == '' or self.platform == '':
            self.add_game_title['text'] = 'Введите Название игры, Жанр и Платформу игры'
        else:
            GamesController.add(
                title=self.title,
                genre=self.genre,
                platform=self.platform
            )
            self.title_game_input.delete(0, 'end')
            self.genre_game_input.delete(0, 'end')
            self.platform_game_input.delete(0, 'end')
        self.table()  # Обновить таблицу сотрудников