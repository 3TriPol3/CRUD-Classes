from tkinter import *
from tkinter import ttk
from MyTasks.Task7.Controllers.My_Tasks_7Controller import BooksController


class MyTasks_7_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Библиотека книг")
        self.geometry('1000x500')

        # Добавить книгу
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_book_title = ttk.Label(self.add_frame, text="Добавить книгу")
        self.add_book_title.pack()

        # Название книги
        self.title_book = ttk.Label(self.add_frame, text="Введите название книги")
        self.title_book.pack()
        self.title_book_input = ttk.Entry(self.add_frame)
        self.title_book_input.pack()

        # Автор книги
        self.author_book = ttk.Label(self.add_frame, text="Введите Автора книги")
        self.author_book.pack()
        self.author_book_input = ttk.Entry(self.add_frame)
        self.author_book_input.pack()

        # Кнопка
        self.add_book_button = ttk.Button(self.add_frame, text="Добавить книгу")
        self.add_book_button["command"] = self.add_book
        self.add_book_button.pack()

        # Изменить год
        self.year_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.year_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_year = ttk.Label(self.year_frame, text='Введите id книги и её год')
        self.title_year.pack()
        self.id_input = ttk.Entry(self.year_frame)
        self.id_input.pack()
        self.year_input = ttk.Entry(self.year_frame)
        self.year_input.pack()
        self.year_button = ttk.Button(self.year_frame, text='Изменить год')
        self.year_button["command"] = self.update_year
        self.year_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    #############################ТАБЛИЦА##############################
        columns = ('id', 'title', 'author', 'year', 'read')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу книг
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения года при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.book = self.tree.item(self.item, "values")[0]  # Из строки получаем id книги
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.book)
        # window_update_grade = UpdateRatindView(self.book)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список книг из БД
        books = BooksController.get()
        list_books = []
        for book in books:
            list_books.append(
                (book.id,
                book.title,
                book.author,
                book.year,
                book.read)
            )
        # Заголовки для таблицы
        self.tree.heading('title', text='Название')
        self.tree.heading('author', text='Автор')
        self.tree.heading('year', text='Год')
        self.tree.heading('read', text='Статус чтения')
        # Добавить данные в таблицу
        for book in list_books:
            self.tree.insert('', END, values=book)

    def update_year(self):
        self.id = self.id_input.get()   # id книги
        self.year = self.year_input.get() # новое описание
        if not self.id or not self.year: # проверка на пустые поля
            self.title_year['text'] = 'Введите id книги и год'
        elif not self.id.isdigit(): # Проверка на целое число
            self.title_year['text'] = 'id книги и год должны быть числами'
        try:
            self.year
        except ValueError:
            self.title_year['text'] = 'id книги и год должны быть числами'
            return
        else:
            BooksController.year_update(
                id=self.id,
                year=self.year
            )
        self.id_input.delete(0, 'end')
        self.year_input.delete(0, 'end')
        self.table() # Обновить таблицу книг

    def add_book(self):
        self.title = self.title_book_input.get()
        self.author = self.author_book_input.get()
        if self.title == '' or self.author == '':
            self.add_book_title['text'] = 'Введите Название и Автора книги'
        else:
            BooksController.add(
            title=self.title,
            author=self.author
            )
            self.title_book_input.delete(0,'end')
            self.author_book_input.delete(0,'end')
        self.table() # Обновить таблицу книг