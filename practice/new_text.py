with open(r'C:\Users\AttkePC\Desktop\test-text.txt', 'r') as file:
       words = file.readlines()
       for i in range (1, len(words), 2):
              print(words[i])
    
    