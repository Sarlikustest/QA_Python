#import string
import random

with open(r'C:\Users\AttkePC\Desktop\test-text.txt', 'r') as file:
    #num = int(input('Количество рандомных фраз? '))
    num = 1
    text = file.read()
   

    words = text.split('\n')
    #print(words)

    # for word in words:
    #     word = word.strip(',').lower()
   
        
    random_word = '\n'.join(random.choice(words) for _ in range(num))

    print(random_word)

 
    