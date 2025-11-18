from MyTasks.Task11.Connection.connection import *

class BaseModel(Model): # Наследует класс Model из peewee
    class Meta:
        database = mysql_db