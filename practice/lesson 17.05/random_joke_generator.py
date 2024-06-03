import random

joke_template = [
    'Почему {} катится вниз?',
    'Потому что {} смеятся над ним!',
    'Кто {} в книгах?',
    'Кто {}?',
    'Что сказал {} ему {} когда они встретились ?'
]
joke_elements = [
    'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
    'водитель','улитка'
]

def random_joke():

    random_element = random.choice(joke_elements)
    random_template = random.choice(joke_template)
    random_element_2 = random.choice(joke_elements)
    
    try:
        joke = random_template.format(random_element)
        print(joke)
    except:
        joke = random_template.format(random_element, random_element_2)
        print(joke)


    #print((random_template).format(random_element))
    
random_joke()