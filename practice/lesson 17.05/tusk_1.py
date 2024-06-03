a = input()
c = []

for i in a:
    c.append(i)

b = len(c)
j = 0
while j < b:
    c[j] = int(c[j])
    j +=1


print(sum(c))

