# from MyTasks.Task7.Models.MyTasks_7 import MyTasks_7
#
#
# class My_Tasks_7Controller:
#     obj = MyTasks_7()
#
#     # Добавить книгу
#     @classmethod
#     def add(cls, title, author, year, read):
#         cls.obj.books = {
#             "title": title,
#             "author": author,
#             "year": year,
#             "read": read
#         }
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.books
#
#     # Отметить как прочитанную
#     @classmethod
#     def mark_read(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["read"] = True
#                 return dict
#         return f"Книги с ID {id} нет"
#
#     # Поиск по автору
#     @classmethod
#     def find_by_author(cls, author):
#         result = []
#         for dict in cls.get():
#             if dict["author"] == author:
#                 result.append(dict)
#         return result
#
#     # Фильтрация по году
#     @classmethod
#     def filter_by_year(cls, year):
#         result = []
#         for dict in cls.get():
#             if dict["year"] == year:
#                 result.append(dict)
#         return result
#
#
# if __name__ == "__main__":
#     print("Все книги:", My_Tasks_7Controller.get())
#     My_Tasks_7Controller.add("Над пропастью во ржи", "Сэлинджер", 1951, False)
#     print("После добавления:", My_Tasks_7Controller.get())
#     My_Tasks_7Controller.mark_read(1)
#     print("После отметки как прочитанной:", My_Tasks_7Controller.get())
#     print("Книги автора 'Оруэлл':", My_Tasks_7Controller.find_by_author("Оруэлл"))
#     print("Книги года 1967:", My_Tasks_7Controller.filter_by_year(1967))

from MyTasks.Task7.Models.MyTasks_7 import *

class BooksController:
    '''
    CRUD
    Функции: добавить расход, сумма по категории, расходы за период
    '''

    # Добавить книгу
    @classmethod
    def add(cls, title, author, year):
        # Вызвывем метод из peewee
        BooksList.create(title=title, author=author, year=year, read=False)

    # Изменить запись
    @classmethod
    def update(cls, id, **kwargs):
        BooksList.update(**kwargs).where(BooksList.id == id).execute()

    # отметить прочитанной
    @classmethod
    def read(cls, id):
        cls.update(id, read=True)

    # Найти книгу по автору - author
    @classmethod
    def get_author(cls, author):
        return BooksList.select().where(BooksList.author == author)

    #  Книги определенного года
    # @classmethod
    # def filter_by_year(cls, year):
    #     result = []



if __name__ == "__main__":
    # BooksController.add('Детство', 'Толстой', 1852)  # Добавить книгу

    BooksController.read(1) # Отметить прочитанной

    for element in BooksController.get_author('Толстой'):  # Найти по автору
        print(element.id, element.title, element.author, element.year, element.read)

    # BooksController.filter_by_year(1852) # Книги определенного года



