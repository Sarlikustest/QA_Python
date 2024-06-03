import pymysql
import pymysql.cursors

from main_config_base import host, user, password, db_name 
try:
    connection = pymysql.connect(
        host = host,
        port = 3306,  # его нет в подключенном файле mai_config_base - берем его в настройках open server'а
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print('success')
    print('#'*30)

    try:
        with connection.cursor() as cursor:
            create_table_q = 'CREATE TABLE `users`(id INT AUTO_INCREMENT, name VARCHAR(32), password VARCHAR(32), email VARCHAR(32), PRIMARY KEY (id))'
            cursor.execute(create_table_q)
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)