import random
csucsok = list(range(10))
elek = []
for i in csucsok:
    elek.append([])
for i in range(15):
    elek[random.randint(0, 9)].append(random.randint(0, 9))

print(f'{csucsok = }')
print(f'{elek = }')

s = [0]
v = [False] * len(csucsok)
while len(s):
    q = s.pop()
    if not v[q]:
        v[q] = True
        for i in elek[q]:
            s.append(i)
print(v)
