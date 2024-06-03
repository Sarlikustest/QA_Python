def calculator():

    while True:
        x = int(input())
        y = int(input())
        z = input('Введите математическую операцию или stop ')
        if z == '+':
            result = x + y
        elif z == '-':
            result = x - y
        elif z == '*':
            result = x*y
        elif z == '/':
            if y == 0:
                print('Error!')
                break
            else:
                result = x/y
        elif z == 'stop':
            break
        else:
            print('Error!')
            break
        print(f'Ответ = {result}')

calculator()

# a = int(input())
# b = int(input())
# action = input('Введите математическую операцию или stop ')


# result = calculator()
# if result is None:
#     print('Error')
# else:
#     print(f'Ответ = {result}')