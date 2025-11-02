from MyTasks.Task13.Models.MyTasks_13 import MyTasks_13


class My_Tasks_13Controller:
    obj = MyTasks_13()

    # Добавление рецепта
    @classmethod
    def add(cls, name, ingredients, cooking_time, difficulty):
        cls.obj.recipes = {
            "name": name,
            "ingredients": ingredients,
            "cooking_time": cooking_time,
            "difficulty": difficulty
        }

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.recipes

    # Поиск рецепта по ингредиенту
    @classmethod
    def find_by_ingredient(cls, ingredient):
        result = []
        for dict in cls.get():
            if ingredient in dict["ingredients"]:
                result.append(dict)
        return result

    # Поиск быстрых рецептов (меньше 30 минут)
    @classmethod
    def quick_recipes(cls):
        result = []
        for dict in cls.get():
            if dict["cooking_time"] < 30:
                result.append(dict)
        return result


if __name__ == "__main__":
    print("Все рецепты:", My_Tasks_13Controller.get())
    My_Tasks_13Controller.add("Омлет", ["яйца", "молоко", "соль"], 10, "легкая")
    print("После добавления:", My_Tasks_13Controller.get())
    print("Рецепты с яйцами:", My_Tasks_13Controller.find_by_ingredient("яйца"))
    print("Быстрые рецепты:", My_Tasks_13Controller.quick_recipes())