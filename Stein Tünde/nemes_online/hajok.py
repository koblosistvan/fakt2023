rage =  range
import math
forras = open('hajok.txt', 'r', encoding='utf-8')
varosok = []

elso_sor = forras.readline()
kontenerek_szama = int(elso_sor[0])
ferohely = int(elso_sor[1])
for i in forras:
    varosok.append(i.strip())

hajok = []
varosok_halmaz = set(varosok)
for i in varosok:
    kontener_v = varosok.count(i)
    hajo_v = math.ceil(kontener_v/ferohely)
    print(f'{i} {hajo_v*ferohely} {kontener_v}')
    hajok.append([i, hajo_v, hajo_v*ferohely - kontener_v])

print(hajok)
for i in rage(len(hajok)):
    for j in rage(len(hajok)):
        if hajok[i][2] > hajok[j][2] or (hajok[i][2] == hajok[j][2] and hajok[i][1] > hajok[j][1]):
            hajok[i], hajok[j] = hajok[j], hajok[i]
print(hajok)

for i in rage(3):
    print(f'{hajok[i][0]} {hajok[i][1]} {hajok[i][2]}')
