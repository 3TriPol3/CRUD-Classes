# from MyTasks.Task2.Models.MyTasks_2 import MyTasks_2
#
#
# class My_Tasks_2Controller:
#     obj = MyTasks_2()  # Создал объект класса MyTasks_2
#
#     # Добавить контакт - Create
#     @classmethod
#     def add(cls, name, phone, email):
#         cls.obj.contacts = {
#             "name": name,
#             "phone": phone,
#             "email": email
#         }
#         return True
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.contacts
#
#     # Найти по имени
#     @classmethod
#     def get_name(cls, name):
#         result = f'Нет - {name}'
#         for dict in cls.get():
#             if dict['name'] == name:
#                 result = f'Есть {name}'
#         return result
#
#     # Обновить телефон
#     @classmethod
#     def update_phone(cls, id, new_phone):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["phone"] = new_phone
#                 return dict
#         return f"Контакта с ID {id} нет"
#
#     # Удалить контакт
#     @classmethod
#     def delete(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 cls.get().remove(dict)
#         return dict
#
#
# if __name__ == "__main__":
#     print(My_Tasks_2Controller.get())
#     print(My_Tasks_2Controller.add("Петр", "+79123456792", "petr@mail.ru"))
#     print(My_Tasks_2Controller.get())
#     print(My_Tasks_2Controller.get_name("Иван"))
#     print(My_Tasks_2Controller.update_phone(2, "+79123456799"))
#     print(My_Tasks_2Controller.delete(1))
#     print(My_Tasks_2Controller.get())

from MyTasks.Task2.Models.MyTasks_2 import *

# Функции: добавить контакт, найти по имени, обновить телефон, удалить контакт


class PhoneController:
    '''
    CRUD
    Функции: добавить контакт, найти по имени, обновить телефон, удалить контакт
    '''

    # Добавление контакта
    @classmethod
    def add(cls, name, email, phone=0):
        # Вызвывем метод из peewee
        PhoneList.create(name=name, phone=phone, email=email)

    # Найти по имени
    @classmethod
    def get_name(cls, name):
        return PhoneList.select().where(PhoneList.name == name)

    @classmethod
    def get(cls):
        return PhoneList.select() # список объектов из таблицы

    # Обновить телефон
    @classmethod
    def update(cls, id, **kwargs):
        PhoneList.update(**kwargs).where(PhoneList.id == id).execute()

    # Удалить контакт
    @classmethod
    def delete(cls, id):
        PhoneList.delete_by_id(id)


if __name__ == "__main__":
    # PhoneController.add('Максим', '+79123458888','maxim@mail.ru' ) # Добавить контакт
    for element in PhoneController.get_name('Максим'): # Найти по имени
        print(element.id, element.name, element.phone, element.email)
    # PhoneListController.update(1, name='Олег', phone='+79199999999', email = 'maxxxim@mail.ru') # Обновить телефон
    PhoneController.delete(2) # Удалить контакт

    for element in PhoneController.get(): # Найти по имени
        print(element.id, element.name, element.phone, element.email)