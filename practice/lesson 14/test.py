def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return None
    return x/y




# def is_valid(num_str):
#     try:
#         int(num_str)
#         return True
#     except ValueError:
#         return False
   




def calc():
    while True:
        n1 = input('Введите число:')
        n2 = input('Введите число:')
        # пример валидации всех проверок
        if not (n1.isnumeric() or (n1.startswith('-') and n1[1:].isnumeric())):
            print('ошибка введи число')
            continue
        if not (n2.isnumeric() or (n2.startswith('-') and n2[1:].isnumeric())):
            print('ошибка введи число')
            continue
        # if not is_valid(n1) or not is_valid(n2):
        #     print('ошибка введи число')
        #     continue
        n1 = int(n1)
        n2 = int(n2)


        operator = input('+-/*')


        if operator == "+":
            result = add(n1,n2)
        elif operator == "-":
            result = subtract(n1,n2)
        elif operator == "*":
            result = multiply(n1,n2)
        elif operator == "/":
            result = divide(n1,n2)
            if result is None:
                print('Ошибка деления на 0')
                continue
        else:
            print("неверная операция")
            continue
        print(result)


calc()
