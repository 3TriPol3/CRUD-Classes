from MyTasks.Task4.Models.MyTasks_4 import MyTasks_4


class My_Tasks_4Controller:
    obj = MyTasks_4()  # Создал объект класса MyTasks_4

    # Добавить фильм - Create
    @classmethod
    def add(cls, title, year, rating, watched=False):
        cls.obj.movies = {
            "title": title,
            "year": year,
            "rating": rating,
            "watched": watched
        }
        return True

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.movies

    # Поставить оценку
    @classmethod
    def set_rating(cls, id, new_rating):
        for dict in cls.get():
            if dict["id"] == id:
                dict["rating"] = new_rating
                return dict
        return f"Фильма с ID {id} нет"

    # Найти по названию
    @classmethod
    def find_by_name(cls, title):
        result = []
        for dict in cls.get():
            if dict["title"] == title:
                result.append(dict)
        return result

    # Показать непросмотренные
    @classmethod
    def show_unwatched(cls):
        result = []
        for dict in cls.get():
            if not dict["watched"]:
                result.append(dict)
        return result

    # Удалить фильм
    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict["id"] == id:
                cls.get().remove(dict)
        return dict


if __name__ == "__main__":
    print(My_Tasks_4Controller.get())
    print(My_Tasks_4Controller.add("Интерстеллар", 2014, 8.6))
    print(My_Tasks_4Controller.get())
    print(My_Tasks_4Controller.set_rating(2, 9.0))
    print(My_Tasks_4Controller.find_by_name("Крест"))
    print(My_Tasks_4Controller.show_unwatched())
    print(My_Tasks_4Controller.delete(1))
    print(My_Tasks_4Controller.get())