# class MyTasks_1:
#     def __init__(self):
#         self.__list_tasks = [
#             {"id": 1, "task": "Купить молоко", "completed": False},
#             {"id": 2, "task": "Сделать уроки", "completed": True}
#         ]
#         self.id = 3  # Следующий ID для новой задачи
#
#     @property
#     def tasks(self):
#         return self.__list_tasks
#
#     @tasks.setter
#     def tasks(self, dict):
#         dict['id'] = self.id
#         self.__list_tasks.append(dict)
#         self.id += 1  # Увеличиваем ID для следующей задачи
#
#
# if __name__ == "__main__":
#     task = MyTasks_1()
#     print(task.tasks)
#     task.tasks = {"task": "Новая задача", "completed": False}
#     print(task.tasks)

from MyTasks.Task1.Models.BaseModel import *

class Task(BaseModel):
    '''
    Этот клас описывает таблицу task в базе данных
    '''
    id = PrimaryKeyField() # первичный ключ в таблице
    task = CharField() # символьный тип данных (строка) с  максимальным количеством символов 255, не пустое
    completed = BooleanField(default=False) # поле Логическое, по умолчанию False

if __name__ == "__main__":
    mysql_db.create_tables([Task])
    number = IntegerField()
    date = DateField()
    datetime = DateTimeField()
    time = TimeField()