from MyTasks.Task20.Models.MyTasks_20 import *

class ClientsController:
    '''
    Функции: добавить клиента, изменить статус, найти по названию, контакты клиента
    '''

    # добавить клиента
    @classmethod
    def add(cls, name, contact_person, phone, email, status):
        ClientsList.create(name=name, contact_person=contact_person, phone=phone, email=email, status=status)

    # изменить статус
    @classmethod
    def update(cls, id, **kwargs):
        ClientsList.update(**kwargs).where(ClientsList.id == id).execute()

    # найти по названию
    @classmethod
    def get_name(cls, name):
        return ClientsList.select().where(ClientsList.name == name)

    # контакты клиента
    @classmethod
    def get_contact_person(cls, contact_person):
        return ClientsList.select().where(ClientsList.contact_person == contact_person)

if __name__ == "__main__":
    ClientsController.add('ИП Антон', 'Антон', '8900402925', 'info@anton', 'активный') # добавить клиента

    ClientsController.update(1, status='неактивный') # изменить статус

    for el in ClientsController.get_name('ООО Ромашка'): # найти по названию
        print(el.id, el.name, el.contact_person, el.phone, el.email, el.status)

    for el in ClientsController.get_contact_person('Ирина'): # контакты клиента
        print(el.id, el.name, el.contact_person, el.phone, el.email, el.status)