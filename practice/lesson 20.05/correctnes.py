import re

def correctness():
    tel_num = input('Введите номер, начиная с + ')
    if tel_num[0] != '+' or len(tel_num) != 12:
        return False
        
    num= tel_num[1:11]
    pattern_tel = r'^[0-9]'
    if not re.match(pattern_tel, num):
        return False
    return True
        
    
print(correctness())