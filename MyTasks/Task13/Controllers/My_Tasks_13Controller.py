# from MyTasks.Task13.Models.MyTasks_13 import MyTasks_13
#
# class My_Tasks_13Controller:
#     obj = MyTasks_13()
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.recipes
#
#     # Добавление рецепта
#     @classmethod        # Классметод позволяет вызывать методы из класса не создавая для него объект
#     def add(cls, name, cooking_time, difficulty, ingredients):
#         # new_ingredients = []
#         # for element in ingredients:
#         #     new_ingredients.append(element)
#         # new_new_ingredients = [element for element in ingredients]
#         dict = {
#             "name": name,
#             "ingredients": list(ingredients),
#             "cooking_time": cooking_time,
#             "difficulty": difficulty
#         }
#         cls.obj.recipes = dict
#         return dict
#
#     # Поиск рецепта по ингредиенту
#     @classmethod
#     def find_ingredient(cls, ingredients):
#         result = []
#         for dict in cls.get():
#             if ingredients in dict["ingredients"]:
#                 result.append(dict)
#         return result
#
#     # Поиск быстрых рецептов (меньше 30 минут)
#     @classmethod
#     def fast_recipes(cls):
#         result = []
#         for dict in cls.get():
#             if dict["cooking_time"] < 30:
#                 result.append(dict)
#         return result
#
#
# if __name__ == "__main__":
#     print("Все рецепты: ", My_Tasks_13Controller.get())
#     My_Tasks_13Controller.add("Яичница", 7, "легкая", ["яйца", "лук", "масло"])
#     print("После добавления: ", My_Tasks_13Controller.get())
#     print("Рецепты с яйцами: ", My_Tasks_13Controller.find_ingredient("яйца"))
#     print("Быстрые рецепты: ", My_Tasks_13Controller.fast_recipes())

from MyTasks.Task13.Models.MyTasks_13 import *

class RecipesController:
    '''
    CRUD
    Функции: добавить рецепт, найти по ингредиенту, быстрые рецепты (<30 мин)
    '''

    # Добавить рецепт
    @classmethod
    def add(cls, name, ingredients, cooking_time, difficulty):
        # Вызвывем метод из peewee
        RecipesList.create(name=name, ingredients=ingredients, cooking_time=cooking_time, difficulty=difficulty)

    # Найти по ингредиенту - ingredients
    @classmethod
    def get_ingredients(cls, ingredients):
        return RecipesList.select().where(RecipesList.ingredients == ingredients)

    # Поиск быстрых рецептов (меньше 30 минут)
    @classmethod
    def fast_recipes(cls, cooking_time):
        return RecipesList.select().where(RecipesList.cooking_time <= cooking_time)


if __name__ == "__main__":
    # RecipesController.add('Омлет', ["яйцо", "соль", "молоко"], 3000, 'легкая')  # Добавить рецепт

    for element in RecipesController.get_ingredients('свекла'): # Найти по ингредиенту
        print(element.id, element.name, element.ingredients, element.cooking_time, element.difficulty)

    for element in RecipesController.fast_recipes(1800): # Поиск быстрых рецептов
        print(element.id, element.name, element.ingredients, element.cooking_time, element.difficulty)