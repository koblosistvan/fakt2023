import random
db_erettsegi = int(input('Érettségi dolgozatok száma: '))
PONTHATAR = 96

pontok = []
for i in range(db_erettsegi):
    pontok.append(random.randint(0, 120))
print(pontok)
harompont = []
for i in range(db_erettsegi):
    if 93 < pontok[i] < PONTHATAR:
        harompont.append('f')
print(f'Kevesebb, mint 3 pont híján 5-ös dolgozatok száma: {len(harompont)}')
maxpont = []
for i in range(db_erettsegi):
    if pontok[i] == 120:
        maxpont.append('f')
print(f'Maxpontos dolgozatok száma: {len(maxpont)}')

#Nem tudom mit jelent a "10%-os sáv"

atlag = sum(pontok)/len(pontok)
print(f'Pontszámok átlaga: {atlag}')
