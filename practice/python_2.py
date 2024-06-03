


def calculator(x, y, z):
    while (z != 'stop'):

        if z == '+':
            return x + y
        elif z == '-':
            return x - y
        elif z == '*':
            return x*y
        elif z == '/':
            if y == 0:
                #print('WTF')
                break
            else:
                return x/y
        else:
            #print('Ты не ввел математический операнд')
            break

a = int(input())
b = int(input())
action = input('Введите математическую операцию или stop ')


result = calculator(a, b, action)
if result is None:
    print('Error')
else:
    print(f'Ответ = {result}')












