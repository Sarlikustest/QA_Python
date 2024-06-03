# def division():
#     x = int(input())
#     y = int(input())
#     result = x/y
#     print(result)

# try:
#     division()
# except ZeroDivisionError:
#     print('На ноль делить нельзя')

def division(x, y):
    result = x/y
    print(result)

try:
    a = int(input())
    b = int(input())
    division(a, b) 
except ZeroDivisionError:
    print('На ноль делить нельзя')