from MyTasks.Task4.Models.BaseModel import *

class MovieList(BaseModel): # Этот класс наследует базовую модель - BaseModel
    '''
    movies = [{"id": 1, "title": "Крестный отец", "year": 1972, "rating": 9.2, "watched":True}]
    Этот класс описывает таблицу в базе данных
    '''
    id = PrimaryKeyField()
    title = CharField()
    year = IntegerField()
    rating = FloatField(default=0.0)
    watched = BooleanField(default=False)

if __name__ == "__main__":
    mysql_db.create_tables([MovieList])