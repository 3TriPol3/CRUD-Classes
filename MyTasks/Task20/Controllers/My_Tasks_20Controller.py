from MyTasks.Task20.Models.MyTasks_20 import MyTasks_20


class My_Tasks_20Controller:
    obj = MyTasks_20()

    # Добавление клиента
    @classmethod
    def add(cls, name, contact_person, phone, email, status):
        cls.obj.clients = {
            "name": name,
            "contact_person": contact_person,
            "phone": phone,
            "email": email,
            "status": status
        }

    # Прокси метод
    @classmethod
    def get(cls):
        return cls.obj.clients

    # Обновление статуса клиента
    @classmethod
    def update_status(cls, id, new_status):
        for dict in cls.get():
            if dict["id"] == id:
                dict["status"] = new_status
        return dict

    # Поиск клиента по имени
    @classmethod
    def find_by_name(cls, name):
        result = []
        for dict in cls.get():
            if name in dict["name"]:
                result.append(dict)
        return result

    # Контакты клиента
    @classmethod
    def get_contact_info(cls, id):
        result = {}
        for dict in cls.get():
            if dict["id"] == id:
                result = {
                    "name": dict["name"],
                    "contact_person": dict["contact_person"],
                    "phone": dict["phone"],
                    "email": dict["email"]
                }
        return result


if __name__ == "__main__":
    print("Все клиенты:", My_Tasks_20Controller.get())
    My_Tasks_20Controller.add("АО Весна", "Петр", "+79991112233", "info@vesna.ru", "новый")
    print("После добавления:", My_Tasks_20Controller.get())
    My_Tasks_20Controller.update_status(1, "неактивный")
    print("После изменения статуса:", My_Tasks_20Controller.get())
    print("Клиенты с 'ООО' в названии:", My_Tasks_20Controller.find_by_name("ООО"))
    print("Контакты клиента ID=1:", My_Tasks_20Controller.get_contact_info(1))