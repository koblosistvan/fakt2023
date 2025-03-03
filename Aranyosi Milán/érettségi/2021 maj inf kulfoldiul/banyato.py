forras = open('melyseg.txt', mode='r', encoding='utf-8')

max_sorok = int(forras.readline())
max_oszlok = int(forras.readline())

melysegek = []
for sor in forras:
    adat = sor.strip().split(' ')
    for i in range(len(adat)):
        adat[i] = int(adat[i])
    melysegek.append(adat)

print('2. feladat')

adott_sor = int(input('A mérés sorának azonosítója=')) - 1
adott_oszlop = int(input('A mérés oszlopának azonosítója=')) - 1
print(f'A mért mélység az adott helyen {melysegek[adott_sor][adott_oszlop]} dm')

print('\n3. feladat')
osszes_melysegek = 0
felszin = 0
for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if melysegek[i][j] != 0:
            felszin += 1
            osszes_melysegek += melysegek[i][j]

print(f'A tó felszíne: {felszin} m2, átlagos mélysége: {osszes_melysegek/felszin/10:0.2f} m')

print(f'\n4. feladat')

legnagyobb_melysegek = melysegek[0][0]

for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if melysegek[i][j] > legnagyobb_melysegek:
            legnagyobb_melysegek = melysegek[i][j]

print(f'A tó legnagyobb mélysége: {legnagyobb_melysegek} dm')
print('A legmélyebb helyek sor-oszlop koordinátái:')

for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if melysegek[i][j] == legnagyobb_melysegek:
            print(f'({i+1};{j+1})', end='\t')


print('\n\n5. feladat')

kerulet = 0

for i in range(len(melysegek)):
    for j in range(len(melysegek[i])):
        if melysegek[i][j] != 0:
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
vizsgalt_oszlop = int(input('A vizsgált szelvény oszlopának azonosítója=')) - 1

kimenet = open('diagram.txt', mode='w', encoding='utf-8')

for i in range(len(melysegek[i])):
    print(f'{i+1:02}{melysegek[i][vizsgalt_oszlop] * "*"}', file=kimenet)


kimenet.close()