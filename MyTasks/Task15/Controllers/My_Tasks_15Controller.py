# from MyTasks.Task15.Models.MyTasks_15 import MyTasks_15
#
#
# class My_Tasks_15Controller:
#     obj = MyTasks_15()
#
#     # Добавление заказа
#     @classmethod
#     def add(cls, customer, product, amount, status, order_date):
#         cls.obj.orders = {
#             "customer": customer,
#             "product": product,
#             "amount": amount,
#             "status": status,
#             "order_date": order_date
#         }
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.orders
#
#     # Обновление статуса заказа
#     @classmethod
#     def update_status(cls, id, new_status):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["status"] = new_status
#         return dict
#
#     # Поиск заказов по имени клиента
#     @classmethod
#     def orders_by_customer(cls, customer):
#         result = []
#         for dict in cls.get():
#             if dict["customer"] == customer:
#                 result.append(dict)
#         return result
#
#     # Отмена заказа
#     @classmethod
#     def cancel_order(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 cls.get().remove(dict)
#         return dict
#
#
# if __name__ == "__main__":
#     print("Все заказы:", My_Tasks_15Controller.get())
#     My_Tasks_15Controller.add("Мария", "Телефон", 1, "новый", "2024-01-21")
#     print("После добавления:", My_Tasks_15Controller.get())
#     My_Tasks_15Controller.update_status(1, "доставлен")
#     print("После изменения статуса:", My_Tasks_15Controller.get())
#     print("Заказы клиента Иван:", My_Tasks_15Controller.orders_by_customer("Иван"))
#     My_Tasks_15Controller.cancel_order(1)
#     print("После отмены заказа:", My_Tasks_15Controller.get())

from MyTasks.Task15.Models.MyTasks_15 import *

class OrdersController:
    '''
    Функции: создать заказ, изменить статус, заказы клиента, отменить заказ
    '''

    # Cоздать заказ
    @classmethod
    def add(cls, customer, product, amount, status, order_date):
        # Вызвывем метод из peewee
        OrdersList.create(customer=customer, product=product, amount=amount, status=status, order_date=order_date)

    # Изменить статус
    @classmethod
    def update(cls, id, **kwargs):
        OrdersList.update(**kwargs).where(OrdersList.id == id).execute()

    # Заказы клиента по имени - customer
    @classmethod
    def get_customer(cls, customer):
        return OrdersList.select().where(OrdersList.customer == customer)

    # Отменить заказ - по id
    @classmethod
    def delete(cls, id):
        OrdersList.delete_by_id(id)


if __name__ == "__main__":
    # OrdersController.add('Антон', 'Ноутбук', '4', 'доставлен', '2025-04-27') # Cоздать заказ

    OrdersController.update(2, status='доставлено') # Изменить статус

    for element in OrdersController.get_customer('Антон'): # Заказы клиента по имени
        print(element.id, element.customer, element.product, element.amount, element.status, element.order_date)

    # OrdersController.delete(4)