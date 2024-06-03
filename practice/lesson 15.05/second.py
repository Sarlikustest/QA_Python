try:
    with open(r'C:\Users\AttkePC\Desktop\test-text.txt', 'r') as file:
        words = file.read()
        print(words)
except FileNotFoundError:
    print('Файл не найден')