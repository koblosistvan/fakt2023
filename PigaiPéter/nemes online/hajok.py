forras = open('hajok.txt', mode='r', encoding='utf-8')
kontenerdbhajocap = forras.readline().strip().split(' ')
kontenerdb = int(kontenerdbhajocap[0])
hajocap = int(kontenerdbhajocap[1])
allomasok = []

for sor in forras:
    allomasok.append(sor.strip())
forras.close()

varosok = set(allomasok)

import math
hajok = []
for varos in varosok:
    andor = allomasok.count(varos)
    print(f'{varos} {math.ceil(andor / hajocap)} {andor % hajocap}')
    hajok.append([varos, math.ceil(andor / hajocap), andor % hajocap])

for i in range(len(hajok)):
    for j in range(len(hajok)):
        if hajok[i][2] > hajok[j][2]:
            hajok[i], hajok[j] = hajok[j], hajok[i]
print('> ' * 15, 'O', ' <'*15)

for i in range(3):
    print(hajok[i][0], hajok[i][1], hajok[i][2])

