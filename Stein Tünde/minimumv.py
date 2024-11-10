import random
n = int(input('> '))
a = [random.randint(1, 100) for k in range(n)]
minimum = a[0]
for i in range(1, n):
    if minimum > a[i]:
        minimum = a[i]
print(minimum)