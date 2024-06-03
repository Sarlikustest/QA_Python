copy_list = []
max_copy = 10
i = 1
while i < 11:
    copy_list.append(i)
    print('Резервная копия', i, 'создана')
    i +=1
if len(copy_list) == max_copy:
    print('Количество созданных копий', len(copy_list))

