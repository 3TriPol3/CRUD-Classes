from MyTasks.Task14.Models.MyTasks_14 import MyTasks_14


class My_Tasks_14Controller:
    obj = MyTasks_14()

    # Добавление автомобиля
    @classmethod
    def add(cls, brand, model, year, color, price):
        cls.obj.cars = {
            "brand": brand,
            "model": model,
            "year": year,
            "color": color,
            "price": price
        }

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.cars

    # Поиск автомобиля по марке
    @classmethod
    def find_by_brand(cls, brand):
        result = []
        for dict in cls.get():
            if dict["brand"] == brand:
                result.append(dict)
        return result

    # Поиск автомобилей по году
    @classmethod
    def cars_by_year(cls, year):
        result = []
        for dict in cls.get():
            if dict["year"] == year:
                result.append(dict)
        return result

    # Изменение цены автомобиля
    @classmethod
    def update_price(cls, id, new_price):
        for dict in cls.get():
            if dict["id"] == id:
                dict["price"] = new_price
        return dict


if __name__ == "__main__":
    print("Все автомобили:", My_Tasks_14Controller.get())
    My_Tasks_14Controller.add("BMW", "X5", 2022, "белый", 3500000)
    print("После добавления:", My_Tasks_14Controller.get())
    print("Автомобили марки Toyota:", My_Tasks_14Controller.find_by_brand("Toyota"))
    print("Автомобили 2020 года:", My_Tasks_14Controller.cars_by_year(2020))
    My_Tasks_14Controller.update_price(1, 2200000)
    print("После изменения цены:", My_Tasks_14Controller.get())