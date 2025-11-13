from peewee import *

from MyTasks.Task1.Connection.connection import mysql_db

mysql_db = MySQLDatabase(
    'BessM82_stud_5',
    user='BessM82_stud_5',
    password='111111',
    host='10.11.13.118',
    port=3306
)

if __name__ == "__main__":
    print(mysql_db.connect())