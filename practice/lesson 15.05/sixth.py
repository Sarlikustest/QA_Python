my_list = [6, 7, 9, 6, 10]

def middle_score(some_list):
    # score = sum(some_list)/len(some_list)
    # print(score)
    some_sum = 0
    some_length = 0
    for i in some_list:
        some_sum += i
        some_length = some_length + 1
    score = some_sum/some_length
    print(score)

middle_score(my_list)