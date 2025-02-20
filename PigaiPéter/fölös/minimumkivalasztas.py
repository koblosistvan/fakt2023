import random
a = []
for i in range(20):
    a.append(random.randint(0,20))
print(a)
for i in range(len(a) - 2):
    min = i
    for j in range(i + 1 , len(a)):
        if a[j]<a[min]:
            min = j
    seged = a[i]
    a[i] = a[min]
    a[min] = seged
print(a)
