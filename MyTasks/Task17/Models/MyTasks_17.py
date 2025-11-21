# class MyTasks_17:
#     def __init__(self):
#         self.__music = [
#             {"id": 1, "title": "Bohemian Rhapsody", "artist": "Queen", "album": "A Night at the Opera", "year": 1975, "genre": "рок"}
#         ]
#         self.id = 2  # Следующий ID для нового трека
#
#     @property
#     def music(self):
#         return self.__music
#
#     @music.setter
#     def music(self, dict):
#         dict['id'] = self.id
#         self.__music.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     music = MyTasks_17()
#     print("Исходные треки:", music.music)
#     music.music = {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "album": "Led Zeppelin IV", "year": 1971, "genre": "рок"}
#     print("Добавлен новый трек:", music.music)

from MyTasks.Task17.Models.BaseModel import *

class MusicList(BaseModel): # Этот класс наследует базовую модель - BaseModel
    '''
    Этот класс описывает таблицу в базе данных
    '''
    id = PrimaryKeyField()
    title = CharField()
    artist = CharField()
    album = CharField()
    year = IntegerField()
    genre = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([MusicList])


