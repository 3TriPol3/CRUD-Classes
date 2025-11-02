class MyTasks_12:
    def __init__(self):
        self.__projects = [
            {"id": 1, "name": "Веб-сайт", "status": "в процессе", "deadline": "2024-03-01", "priority": "высокий"}
        ]
        self.id = 2  # Следующий ID для нового проекта

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, dict):
        dict['id'] = self.id
        self.__projects.append(dict)
        self.id += 1


if __name__ == "__main__":
    project = MyTasks_12()
    print("Исходные проекты:", project.projects)
    project.projects = {"name": "Мобильное приложение", "status": "новый", "deadline": "2024-04-15", "priority": "средний"}
    print("Добавлен новый проект:", project.projects)