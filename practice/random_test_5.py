import random
j = 0
my_list = [2,2,2,2,1,2,2,2]
if sum(my_list[0:4]) > sum(my_list[4:8]):
    my_list = my_list[4:8]
    j = j+1
    if sum(my_list[0:2]) > sum(my_list[2:4]):
        my_list = my_list[2:4]
        j = j+1
        if my_list[0] > my_list[1]:
            j = j+1
        else:
            j = j+1
    else:
        my_list = my_list[0:2]
        j = j+1
        if my_list[0] > my_list[1]:
            j = j+1
        else:
            j = j+1
     
          
else:
    my_list = my_list[0:4]
    j = j+1
    if sum(my_list[0:2]) > sum(my_list[2:4]):
        my_list = my_list[2:4]
        j = j+1
        if my_list[0] > my_list[1]:
            j = j+1
        else:
            j = j+1
    else:
        my_list = my_list[0:2]
        j = j+1
        if my_list[0] > my_list[1]:
            j = j+1
        else:
            j = j+1

print(j)
