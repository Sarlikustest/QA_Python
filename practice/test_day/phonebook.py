some_phonebook = {'Петя': '111111111', 'Федя': '222222222', 'Саша':'333333333'}
def phonebook(phone):
    while True:
        question = input('добавить нового пользователя? y/n ')
        if question == 'y':
            name = input('Имя? ')
            number = int(input('Номер  телефона? '))
            phone[name] = number
        elif question == 'n':
            print('Хорошо никого не добавляем')н
        else:
            print('Ввдено неправильное значение')
            return False
        phonebook_request = input('Вывести всю телефонную книгу? y/n ')
        if phonebook_request == 'y':
            print(phone)
            break
        elif phonebook_request == 'n':
            print('Всего хорошего ')
            break
        else:
            print('Введено неправильное значение ')
            break

phonebook(some_phonebook)
