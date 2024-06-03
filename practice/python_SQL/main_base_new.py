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
            new_view = '''
            CREATE VIEW good_ice_tea AS
            SELECT id, category_id, name, count, price
            FROM `good`
            WHERE name LIKE '%Айс Ти%'
            '''
            cursor.execute(new_view)
            connection.commit()
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)

#     import pymysql
# import pymysql.cursors
# from main_config_base import host,user,password,db_name


# try:
#     connection = pymysql.connect(
#     host=host,
#     port=3306,
#     user=user,
#     password=password,
#     database=db_name,
#     cursorclass=pymysql.cursors.DictCursor
#     )
#     print('succsess')
#     print('#' * 30)
#     try:
#         with connection.cursor() as cursor:
#             #создал таблицу
#             create_table_query = '''
#             CREATE TABLE IF NOT EXISTS `students`(
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(255) NOT NULL,
#             email VARCHAR(255) NOT NULL,
#             age INT NOT NULL
#             );
#             '''
#             cursor.execute(create_table_query)
#             print('table students created')


#             #заполняю таблицу
#             insert_query = '''
#             INSERT INTO `students` (name,email,age) VALUES
#             ('jon Erik','erikspichak@gmail.com',20),
#             (' Erik','erikspichak@gmail.com',210),
#             ('jon ','erikspichak@gmail.com',230),
#             ('jona Erik','erikspichak@gmail.com',220),
#             ('joner Erik','erikspichak@gmail.com',210);
#             '''
#             cursor.execute(insert_query)
#             connection.commit()
#             print('data inserted')


#     except Exception as e:
#         print('An error ')
#         print(e)        
           
#     finally:
#         connection.close()
# except Exception as ex:
#     print('Connection rufus')
#     print(ex)
