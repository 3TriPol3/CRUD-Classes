# from MyTasks.Task8.Models.MyTasks_8 import MyTasks_8
#
#
# class My_Tasks_8Controller:
#     obj = MyTasks_8()
#
#     # Добавление сотрудника
#     @classmethod
#     def add(cls, name, position, salary, department):
#         cls.obj.employees = {
#             "name": name,
#             "position": position,
#             "salary": salary,
#             "department": department
#         }
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.employees
#
#     # Увеличение зарплаты
#     @classmethod
#     def increase_salary(cls, id, amount):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["salary"] += amount
#         return dict
#
#     # Поиск сотрудников по отделу
#     @classmethod
#     def get_by_department(cls, department):
#         result = []
#         for dict in cls.get():
#             if dict["department"] == department:
#                 result.append(dict)
#         return result
#
#     # Увольнение сотрудника
#     @classmethod
#     def delete(cls, id):
#          for dict in cls.get():
#              if dict["id"] == id:
#                  cls.get().remove(dict)
#          return dict
#
#
# if __name__ == "__main__":
#     print("Все сотрудники:", My_Tasks_8Controller.get())
#     My_Tasks_8Controller.add("Иван", "Тестировщик", 80000, "QA")
#     print("После добавления:", My_Tasks_8Controller.get())
#     My_Tasks_8Controller.increase_salary(1, 10000)
#     print("После повышения зарплаты:", My_Tasks_8Controller.get())
#     print("Сотрудники отдела IT:", My_Tasks_8Controller.get_by_department("IT"))
#     My_Tasks_8Controller.delete(1)
#     print("После увольнения:", My_Tasks_8Controller.get())

from MyTasks.Task8.Models.MyTasks_8 import *

class StaffController:
    '''
    CRUD
    Функции: добавить сотрудника, повысить зарплату, сотрудники отдела, уволить
    '''

    # Добавить книгу
    @classmethod
    def add(cls, name, position, salary, department=False):
        # Вызвывем метод из peewee
        StaffList.create(name=name, position=position, salary=salary, department=False)

    #  Увеличение зарплаты по - id
    @classmethod
    def salary_update(cls, id, **kwargs):
        StaffList.update(**kwargs).where(StaffList.id == id).execute()

    # Сотрудники по отделам - department
    @classmethod
    def get_department(cls, department):
        return StaffList.select().where(StaffList.department == department)

    # Уволить(удалить) сотрудника по - id
    @classmethod
    def delete(cls, id):
        StaffList.delete_by_id(id)

    @classmethod
    def get(cls):
        return StaffList.select()



if __name__ == "__main__":
    # StaffController.add('Анастасия', 'Главный Бухгалтер', 75000, 'Бухгалтерия')  # Добавить сотрудника

    StaffController.salary_update(1, salary=100000)  #Увеличение зарплаты

    for element in StaffController.get_department('IT'): # Сотрудники по отделам
        print(element.id, element.name, element.position, element.salary, element.department)

    # StaffController.delete(3)  # Удалить сотрудника