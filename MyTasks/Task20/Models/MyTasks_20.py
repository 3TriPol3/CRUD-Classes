# class MyTasks_20:
#     def __init__(self):
#         self.__clients = [
#             {"id": 1, "name": "ООО Ромашка", "contact_person": "Ирина", "phone": "+79998887766", "email": "info@romashka.ru", "status": "активный"}
#         ]
#         self.id = 2  # Следующий ID для нового клиента
#
#     @property
#     def clients(self):
#         return self.__clients
#
#     @clients.setter
#     def clients(self, dict):
#         dict['id'] = self.id
#         self.__clients.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     client = MyTasks_20()
#     print("Исходные клиенты:", client.clients)
#     client.clients = {"name": "АО Весна", "contact_person": "Петр", "phone": "+79991112233", "email": "info@vesna.ru", "status": "новый"}
#     print("Добавлен новый клиент:", client.clients)

from MyTasks.Task20.Models.BaseModel import *

class ClientsList(BaseModel): # Этот класс наследует базовую модель - BaseModel
    '''
    Этот класс описывает таблицу в БД
    '''
    id = PrimaryKeyField()
    name = CharField()
    contact_person = CharField()
    phone = IntegerField()
    email = CharField()
    status = CharField()

if __name__ == "__main__":
    print(mysql_db.create_tables([ClientsList]))