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
print(f'A tó felszíne {felszin} m2')