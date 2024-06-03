def check_password():
    password = input()
    if len(password) < 8:
        return False
    if password.islower == True:
        return False
    if password.isupper == True:
        return False
    if password.isdigit == True:
        return False
  
    print('Hello')
        
check_password()