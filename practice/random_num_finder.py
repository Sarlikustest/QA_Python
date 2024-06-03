import random

n = random.randint(1, 1000)

for i in range(10):
    x = int(input('Введите число:'))
    if x > n:
        print('Загаданое число меньше')
    elif x < n:
        print('Загаданное число больше')
    elif x == n:
        print('Вы угадали число')
        break
else:
    print('Вы не угадали число')

# с циклом while
   # num = random.randint(1, 1000)
#i = 0
#while i < 5:
 #   x = int(input('Введите число:'))
  #  if x > num:
   #     print('Загаданое число меньше')
    #    i += 1
    #elif x < num:
     #   print('Загаданное число больше')
      #  i += 1
   # elif x == num:
    #    print('Вы угадали число')
     #   break
#else:
 #   print('Вы не угадали число')

