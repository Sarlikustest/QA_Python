import requests
def status():
    cite = input('Введите URL ')
    resp = requests.get(cite)
    status_code = resp.status_code

    if status_code == 200:
        return status_code, True
        # print('сайт работает')
       # return True
        
    else:
        # print(status_code)
        # print('error')
        return False

print(status())