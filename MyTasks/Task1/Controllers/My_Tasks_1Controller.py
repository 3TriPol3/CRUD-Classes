# from MyTasks.Task1.Models.MyTasks_1 import *
#
# class My_Tasks_1Controller:
#     obj = MyTasks_1()  # Создал объект класса MyTasks_1
#
#     # Добавить дело - Create
#     @classmethod        # Классметод позволяет вызывать методы из класса не создавая для него объект
#     def add(cls, task):
#         cls.obj.tasks = {
#             "task": task,
#             "completed": False
#         }
#         return True
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.tasks
#
#     # Отметить выполненной
#     @classmethod
#     def completed(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:  # Проверка на существование ID
#                 dict["completed"] = True
#                 return dict
#         return f"Задачи с ID {id} нет"
#
#     # Удалить
#     @classmethod
#     def delete(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 cls.get().remove(dict)
#         return dict
#
# if __name__ == "__main__":
#     print(My_Tasks_1Controller.get())
#     print(My_Tasks_1Controller.add("Приготовить ужин"))
#     print(My_Tasks_1Controller.get())
#     print(My_Tasks_1Controller.completed(2))
#     print(My_Tasks_1Controller.delete(1))
#     print(My_Tasks_1Controller.get())

from MyTasks.Task1.Models.MyTasks_1 import *

class TaskController:
    '''
    CRUD
    Через модель Task подключаемся к базе данных таблице task
    и упрвляем данными
    Model.create(), for executing INSERT queries.

    Model.save() and Model.update(), for executing UPDATE queries.

    Model.delete_instance() and Model.delete(), for executing DELETE queries.

    Model.select(), for executing SELECT queries.

    '''
    @classmethod
    def add(cls,task):
        Task.create(task=task) # Добавляем задачу в базу данных c помощью модели Task
    @classmethod
    def get(cls):
        return Task.select() # возвращащает список записей из таблицы в виде объектов
    @classmethod
    def show(cls,id):
       return Task.get_or_none(id) # работает с уникальными полями

    @classmethod
    def update(cls,id,**kwargs):
        Task.update(**kwargs).where(Task.id == id).execute()
    @classmethod
    def delete(cls,id):
        Task.delete_by_id(id)

if __name__ == "__main__":
    TaskController.add('Поспать')
    list = TaskController.get()
    for task in TaskController.get():
        print(
            task.id, #ид записи
            task.task,
            task.completed
        )
    TaskController.update(3,task = 'Работать',completed=True)
    # TaskController.delete(2)
    for task in TaskController.get():
        print(
            task.id, #id записи
            task.task,
            task.completed
        )