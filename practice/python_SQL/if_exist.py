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
            if_exist = '''
            CREATE VIEW did_exist AS
            SELECT 
                good_category.id as try_exist_id,
                good_category.parent_id as try_exist_parent_id,
                good_category.name as try_exist_name
            FROM 
                good_category 
            '''
            cursor.execute(if_exist)
            connection.commit()
            if  if_exist:
                print('table exist')
            else:
                print('table_not_exist')

        with connection.cursor() as cursor:
            if_null = '''
            CREATE VIEW total_null AS
            SELECT
            (SELECT COUNT(*) FROM good_category WHERE id IS NULL) + (SELECT COUNT(*) FROM good_category WHERE parent_id IS NULL) +(SELECT COUNT(*) FROM good_category WHERE name IS NULL) AS total_null
            '''
            cursor.execute(if_null)
            
            connection.commit()

        if_nul = '''
            CREATE VIEW total_null AS
            SELECT
            (SELECT COUNT(*) FROM good_category WHERE id IS NULL) + (SELECT COUNT(*) FROM good_category WHERE parent_id IS NULL) +(SELECT COUNT(*) FROM good_category WHERE name IS NULL) AS total_null
            '''
        cursor.execute(if_nul)
        null_counts = cursor.fetchone()
        print(null_counts)
        connection.commit()

    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)