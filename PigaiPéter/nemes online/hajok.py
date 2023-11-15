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

for varos in varosok:
    andor = allomasok.count(varos)
    print(f'{varos} {math.ceil(andor / hajocap)} {andor % hajocap}')
