# Подключение к БД - MySQL ORM Peewee
from peewee import *

#Connect to a MySQL Database on network
mysql_db = MySQLDatabase(
    'BessM82_shop_3',
    user='BessM82_shop_3',
    password='111111',
    host='10.11.13.118',
    port=3306
)


if __name__ == "__main__":
    print(mysql_db.connect())
