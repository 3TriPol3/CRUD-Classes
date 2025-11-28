# from MyTasks.Task3.Models.MyTasks_3 import MyTasks_3
#
#
# class My_Tasks_3Controller:
#     obj = MyTasks_3()  # Создал объект класса MyTasks_3
#
#     # Добавить продукт - Create
#     @classmethod
#     def add(cls, product, quantity, bought=False):
#         cls.obj.products = {
#             "product": product,
#             "quantity": quantity,
#             "bought": bought
#         }
#         return True
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.products
#
#     # Отметить как купленный
#     @classmethod
#     def mark_bought(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["bought"] = True
#                 return dict
#         return f"Продукта с ID {id} нет"
#
#     # Показать некупленное
#     @classmethod
#     def show_unbought(cls):
#         result = []
#         for dict in cls.get():
#             if not dict["bought"]:
#                 result.append(dict)
#         return result
#
#     # Удалить продукт
#     @classmethod
#     def delete(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 cls.get().remove(dict)
#         return dict
#
#
# if __name__ == "__main__":
#     print(My_Tasks_3Controller.get())
#     print(My_Tasks_3Controller.add("Яблоки", 5))
#     print(My_Tasks_3Controller.get())
#     print(My_Tasks_3Controller.mark_bought(2))
#     print(My_Tasks_3Controller.show_unbought())
#     print(My_Tasks_3Controller.delete(1))
#     print(My_Tasks_3Controller.get())
from itertools import product

from MyTasks.Task3.Models.MyTasks_3 import *


class ShopingListController:
    '''
    CRUD
    Функции: добавить продукт, отметить купленным, показать некупленное, удалить
    '''

    @classmethod
    def add(cls, product, quantity, bought=False):
        # Вызвывем метод из peewee
        ShopingList.create(product=product, quantity=quantity, bought=bought)

    @classmethod
    def update(cls, id, **kwargs):
        ShopingList.update(**kwargs).where(ShopingList.id == id).execute()

    # отметить купленным
    @classmethod
    def bought(cls, id):
        cls.update(id, bought = True)

    @classmethod
    def get(cls):
        return ShopingList.select() # список объектов из таблицы

    @classmethod
    def get_not_bought(cls):
        return ShopingList.select().where(ShopingList.bought == False)

    @classmethod
    def delete(cls, id):
        ShopingList.delete_by_id(id)

    @classmethod
    def bought_update(cls, id, **kwargs):
        ShopingList.update(**kwargs).where(ShopingList.id == id).execute()


if __name__ == "__main__":
    # ShopingListController.add('хлеб', 2)
    ShopingListController.update(1, product='батон', quantity=4, bought = True)
    ShopingListController.bought(2)
    print(ShopingListController.get())
    for element in ShopingListController.get():
        print(element.id, element.product, element.quantity, element.bought)

    print('**************************************')

    for element in ShopingListController.get_not_bought():
        print(element.id, element.product, element.quantity, element.bought)

    ShopingListController.delete(4)
