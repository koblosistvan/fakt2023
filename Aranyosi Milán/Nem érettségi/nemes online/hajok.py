import math

forras = open('hajok.txt', mode='r', encoding='utf-8')

elso_sor = forras.readline().strip().split()
hajon_max = int(elso_sor[1])
kontenerek = int(elso_sor[0])
celallomasok = []

for sor in forras:
    celallomasok.append(sor.strip())

forras.close()

varosok = set(celallomasok)

hajok = []

#print(varosok)

for varos in varosok:
    kontener_varosba = celallomasok.count(varos)
    hajo_varosba = math.ceil(kontener_varosba/hajon_max)
    #print(f'{varos} {hajo_varosba}  {hajo_varosba * hajon_max - kontener_varosba}')
    hajok.append([varos, hajo_varosba, hajo_varosba * hajon_max - kontener_varosba])

#print(hajok)

for i in range(len(hajok)):
    for j in range(len(hajok)):
        if hajok[i][2] > hajok[j][2] or hajok[i][2] == hajok[j][2] and hajok[i][1] > hajok[j][1]:
            hajok[i], hajok[j] = hajok[j], hajok[i]

#print(hajok)

for i in range(3):
    print(f'{hajok[i][0]}, {hajok[i][1]}, {hajok[i][2]} ')
