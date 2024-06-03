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
            for_python = '''
            SELECT *, YEAR(creation_date) as `year_only`
            FROM `order`
            WHERE `status_id` IN (2, 4)
            '''
            cursor.execute(for_python)
            for_print = cursor.fetchall()
            for i in for_print:
                print(i)
                


    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)