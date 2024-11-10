import random
n = int(input('> '))
a = []
for i in range(n):
    a.append(random.randint(0, 99))
print(f'> {", ".join(map(str, a))}')
for i in range(n-1):
   minimum = i
   for j in range(i+1, n):
        if a[j] < a[minimum]:
            minimum = j
   seged = a[i]
   a[i] = a[minimum]
   a[minimum] = seged
print(f'> {", ".join(map(str, a))}')
