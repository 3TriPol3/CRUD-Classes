from peewee import *

mysql_db = MySQLDatabase(
    'BessM82_meals_10',
    user='BessM82_meals_10',
    password='111111',
    host='10.11.13.118',
    port=3306
)

if __name__ == "__main__":
    print(mysql_db.connect())