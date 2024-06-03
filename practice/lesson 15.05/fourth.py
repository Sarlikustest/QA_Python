my_list = [1, 2, 35, 40, 22, 18, 75]

def list_sum(some_list):
    some_sum = 0
    for i in some_list:
        some_sum += i
    return some_sum

#b = list_sum(my_list)

def division():
    a = int(input('На что делим? '))
    try:
        result = list_sum(my_list)/a
        print(result)
    except ZeroDivisionError:
        print('Error')
   
division()

