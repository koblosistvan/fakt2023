szam = input('Kérem a TAJ-számot: ')

elso = 0
mas = 0
harm = 0
negy = 0
ot = 0
hat = 0
het = 0
nyolc = 0
kilenc = 0

for i in szam:
    elso = int(szam[0])
    mas = int(szam[1])
    harm = int(szam[2])
    negy = int(szam[3])
    ot = int(szam[4])
    hat = int(szam[5])
    het = int(szam[6])
    nyolc = int(szam[7])
    kilenc = int(szam[8])

print(f'Az ellenőrzőszámjegy: {kilenc}')

osszeg = 3 * elso + 3 * harm + 3 * ot + 3 * het + 7 * mas + 7 * negy + 7 * hat + 7 * nyolc

print(f'A szorzatok összege: {osszeg}')

if osszeg % 10 == kilenc:
    print(f'Helyes a szám!')
else:
    print('Hibás a szám!')
