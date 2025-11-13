from MyTasks.Task3.Connect.connection import *


class BaseModel(Model): # Наследует класс Model из peewee
    class Meta:
        database = mysql_db