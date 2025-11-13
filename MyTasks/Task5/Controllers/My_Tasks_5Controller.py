# from MyTasks.Task5.Models.MyTasks_5 import MyTasks_5
#
#
# class My_Tasks_5Controller:
#     obj = MyTasks_5()  # Создал объект класса MyTasks_5
#
#     # Добавить студента - Create
#     @classmethod
#     def add(cls, name, age, grade):
#         cls.obj.students = {
#             "name": name,
#             "age": age,
#             "grade": grade
#         }
#         return True
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.students
#
#     # Обновить оценку
#     @classmethod
#     def update_grade(cls, id, new_grade):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["grade"] = new_grade
#                 return dict
#         return f"Студента с ID {id} нет"
#
#     # Найти по имени
#     @classmethod
#     def find_by_name(cls, name):
#         result = []
#         for dict in cls.get():
#             if dict["name"] == name:
#                 result.append(dict)
#         return result
#
#     # Удалить студента
#     @classmethod
#     def delete(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 cls.get().remove(dict)
#         return dict
#
#
# if __name__ == "__main__":
#     print(My_Tasks_5Controller.get())
#     print(My_Tasks_5Controller.add("Мария", 22, "A"))
#     print(My_Tasks_5Controller.get())
#     print(My_Tasks_5Controller.update_grade(2, "C"))
#     print(My_Tasks_5Controller.find_by_name("Ан"))
#     print(My_Tasks_5Controller.delete(1))
#     print(My_Tasks_5Controller.get())

from MyTasks.Task5.Models.MyTasks_5 import *

class StudentsController:
    '''
    Через модель подключаемся к базе данных к таблице и управляем данными
    CRUD
    Функции: добавить студента, изменить оценку, найти по имени, удалить студента
    '''

    # Добавить нового студента
    @classmethod
    def add(cls, name, age, grade):
        # Вызвывем метод из peewee (create)
        StudentsList.create(name=name, age=age, grade=grade)

    # Изменить оценку студента по - id
    @classmethod
    def update(cls, id, **kwargs):
        StudentsList.update(**kwargs).where(StudentsList.id == id).execute()

    # Найти студента по имени - name
    @classmethod
    def get_name(cls, name):
        return StudentsList.select().where(StudentsList.name == name)

    # Удалить студента по - id
    @classmethod
    def delete(cls, id):
        StudentsList.delete_by_id(id)


if __name__ == "__main__":
    # StudentsController.add('Sergey','25','C') # Добавить Студента

    # StudentsController.update(5, grade='D') # Изменить оценку

    for element in StudentsController.get_name('Max'): # Найти по имени
        print(element.id, element.name, element.age, element.grade)

    # StudentsController.delete(1)  # Удалить студента