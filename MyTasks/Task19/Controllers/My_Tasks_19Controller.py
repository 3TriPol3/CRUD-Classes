from MyTasks.Task19.Models.MyTasks_19 import MyTasks_19


class My_Tasks_19Controller:
    obj = MyTasks_19()

    # Добавление тренировки
    @classmethod
    def add(cls, date, type, duration, calories, notes):
        cls.obj.workouts = {
            "date": date,
            "type": type,
            "duration": duration,
            "calories": calories,
            "notes": notes
        }

    # прокси - метод
    @classmethod
    def get(cls):
        return cls.obj.workouts

    # недельная статистика
    @classmethod
    def weekly_stats(cls):
        total_duration = 0
        total_calories = 0
        for dict in cls.get():
            total_duration += dict["duration"]
            total_calories += dict["calories"]
        return {"total_duration": total_duration, "total_calories": total_calories}

    # Поиск по типу
    @classmethod
    def find_by_type(cls, workout_type):
        result = []
        for dict in cls.get():
            if dict["type"] == workout_type:
                result.append(dict)
        return result

    # Общая продолжительность
    @classmethod
    def total_duration(cls):
        total = 0
        for dict in cls.get():
            total += dict["duration"]
        return total


if __name__ == "__main__":
    print("Все тренировки:", My_Tasks_19Controller.get())
    My_Tasks_19Controller.add("2024-01-21", "плавание", 60, 500, "В бассейне")
    print("После добавления:", My_Tasks_19Controller.get())
    print("Статистика за неделю:", My_Tasks_19Controller.weekly_stats())
    print("Тренировки типа 'бег':", My_Tasks_19Controller.find_by_type("бег"))
    print("Общая продолжительность:", My_Tasks_19Controller.total_duration(), "минут")