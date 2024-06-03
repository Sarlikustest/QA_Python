try:
    a = int(input())
    b = int(input())
    result = a/b
    print(result)
except ZeroDivisionError:
    print('На ноль делить нельзя')
except ValueError:
    print('Введено не число')
