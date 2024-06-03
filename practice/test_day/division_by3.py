my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def division_by3(some_list):
    new_list = []
    for i in some_list:
        if i%3==0 and i
         new_list.append(i)
    print(new_list)

division_by3(my_list)
