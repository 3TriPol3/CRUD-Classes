from tkinter import *
from tkinter import ttk
from MyTasks.Task2.Controllers.My_Tasks_2Controller import PhoneController


class MyTasks_2_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Телефонная книга")
        self.geometry('1000x600')

        # Добавить запись в телефонную книгу
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_phone_title = ttk.Label(self.add_frame, text="Добавить запись")
        self.add_phone_title.pack()

        # Имя
        self.name_phone = ttk.Label(self.add_frame, text="Введите Имя")
        self.name_phone.pack()
        self.name_phone_input = ttk.Entry(self.add_frame)
        self.name_phone_input.pack()


        # Телефон
        self.number_phone = ttk.Label(self.add_frame, text="Введите Телефон")
        self.number_phone.pack()
        self.number_phone_input = ttk.Entry(self.add_frame)
        self.number_phone_input.pack()


        # Электронная почта
        self.email_phone = ttk.Label(self.add_frame, text="Введите должность сотрудника")
        self.email_phone.pack()
        self.email_phone_input = ttk.Entry(self.add_frame)
        self.email_phone_input.pack()

        # Кнопка
        self.add_phone_button = ttk.Button(self.add_frame, text="Добавить сотрудника")
        self.add_phone_button["command"] = self.add_phone
        self.add_phone_button.pack()

        # Изменить телефон
        self.phone_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.phone_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_phone = ttk.Label(self.phone_frame, text='Введите id записи и телефон')
        self.title_phone.pack()
        self.id_input = ttk.Entry(self.phone_frame)
        self.id_input.pack()
        self.phone_input = ttk.Entry(self.phone_frame)
        self.phone_input.pack()
        self.phone_button = ttk.Button(self.phone_frame, text='Изменить телефон')
        self.phone_button["command"] = self.update_phone
        self.phone_button.pack()
