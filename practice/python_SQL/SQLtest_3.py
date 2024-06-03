import pymysql
import pymysql.cursors
from main_config_base import host,user,password,db_name


try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('succsess')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            not_tea = '''
            CREATE VIEW not_ice1 AS
            SELECT * FROM `good`
            WHERE NOT name LIKE "%АЙС ТИ%"
            '''
            cursor.execute(not_tea)

            table_update = '''
            UPDATE `not_ice1` SET name = 'чай',
            count = 1,
            price = 2
           
            '''
         
            cursor.execute(table_update)
            connection.commit()

            play = '''
            SELECT * FROM `good`
            '''
            cursor.execute(play)
    

            x = cursor.fetchall()
           

            for i in x[:20]:
                print(i)
            
            
            


    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection error!')
    print(ex)