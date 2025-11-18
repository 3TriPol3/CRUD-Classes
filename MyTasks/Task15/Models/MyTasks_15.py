# class MyTasks_15:
#     def __init__(self):
#         self.__orders = [
#             {"id": 1, "customer": "Иван", "product": "Ноутбук", "amount": 1, "status": "доставляется", "order_date": "2024-01-20"}
#         ]
#         self.id = 2  # Следующий ID для нового заказа
#
#     @property
#     def orders(self):
#         return self.__orders
#
#     @orders.setter
#     def orders(self, dict):
#         dict['id'] = self.id
#         self.__orders.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     order = MyTasks_15()
#     print("Исходные заказы:", order.orders)
#     order.orders = {"customer": "Мария", "product": "Телефон", "amount": 1, "status": "новый", "order_date": "2024-01-21"}
#     print("Добавлен новый заказ:", order.orders)

from MyTasks.Task15.Models.BaseModel import *

class OrdersList(BaseModel): # Этот класс наследует базовую модель - BaseModel
    '''
    Этот класс описывает таблицу в базе данных
    '''
    id = PrimaryKeyField()
    customer =CharField()
    product =CharField()
    amount = IntegerField()
    status = CharField()
    order_date = DateField()

if __name__ == "__main__":
    mysql_db.create_tables([OrdersList])