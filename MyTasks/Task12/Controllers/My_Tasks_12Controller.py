from MyTasks.Task12.Models.MyTasks_12 import MyTasks_12


class My_Tasks_12Controller:
    obj = MyTasks_12()

    # Добавление нового проекта
    @classmethod
    def add(cls, name, status, deadline, priority):
        cls.obj.projects = {
            "name": name,
            "status": status,
            "deadline": deadline,
            "priority": priority
        }

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.projects

    # Обновление статуса проекта
    @classmethod
    def update_status(cls, id, new_status):
        for dict in cls.get():
            if dict["id"] == id:
                dict["status"] = new_status
        return dict

    # Поиск проектов по приоритету
    @classmethod
    def projects_by_priority(cls, priority):
        result = []
        for dict in cls.get():
            if dict["priority"] == priority:
                result.append(dict)
        return result

    # Поиск просроченных проектов
    @classmethod
    def overdue_projects(cls):
        result = []
        for dict in cls.get():
            if dict["deadline"] < "2025-11-10":
                result.append(dict)
        return result


if __name__ == "__main__":
    print("Все проекты:", My_Tasks_12Controller.get())
    My_Tasks_12Controller.add("Мобильное приложение", "новый", "2024-04-15", "средний")
    print("После добавления:", My_Tasks_12Controller.get())
    My_Tasks_12Controller.update_status(1, "завершен")
    print("После изменения статуса:", My_Tasks_12Controller.get())
    print("Проекты с высоким приоритетом:", My_Tasks_12Controller.projects_by_priority("высокий"))
    print("Просроченные проекты:", My_Tasks_12Controller.overdue_projects())