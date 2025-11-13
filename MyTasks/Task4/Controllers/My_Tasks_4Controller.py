from MyTasks.Task4.Models.MyTasks_4 import *

class MovieController:
    '''
    CRUD
    Функции: добавить фильм, поставить оценку, найти по названию, показать непросмотренные
    '''

    @classmethod
    def add(cls, title, year, rating=0.0, watched=False):
        '''
            добавить фильм
        '''
        MovieList.create(
            title = title,
            year = year,
            rating = rating,
            watched = watched
        )
    @classmethod
    def rating_update(cls,id,rating):
        '''поставить оценку'''
        MovieList.update({MovieList.rating:rating}).where(MovieList.id == id).execute()

    @classmethod
    def get_title(cls,title):
        '''найти по названию'''
        return MovieList.select().where(MovieList.title == title)

    @classmethod
    def get_watched_false(cls):
        '''показать непросмотренные'''
        return MovieList.select().where(MovieList.watched == False)

if __name__ == "__main__":
    MovieController.add('1+1',1992) # Добавить фильм
    # MovieController.rating_update(1, 5.0) # Поставить оценку
    for movie in MovieController.get_title('крёстный отец'): # Найти по названию
        print(movie.id, movie.title,movie.rating, movie.year,movie.watched)

    for movie in MovieController.get_watched_false(): # Показать непросмотренные
        print(movie.id, movie.title, movie.rating, movie.year, movie.watched)