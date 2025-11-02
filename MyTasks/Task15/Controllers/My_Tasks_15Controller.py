from MyTasks.Task15.Models.MyTasks_15 import MyTasks_15


class My_Tasks_15Controller:
    obj = MyTasks_15()

    # Добавление заказа
    @classmethod
    def add(cls, customer, product, amount, status, order_date):
        cls.obj.orders = {
            "customer": customer,
            "product": product,
            "amount": amount,
            "status": status,
            "order_date": order_date
        }

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.orders

    # Обновление статуса заказа
    @classmethod
    def update_status(cls, id, new_status):
        for dict in cls.get():
            if dict["id"] == id:
                dict["status"] = new_status
        return dict

    # Поиск заказов по имени клиента
    @classmethod
    def orders_by_customer(cls, customer):
        result = []
        for dict in cls.get():
            if dict["customer"] == customer:
                result.append(dict)
        return result

    # Отмена заказа
    @classmethod
    def cancel_order(cls, id):
        for dict in cls.get():
            if dict["id"] == id:
                cls.get().remove(dict)
        return dict


if __name__ == "__main__":
    print("Все заказы:", My_Tasks_15Controller.get())
    My_Tasks_15Controller.add("Мария", "Телефон", 1, "новый", "2024-01-21")
    print("После добавления:", My_Tasks_15Controller.get())
    My_Tasks_15Controller.update_status(1, "доставлен")
    print("После изменения статуса:", My_Tasks_15Controller.get())
    print("Заказы клиента Иван:", My_Tasks_15Controller.orders_by_customer("Иван"))
    My_Tasks_15Controller.cancel_order(1)
    print("После отмены заказа:", My_Tasks_15Controller.get())