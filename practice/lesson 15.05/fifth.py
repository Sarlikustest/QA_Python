
    
def count_letters():
    text = input()

    words = text.split()

 



#создаю 2 пустых списка для хранения слов и их частоты
    uniq_words = []
    words_count = []


# #подсчитывает частоту встречаемости каждого слова
    for word in words:
     #убирает знаки препинания
        word = word.split()
        print(word)
        # for letter in word:
        #     letter = letter.split()
        #     print(letter)
            
        


# #     #если слово уже есть в списке, увеличиваю его счетчик
#         if letter in uniq_words:
#             index = uniq_words.index(letter)
#             words_count[index] += 1
# #     #если слово встречается впервые, добавляем в список
#         else:
#             uniq_words.append(letter)
#             words_count.append(1)
# # #найти наиболее часто встречающееся слово
#     max_count = max(words_count)
#     most_common_word = uniq_words[words_count.index(max_count)]
#     print(max_count)
#     print(most_common_word)

count_letters()