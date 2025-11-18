# from MyTasks.Task10.Models.MyTasks_10 import MyTasks_10
#
#
# class My_Tasks_10Controller:
#     obj = MyTasks_10()
#
#     # Добавление нового приема пищи
#     @classmethod
#     def add(cls, meal, food, calories, time):
#         cls.obj.meals = {
#             "meal": meal,
#             "food": food,
#             "calories": calories,
#             "time": time
#         }
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.meals
#
#     # Подсчет калорий за день
#     @classmethod
#     def total_calories(cls):
#         total = 0
#         for dict in cls.get():
#             total += dict["calories"]
#         return total
#
#     # Приёмы пищи по времени
#     @classmethod
#     def find_by_time(cls, time):
#         result = []
#         for dict in cls.get():
#             if dict["time"] == time:
#                 result.append(dict)
#         return result
#
#
# if __name__ == "__main__":
#     print("Все приемы пищи:", My_Tasks_10Controller.get())
#     My_Tasks_10Controller.add("Ужин", "Рыба", 500, "19:00")
#     print("После добавления:", My_Tasks_10Controller.get())
#     print("Калории за день:", My_Tasks_10Controller.total_calories())
#     print("Приемы пищи в 19:00:", My_Tasks_10Controller.find_by_time("19:00"))

from MyTasks.Task10.Models.MyTasks_10 import *

class MealsController:
    '''
    CRUD
    Функции: добавить прием пищи, калории за день, найти по времени
    '''

    # Добавить прием пищи
    @classmethod
    def add(cls, meal, food, calories, time):
        # Вызвывем метод из peewee
        MealsList.create(meal=meal, food=food, calories=calories, time=time)

    # Калорий за день
    # @classmethod
    # def total_calories(cls):
    #     total = 0

    # Найти по времени - time
    @classmethod
    def get_time(cls, time):
        return MealsList.select().where(MealsList.time == time)


if __name__ == "__main__":
    # MealsController.add('Обед', 'Борщ', '1000', '11:35')  # Добавить приём пищи

    # MealsController.total_calories() # Калорий за день # /*/

    for element in MealsController.get_time('08:00'): # Найти по времени - time
        print(element.id, element.meal, element.food, element.calories, element.time)