import random

csucsok = list(range(10))
elek = []
for csucs in csucsok:
    elek.append([])
for _ in range(15):
    elek[random.randint(0, 9)].append(random.randint(0, 9))

print(f'{csucsok=}')
print(f'{elek=}')

# szélességi bejárás
start = 0
sor = [start]
megvolt = [False] * len(csucsok)
szulo = [None] * len(csucsok)
print(f'{megvolt=}')
print(f'{szulo=}')

while len(sor) > 0:
    pass