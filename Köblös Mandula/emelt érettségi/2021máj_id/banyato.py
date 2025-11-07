forras = open('melyseg.txt', mode='r', encoding = 'utf-8')

sorok = int(forras.readline())
oszlopok = int(forras.readline())

melysegek = []
for sor in forras:
    adat = sor.strip().split(' ')
    for i in range(len(adat)):
        adat[i] = int(adat[i])
    melysegek.append(adat)

forras.close()

print('2.feladat')
sorszam = int(input('A mérés sorának azonosítója='))-1
oszlopszam = int(input('A mérés oszlopának azonosítója='))-1
print(f'A mért mélység az adott helyen {melysegek[sorszam][oszlopszam]} dm')

print('\n3.feladat')
felszin = 0
osszes = 0
for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if melysegek[i][j] > 0:
            felszin += 1
            osszes += melysegek[i][j]
print(f'A tó felszíne {felszin} m2, átlagos mélysége: {osszes/felszin/10 :0.2f} m')

print('\n4.feladat')
legnagyobb_melyseg = melysegek[0][0]
for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if melysegek[i][j] > legnagyobb_melyseg:
            legnagyobb_melyseg = melysegek[i][j]
print(f'A tó legnagyobb mélysége {legnagyobb_melyseg} dm')

print('A legmélyebb helyek sor-oszlop koordinátái:')
for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if melysegek[i][j] == legnagyobb_melyseg:
            print(f'({i+1}; {j+1})', end='\t')

print('\n\n5.feladat')
kerulet = 0
for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if melysegek[i][j] > 0:
            if melysegek[i-1][j] == 0:
                kerulet += 1
            if melysegek[i+1][j] == 0:
                kerulet += 1
            if melysegek[i][j-1] == 0:
                kerulet += 1
            if melysegek[i][j+1] == 0:
                kerulet += 1
print(f'A tó partvonala {kerulet} m hosszú')

print('\n6.feladat')

kiiras = open('diagram.txt', mode='w', encoding='utf-8')

oszlop_azonosito = int(input('A vizsgált szelvény oszlopának azonosítója='))-1

for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if j == oszlop_azonosito:
            print(f'{i+1:02}{melysegek[i][j]*"*"}', file=kiiras)
