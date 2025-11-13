from MyTasks.Task2.Connect.connection import *


class BaseModel(Model): # Наследует класс Model из peewee
    class Meta:
        database = mysql_db