from MyTasks.Task1.Connection.connection import *

class BaseModel(Model):
    class Meta:
        database = mysql_db