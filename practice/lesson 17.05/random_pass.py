import random
import string

def generate_password():
    length = int(input())
    if length < 9 and length > 32:
        return False
    characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
    password = ''.join(random.choice(characters) for _ in range(length))
    print(password)
generate_password()

# number = random.randrange(8,32)
# b = []
# j = 0
# while j < number:
#     i = random.randrange(9)
#     b.append(i)
#     j +=1
# for j in b:
#     j = string(j)
# print(b)
