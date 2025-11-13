from peewee import *

# Подключение к базе данных MySQL по сети.
mysql_db = MySQLDatabase(
    'BessM82_movies_4',
    user='BessM82_movies_4',
    password='111111',
    host='10.11.13.118',
    port=3306)
if __name__ == "__main__":
    print(mysql_db.connect())