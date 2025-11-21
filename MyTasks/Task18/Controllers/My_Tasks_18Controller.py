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
