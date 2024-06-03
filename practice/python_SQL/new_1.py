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
           
            if_insert = '''
            INSERT INTO `good` (category_id, name, count, price) VALUES
            (3,'Cucumber',20, 300);
            '''
            cursor.execute(if_insert)
            connection.commit()


            check_query = 'SELECT * FROM `good` WHERE name = "Cucumber";'
            cursor.execute(check_query)
            result = cursor.fetchone()
            if result:
               print('good')
            else:
               print('not good')


    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
