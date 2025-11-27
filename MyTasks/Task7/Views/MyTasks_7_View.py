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

        # год книги
        self.year_book = ttk.Label(self.add_frame, text="Введите год книги")
        self.year_book.pack()
        self.year_book_input = ttk.Entry(self.add_frame)
        self.year_book_input.pack()

        # Кнопка
        self.add_book_button = ttk.Button(self.add_frame, text="Добавить книгу")
        self.add_book_button["command"] = self.add_book
        self.add_book_button.pack()

        # Изменить год
        self.read_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.read_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_read = ttk.Label(self.read_frame, text='Введите id книги и её статус')
        self.title_read.pack()
        self.id_input = ttk.Entry(self.read_frame)
        self.id_input.pack()
        self.read_input = ttk.Entry(self.read_frame)
        self.read_input.pack()
        self.read_button = ttk.Button(self.read_frame, text='Изменить статус')
        self.read_button["command"] = self.update_read
        self.read_button.pack()

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

    def update_read(self):
        self.id = self.id_input.get()   # id книги
        self.read = self.read_input.get() # новое описание
        if not self.id or not self.read: # проверка на пустые поля
            self.title_read['text'] = 'Введите id книги и статус'
            return
        else:
            BooksController.read_update(
                id=self.id,
                read=self.read
            )
        self.id_input.delete(0, 'end')
        self.read_input.delete(0, 'end')
        self.table() # Обновить таблицу книг

    def add_book(self):
        self.title = self.title_book_input.get()
        self.author = self.author_book_input.get()
        self.year = self.year_book_input.get()
        if self.title == '' or self.author == '' or self.year == '':
            self.add_book_title['text'] = 'Введите Название, Автора и год книги'
        else:
            BooksController.add(
            title=self.title,
            author=self.author,
            year=self.year
            )
            self.title_book_input.delete(0,'end')
            self.author_book_input.delete(0,'end')
            self.year_book_input.delete(0, 'end')
        self.table() # Обновить таблицу книг