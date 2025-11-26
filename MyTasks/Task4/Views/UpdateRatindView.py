from tkinter import *
from tkinter import ttk
from MyTasks.Task4.Controllers.My_Tasks_4Controller import MovieController

class UpdateRatindView(Tk):
    def __init__(self, film_id):
        super().__init__()
        self.film_id = film_id
        # Конфигурация окна
        self.title("Изменить рейтинг фильма")
        self.geometry('300x300')

        # Поставить оценку
        self.rating_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.rating_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_rating = ttk.Label(self.rating_frame, text='Введите id фильма и его новый рейтинг')
        self.title_rating.pack()
        # self.id_input = ttk.Entry(self.rating_frame)
        # self.id_input.pack()
        self.rating_input = ttk.Entry(self.rating_frame)
        self.rating_input.pack()
        self.rating_button = ttk.Button(self.rating_frame, text='Изменить рейтинг')
        self.rating_button["command"] = self.update_rating
        self.rating_button.pack()

    def update_rating(self):
        # self.id = self.id_input.get()   # id фильма
        self.rating = self.rating_input.get() # новый рейтинг
        # if not self.id or not self.rating: # проверка на пустые поля
        #     self.title_rating['text'] = 'Введите id фильма и рейтинг'
        # elif not self.id.isdigit(): # Проверка на целое число
        #     self.title_rating['text'] = 'id фильма и рейтинг должны быть числами'
        try:
            float(self.rating)
        except ValueError:
            self.title_rating['text'] = 'id фильма и рейтинг должны быть числами'
            return
        else:
            MovieController.rating_update(
                id=self.film_id,
                rating=self.rating
            )
        self.destroy()

if __name__ == "__main__":
    win = UpdateRatindView()
    mainloop()