from MyTasks.Task8.Models.MyTasks_8 import MyTasks_8


class My_Tasks_8Controller:
    obj = MyTasks_8()

    # Добавление сотрудника
    @classmethod
    def add(cls, name, position, salary, department):
        cls.obj.employees = {
            "name": name,
            "position": position,
            "salary": salary,
            "department": department
        }

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.employees

    # Увеличение зарплаты
    @classmethod
    def increase_salary(cls, id, amount):
        for dict in cls.get():
            if dict["id"] == id:
                dict["salary"] += amount
        return dict

    # Поиск сотрудников по отделу
    @classmethod
    def get_by_department(cls, department):
        result = []
        for dict in cls.get():
            if dict["department"] == department:
                result.append(dict)
        return result

    # Увольнение сотрудника
    @classmethod
    def delete(cls, id):
         for dict in cls.get():
             if dict["id"] == id:
                 cls.get().remove(dict)
         return dict


if __name__ == "__main__":
    print("Все сотрудники:", My_Tasks_8Controller.get())
    My_Tasks_8Controller.add("Иван", "Тестировщик", 80000, "QA")
    print("После добавления:", My_Tasks_8Controller.get())
    My_Tasks_8Controller.increase_salary(1, 10000)
    print("После повышения зарплаты:", My_Tasks_8Controller.get())
    print("Сотрудники отдела IT:", My_Tasks_8Controller.get_by_department("IT"))
    My_Tasks_8Controller.delete(1)
    print("После увольнения:", My_Tasks_8Controller.get())