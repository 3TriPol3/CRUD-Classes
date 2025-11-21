# class MyTasks_19:
#     def __init__(self):
#         self.__workouts = [
#             {"id": 1, "date": "2024-01-20", "type": "бег", "duration": 45, "calories": 400, "notes": "Утренняя пробежка"}
#         ]
#         self.id = 2  # Следующий ID для новой тренировки
#
#     @property
#     def workouts(self):
#         return self.__workouts
#
#     @workouts.setter
#     def workouts(self, dict):
#         dict['id'] = self.id
#         self.__workouts.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     workout = MyTasks_19()
#     print("Исходные тренировки:", workout.workouts)
#     workout.workouts = {"date": "2024-01-21", "type": "плавание", "duration": 60, "calories": 500, "notes": "В бассейне"}
#     print("Добавлена новая тренировка:", workout.workouts)
