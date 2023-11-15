import math
forras = open('hajok.txt', 'r', encoding='utf-8')
varosok = []

elso_sor = forras.readline()
kontenerek_szama = int(elso_sor[0])
ferohely = int(elso_sor[1])
for i in forras:
    varosok.append(int(i.strip()))

varosok_halmaz = set(varosok)
for i in varosok:
    kontener_v = varosok.count(i)
    print(f'{i} {math.ceil(kontener_v/ferohely)} {kontener_v}')