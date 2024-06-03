import re

user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}

def login_check():
    
    while True:
    
        e_mail = input()
        name = input()
        password = input()

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


        if not re.match(pattern, e_mail):
            return False
    
        parts = e_mail.split('@')


        if len(parts[0])<4:
            return False
    
        
        if e_mail in user_database:
            print('Пользователь с таким именем уже зарегистрирован')
            break


        pattern_name = r'^[a-zA-Z]'
        if not re.match(pattern_name, name):
            return False
        

        pattern_pass = r'^[a-zA-Z0-9._%+-]'


        if not re.match(pattern_pass, password):
            return False
        
        count_alpha = 0
        count_lower = 0
        count_int = 0
        for letter in password:
            if letter.isalpha():
                count_alpha +=1
            if letter.islower():
                count_lower +=1
            if letter.isdigit():
                count_int +=1
        if count_alpha < 1 or count_lower < 1 or count_int < 1:
            return False
            
        if len(password)<8:
            return False
        
        print('Привет')

        question = input('Записать имя в базу данных? (да/нет) ')
        if question == 'да':
            user_database[e_mail] = {'name': name, 'password' : password}
        else:
            print('Пользователь не добавлен') 
        question = input('Вывести на экран базу данных? (да/нет) ')
        if question == 'да':
            print(user_database)
        else:
            print('Всего хорошего!') 
        return False     
        

login_check()








