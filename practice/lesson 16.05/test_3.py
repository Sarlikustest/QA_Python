def compare(some_list):
    # some_list_len = len(some_list)
    # new_list = set(some_list)
    # final_list = list(new_list)
    # if some_list_len == len(final_list):
    #     print('True')
        
    # else:
    #     print('False')

    new_list = set(some_list)
    if len(new_list) == len(some_list):
        print('true')
    else:
        print('false')
    print(len(some_list))
    print(len(new_list))
    
        

   
list_1 = [1,2,3,4,5]
list_2 = [1,2,3,4,1]

compare(list_1)
compare(list_2)