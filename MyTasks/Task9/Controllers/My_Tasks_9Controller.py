# from MyTasks.Task9.Models.MyTasks_9 import MyTasks_9
#
#
# class My_Tasks_9Controller:
#     obj = MyTasks_9()
#
#     # Добавление игры
#     @classmethod
#     def add(cls, title, genre, platform, completed):
#         cls.obj.games = {
#             "title": title,
#             "genre": genre,
#             "platform": platform,
#             "completed": completed
#         }
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.games
#
#     # Поиск игры по жанру
#     @classmethod
#     def find_by_genre(cls, genre):
#         result = []
#         for dict in cls.get():
#             if dict["genre"] == genre:
#                 result.append(dict)
#         return result
#
#     # Отметить игру как пройденную
#     @classmethod
#     def mark_completed(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["completed"] = True
#                 return dict
#         return f"Игры с ID {id} нет"
#
#     # Фильтрация игр по платформе
#     @classmethod
#     def filter_by_platform(cls, platform):
#         result = []
#         for dict in cls.get():
#             if dict["platform"] == platform:
#                 result.append(dict)
#         return result
#
#
# if __name__ == "__main__":
#     print("Все игры:", My_Tasks_9Controller.get())
#     My_Tasks_9Controller.add("Cyberpunk 2077", "RPG", "PS5", False)
#     print("После добавления:", My_Tasks_9Controller.get())
#     My_Tasks_9Controller.mark_completed(1)
#     print("После отметки как пройденной:", My_Tasks_9Controller.get())
#     print("Игры жанра RPG:", My_Tasks_9Controller.find_by_genre("RPG"))
#     print("Игры для платформы PC:", My_Tasks_9Controller.filter_by_platform("PC"))

from MyTasks.Task9.Models.MyTasks_9 import *

class GamesController:
    '''
    CRUD
    Функции: добавить расход, сумма по категории, расходы за период
    '''