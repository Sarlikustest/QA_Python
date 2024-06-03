import requests

resp = requests.get('https://easysmarthub.ru/1')
status_code = resp.status_code

if status_code == 200:  # если страница существ, то выведется 200 и yes
    print(status_code)
    print('yes')
else: # если ввести некорректную страницу (например 'https://easysmarthub.ru/1') будет ошибка и соотв выведется, 404 и no
    print(status_code)
    print('no')