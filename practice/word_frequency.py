str = 'Привет, привет твое имя как и мое имя начинается с п как слово привет'
my_dict = {}
new_str = str.split()
for word in new_str:
    word = word.strip(',.').lower()

    if word in my_dict:
        my_dict[word] +=1
    else:
        my_dict[word] = 1

print(my_dict)

