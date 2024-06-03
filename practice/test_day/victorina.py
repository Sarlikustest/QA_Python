name = input('введите свое имя игрок ')
right_answer = 10
wrong_answer = 0

questions = {'Валюта России? ':['рубли', 'доллары'], 'Валюта Китая? ': ['юани', 'марки']}

print('Какая валюта используется в России? ')
first_question = questions['Валюта России? ']
print(first_question)
answer = input('Выберите ответ из предложенных вариантов: ')
players = {}
if answer == 'рубли':
    players[name] = right_answer
else:
    players[name] = wrong_answer


print('Какая валюта используется в Китае? ')
second_question = questions['Валюта Китая? ']
print(second_question)
answer = input('Выберите ответ из предложенных вариантов: ')
if answer == 'юани' and players[name] == 10:
    players[name] = right_answer + right_answer

elif answer == 'юани' and players[name] == 0:
    players[name] = right_answer + wrong_answer

elif answer == 'марки' and players[name] == 10:
    players[name] = right_answer + wrong_answer

else:
    players[name] = wrong_answer

for i in players:
    print('По результатам викторины игрок', i, 'получил', players[i], 'очков')