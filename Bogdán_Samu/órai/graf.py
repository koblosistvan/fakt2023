import random
csucsok = list(range(10))
elek = []
for i in csucsok:
    elek.append([])
for i in range(15):
    elek[random.randint(0, 9)].append(random.randint(0, 9))

print(f'{csucsok=}')
print(f'{elek=}')

start = 0
sor = [start]
megvolt = [False] * len(csucsok)
szulo = [None] * len(csucsok)
