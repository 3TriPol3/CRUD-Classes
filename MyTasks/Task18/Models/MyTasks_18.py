class MyTasks_18:
    def __init__(self):
        self.__equipment = [
            {"id": 1, "name": "Ноутбук Dell", "type": "ноутбук", "serial": "ABC123", "status": "в работе", "user": "Петр"}
        ]
        self.id = 2  # Следующий ID для нового оборудования

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, dict):
        dict['id'] = self.id
        self.__equipment.append(dict)
        self.id += 1


if __name__ == "__main__":
    equip = MyTasks_18()
    print("Исходное оборудование:", equip.equipment)
    equip.equipment = {"name": "Монитор Samsung", "type": "монитор", "serial": "DEF456", "status": "в резерве", "user": "не назначен"}
    print("Добавлено новое оборудование:", equip.equipment)