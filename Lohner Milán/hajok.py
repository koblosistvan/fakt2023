import math

forras = open('hajok.txt', mode='r', encoding='utf-8')

elsosor = forras.readline().strip().split(' ')

osszeskont = int(elsosor[0])

kontenerperhajo = int(elsosor[1])

celallomasok = []


for sor in forras:
    adat = sor.strip().split(' ')
    celallomasok.append(sor.strip())


városok = set(sorted(celallomasok))
hajok = []

for város in városok:
    konténer_varosba = celallomasok.count(város)
    hajokvarosba = math.ceil(konténer_varosba/kontenerperhajo)

    print(f'{város} {math.ceil(konténer_varosba/kontenerperhajo)}, {hajokvarosba-konténer_varosba}')
    hajok.append([város, hajokvarosba, hajokvarosba*kontenerperhajo-konténer_varosba])

for i in range(len(hajok)):
    for j in range(len(hajok)):
        if hajok[i][2] > hajok[j][2] or (hajok[i][2] == hajok[j][2] and hajok[i][1] > hajok[j][1]):
            hajok[i], hajok[j] = hajok[j], hajok[i]

#print(hajok)


for i in range(3):
    print(f'{hajok[i][0]}, {hajok[i][1]}, {hajok[i][2]}')