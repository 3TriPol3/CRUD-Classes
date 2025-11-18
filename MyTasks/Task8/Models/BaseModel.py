from MyTasks.Task8.Connection.connection import *

class BaseModel(Model): # Наследует класс Model из peewee
    class Meta:
        database = mysql_db