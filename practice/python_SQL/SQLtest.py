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
            new_table = '''
        CREATE TABLE `team` (
        id INT AUTO_INCREMENT PRIMARY KEY,
        team_name VARCHAR(255),
        team_members int CHECK
            (team_members < 11)
        )
'''
            cursor.execute(new_table)

            new_insert = '''
            INSERT INTO `team` (team_name, team_members) VALUES
            ('Роботы', 9),
            ('Собаки', 10),
            ('Кошки', 7),
            ('Люди', 1),
            ('танцоры', 5),
            ('Шмели', 8),
            ('Крабы', 3),
            ('Рубли', 4),
            ('боты', 7),
            ('Роб', 9)
            '''

            cursor.execute(new_insert)
            connection.commit()

            try:
                find_people = '''
                SELECT * FROM `team`
                WHERE team_members > 5
                '''
                cursor.execute(find_people)
                for_print = cursor.fetchall()
                print(for_print)
                
            except:
                print('таких команд нет')



        



    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection error!')
    print(ex)