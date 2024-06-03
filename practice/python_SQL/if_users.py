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
            cursor.execute('SHOW TABLES LIKE "user";')
            result = cursor.fetchone()
            if not result:
               print('does not exist')
            else:
                print('exists')

            another_view = '''
             
                    SELECT * FROM user
                    WHERE email LIKE '%gmail.com'
                    AND reg_date BETWEEN '2017-01-02' AND '2017-09-30';
                

        '''
            cursor.execute(another_view)
            mails = cursor.fetchall()

            for i in mails[:10]:
                print(i)
            connection.commit()


    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)