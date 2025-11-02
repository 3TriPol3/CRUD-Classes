class MyTasks_11:
    def __init__(self):
        self.__events = [
            {"id": 1, "title": "Встреча", "date": "2024-02-15", "time": "14:00", "description": "С коллегами"}
        ]
        self.id = 2  # Следующий ID для нового события

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, dict):
        dict['id'] = self.id
        self.__events.append(dict)
        self.id += 1


if __name__ == "__main__":
    event = MyTasks_11()
    print("События:", event.events)
    event.events = {"title": "Совещание", "date": "2024-02-16", "time": "10:00", "description": "По проекту"}
    print("Новое событие:", event.events)