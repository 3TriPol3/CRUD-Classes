# class MyTasks_14:
#     def __init__(self):
#         self.__cars = [
#             {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2020, "color": "черный", "price": 2000000}
#         ]
#         self.id = 2  # Следующий ID для нового автомобиля
#
#     @property
#     def cars(self):
#         return self.__cars
#
#     @cars.setter
#     def cars(self, dict):
#         dict['id'] = self.id
#         self.__cars.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     car = MyTasks_14()
#     print("Исходные автомобили:", car.cars)
#     car.cars = {"brand": "BMW", "model": "X5", "year": 2022, "color": "белый", "price": 3500000}
#     print("Добавлен новый автомобиль:", car.cars)

from MyTasks.Task14.Models.BaseModel import *

class CarsList(BaseModel): # Этот класс наследует базовую модель - BaseModel
    '''
    Этот класс описывает таблицу в базе данных
    '''
    id = PrimaryKeyField()
    brand = CharField()
    model = CharField()
    year = IntegerField()
    color = CharField()
    price = FloatField()

if __name__ == "__main__":
    mysql_db.create_tables([CarsList])