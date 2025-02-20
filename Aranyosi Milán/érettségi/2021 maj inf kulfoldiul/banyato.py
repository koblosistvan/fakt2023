forras = open('melyseg.txt', mode='r', encoding='utf-8')

max_sorok = int(forras.readline())
max_oszlok = int(forras.readline())

melysegek = []
for sor in forras:
    adat = sor.strip().split(' ')
    for i in range(len(adat)):
        adat[i] = int(adat[i])
    melysegek.append(adat)
print(melysegek)

print('2. feladat')

adott_sor = int(input('A mérés sorának azonosítója=')) - 1
adott_oszlop = int(input('A mérés oszlopának azonosítója=')) - 1
print(f'A mért mélység az adott helyen {melysegek[adott_sor][adott_oszlop]} dm')

print('\n3. feladat')
seged_melysegek = 0
for i in range(len(melysegek)):
    pass



print(f'A tó felszíne: {} m2, átlagos mélysége: {} m')

'''


4. feladat
A tó legnagyobb mélysége: 98 dm
A legmélyebb helyek sor-oszlop koordinátái:
(14; 20) (26; 11) (32; 16)
5. feladat
A tó partvonala 270 m hosszú
6. feladat
A vizsgált szelvény oszlopának azonosítója=6 
'''