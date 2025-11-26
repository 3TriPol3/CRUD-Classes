# from MyTasks.Task18.Models.MyTasks_18 import MyTasks_18
#
#
# class My_Tasks_18Controller:
#     obj = MyTasks_18()
#
#     # Добавление оборудования
#     @classmethod
#     def add(cls, name, type, serial, status, user):
#         cls.obj.equipment = {
#             "name": name,
#             "type": type,
#             "serial": serial,
#             "status": status,
#             "user": user
#         }
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.equipment
#
#     # Изменение статуса оборудования
#     @classmethod
#     def update_status(cls, id, new_status):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["status"] = new_status
#         return dict
#
#     # Поиск оборудования по пользователю
#     @classmethod
#     def find_by_user(cls, user):
#         result = []
#         for dict in cls.get():
#             if dict["user"] == user:
#                 result.append(dict)
#         return result
#
#     # Списание оборудования
#     @classmethod
#     def write_off(cls, id):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 cls.get().remove(dict)
#         return dict
#
#
# if __name__ == "__main__":
#     print("Все оборудование:", My_Tasks_18Controller.get())
#     My_Tasks_18Controller.add("Монитор Samsung", "монитор", "DEF456", "в резерве", "не назначен")
#     print("После добавления:", My_Tasks_18Controller.get())
#     My_Tasks_18Controller.update_status(1, "в ремонте")
#     print("После изменения статуса:", My_Tasks_18Controller.get())
#     print("Оборудование пользователя Петр:", My_Tasks_18Controller.find_by_user("Петр"))
#     My_Tasks_18Controller.write_off(1)
#     print("После списания:", My_Tasks_18Controller.get())
from MyTasks.Task18.Models.MyTasks_18 import *

class EquipmentController:
    '''
    Функции: добавить оборудование, изменить статус, найти по пользователю, списать
    '''

    # добавить оборудование
    @classmethod
    def add(cls, name, type, serial, status, user):
        EquipmentList.create(name=name, type=type, serial=serial, status=status, user=user)

    # изменить статус
    @classmethod
    def update(cls, id, **kwargs):
        EquipmentList.update(**kwargs).where(EquipmentList.id == id).execute()

    # найти по пользователю
    @classmethod
    def get_user(cls, user):
        return EquipmentList.select().where(EquipmentList.user == user)

    # списать(удалить)
    @classmethod
    def delete(cls, id):
        EquipmentList.delete_by_id(id)

if __name__ == "__main__":
    # EquipmentController.add('ASUS ROG PHONE 5', 'телефон', 'SSS999', 'в работе', 'Максим') # добавить оборудование

    EquipmentController.update(1, status='в разработке') # изменить статус

    for el in EquipmentController.get_user('Петр'): # найти по пользователю
        print(el.id, el.name, el.type, el.serial, el.status, el.user)

    # EquipmentController.delete(8) # списать