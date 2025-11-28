# class MyTasks_9:
#     def __init__(self):
#         self.__games = [
#             {"id": 1, "title": "The Witcher 3", "genre": "RPG", "platform": "PC", "completed": True}
#         ]
#         self.id = 2  # Следующий ID для новой игры
#
#     @property
#     def games(self):
#         return self.__games
#
#     @games.setter
#     def games(self, dict):
#         dict['id'] = self.id
#         self.__games.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     game = MyTasks_9()
#     print("Исходные игры:", game.games)
#     game.games = {"title": "Cyberpunk 2077", "genre": "RPG", "platform": "PS5", "completed": False}
#     print("Добавлена новая игра:", game.games)


from MyTasks.Task9.Models.BaseModel import *

class GamesList(BaseModel): # Этот класс наследует базовую модель - BaseModel
    '''
       Этот класс описывает таблицу в базе данных
    '''
    id = PrimaryKeyField()
    title = CharField()
    genre = CharField()
    platform = CharField()
    completed = BooleanField(default=False)


if __name__ == "__main__":
    mysql_db.create_tables([GamesList])