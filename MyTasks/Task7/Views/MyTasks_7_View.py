from tkinter import *
from tkinter import ttk
from MyTasks.Task7.Controllers.My_Tasks_7Controller import BooksController


class MyTasks_7_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Библиотека книг")
        self.geometry('800x500')

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