import re
def password_validate(passw):
    if len(passw) < 8:
        return False
    if passw[0] != '+' and passw[len(passw) - 1] !='+':
        return False
    
    count_number = 0
    for num in passw:
        if num.isdigit():
            count_number +=1
    if count_number < 1:
        return False
    # pattern_name = r'^[a-zA-Z]'
    # if not re.match(pattern_name, passw):
    #     return False
    return True
print(password_validate("fedy1ghjkjjkj+"))
