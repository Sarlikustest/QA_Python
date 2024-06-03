with open(r'C:\Users\AttkePC\Desktop\test-text.txt', 'r') as file:
    words = file.read()
    uniq_words = words.split()
    a = uniq_words.index('Рэдрик')
    print(uniq_words[a])
    
   
   