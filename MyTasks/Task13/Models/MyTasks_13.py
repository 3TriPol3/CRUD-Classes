class MyTasks_13:
    def __init__(self):
        self.__recipes = [
            {"id": 1, "name": "Борщ", "ingredients": ["свекла", "капуста", "мясо"], "cooking_time": 120, "difficulty": "средняя"}
        ]
        self.id = 2  # Следующий ID для нового рецепта

    @property
    def recipes(self):
        return self.__recipes

    @recipes.setter
    def recipes(self, dict):
        dict['id'] = self.id
        self.__recipes.append(dict)
        self.id += 1


if __name__ == "__main__":
    recipe = MyTasks_13()
    print("Исходные рецепты:", recipe.recipes)
    recipe.recipes = {"name": "Омлет", "ingredients": ["яйца", "молоко", "соль"], "cooking_time": 10, "difficulty": "легкая"}
    print("Добавлен новый рецепт:", recipe.recipes)