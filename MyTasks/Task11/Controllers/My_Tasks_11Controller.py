from MyTasks.Task11.Models.MyTasks_11 import MyTasks_11


class My_Tasks_11Controller:
    obj = MyTasks_11()

    # Добавление события
    @classmethod
    def add(cls, title, date, time, description):
        cls.obj.events = {
            "title": title,
            "date": date,
            "time": time,
            "description": description
        }

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.events

    # События на определенную дату
    @classmethod
    def events_on_date(cls, date):
        result = []
        for dict in cls.get():
            if dict["date"] == date:
                result.append(dict)
        return result

    # Предстоящие события
    @classmethod
    def upcoming_events(cls):
        result = []
        for dict in cls.get():
            if dict["date"] >= "2025-11-10":
                result.append(dict)
        return result


if __name__ == "__main__":
    print("Все события:", My_Tasks_11Controller.get())
    My_Tasks_11Controller.add("Совещание", "2025-11-16", "10:00", "По проекту")
    print("После добавления:", My_Tasks_11Controller.get())
    print("События на 2024-02-15:", My_Tasks_11Controller.events_on_date("2024-02-15"))
    print("Предстоящие события:", My_Tasks_11Controller.upcoming_events())