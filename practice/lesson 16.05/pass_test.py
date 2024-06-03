password = input()
test_list = [',','!','#','$','^','%','&','*','{','}','(',')','[',']']
for i in password:
    for j in test_list:
        if i == j:
            print('error')
b = password.count('@')
if b != 1:
    print('error')
dog_index = password.index('@')
login_length = password[0:dog_index]
if len(login_length) < 6:
    print('error')
pass_length = len(password)
domain = password[dog_index+1:pass_length]
j=0
for i in domain:
    if i == '.':
      j = j + 1  
if j == 0:
    print('error')
print(domain)

