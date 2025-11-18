# class MyTasks_10:
#     def __init__(self):
#         self.__meals = [
#             {"id": 1, "meal": "Завтрак", "food": "Овсянка", "calories": 300, "time": "08:00"}
#         ]
#         self.id = 2  # Следующий ID для нового приема пищи
#
#     @property
#     def meals(self):
#         return self.__meals
#
#     @meals.setter
#     def meals(self, dict):
#         dict['id'] = self.id
#         self.__meals.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     meal = MyTasks_10()
#     print("Приемы пищи:", meal.meals)
#     meal.meals = {"meal": "Обед", "food": "Салат", "calories": 400, "time": "13:00"}
#     print("Новый прием пищи:", meal.meals)

from MyTasks.Task10.Models.BaseModel import *

class MealsList(BaseModel): # Этот класс наследует базовую модель - BaseModel
    '''
       Этот класс описывает таблицу в базе данных
    '''
    id = PrimaryKeyField()
    meal = CharField()
    food = CharField()
    calories = FloatField()
    time = TimeField()


if __name__ == "__main__":
    mysql_db.create_tables([MealsList])