my_list = [1, 2, 5, 10, -3, 5, -10]
for num in my_list:
    if num < 0:
        print('Первое отрицательное число в списке', num, 'его местоположение в списке', my_list.index(num)+1)
        break

    