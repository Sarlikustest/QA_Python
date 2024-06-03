def word_finder(some_string):
    word = input('Какое слово искать? ')
    string_split = some_string.split()
    #print(string_split)
    for i in string_split:
        if i == word:
            print('Есть такое слово')
            break
        else:
            continue
    else:
        print('нет такого слова')
        

text = 'Привет, привет как дела? рад видеть'
word_finder(text)