# class MyTasks_13:
#     def __init__(self):
#         self.__recipes = [
#             {"id": 1, "name": "Борщ", "ingredients": ["свекла", "капуста", "мясо"], "cooking_time": 120, "difficulty": "средняя"}
#         ]
#         self.id = 2  # Следующий ID для нового рецепта
#
#     @property
#     def recipes(self):
#         return self.__recipes
#
#     @recipes.setter
#     def recipes(self, dict):
#         dict['id'] = self.id
#         self.__recipes.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     recipe = MyTasks_13()
#     print("Все рецепты:", recipe.recipes)
#     recipe.recipes = {"name": "Яичница", "ingredients": ["яйца", "лук", "масло"], "cooking_time": 7, "difficulty": "легкая"}
#     print("Добавлен новый рецепт:", recipe.recipes)

from MyTasks.Task13.Models.BaseModel import *

class RecipesList(BaseModel): # Этот класс наследует базовую модель - BaseModel
    '''
       Этот класс описывает таблицу в базе данных
    '''
    id = PrimaryKeyField()
    name = CharField()
    ingredients = CharField()
    cooking_time = TimeField()
    difficulty = CharField()


if __name__ == "__main__":
    mysql_db.create_tables([RecipesList])