from MyTasks.Task4.Models.MyTasks_4 import *

class MovieController:
    '''
    CRUD
    Функции: добавить фильм, поставить оценку, найти по названию, показать непросмотренные
    '''

    # добавить фильм
    @classmethod
    def add(cls, title, year, rating=0.0, watched=False):
        MovieList.create(title = title, year = year, rating = rating, watched = watched)

    # поставить оценку
    @classmethod
    def rating_update(cls, id, rating):
        MovieList.update({MovieList.rating:rating}).where(MovieList.id == id).execute()

    # найти по названию
    @classmethod
    def get_title(cls,title):
        return MovieList.select().where(MovieList.title == title)

    # показать непросмотренные
    @classmethod
    def get_watched_false(cls):
        '''показать непросмотренные'''
        return MovieList.select().where(MovieList.watched == False)

if __name__ == "__main__":
    # MovieController.add('1+1',1992) # Добавить фильм

    # MovieController.rating_update(1, 5.0) # Поставить оценку

    for movie in MovieController.get_title('крёстный отец'): # Найти по названию
        print(movie.id, movie.title,movie.rating, movie.year,movie.watched)

    for movie in MovieController.get_watched_false(): # Показать непросмотренные
        print(movie.id, movie.title, movie.rating, movie.year, movie.watched)