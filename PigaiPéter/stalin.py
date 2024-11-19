import random
a = []
for i in range(20):
    a.append(random.randint(0,20))
sorted = [a[0]]
print(a)
for i in range(len(a)-1):
    if sorted[len(sorted)-1] < a[i+1]:
        sorted.append(a[i+1])
print(sorted)