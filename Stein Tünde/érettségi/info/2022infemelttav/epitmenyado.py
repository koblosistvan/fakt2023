# 1
forras = open('utca.txt', 'r', encoding='utf-8')
elso_sor = forras.readline().strip().split(' ')
a_sav = int(elso_sor[0])
b_sav = int(elso_sor[1])
c_sav = int(elso_sor[2])
adoszam = []
utcanev = []
hazszam = []
sav = []
terulet = []
for i in forras:
    sor = i.strip().split(' ')
    adoszam.append(int(sor[0]))
    utcanev.append(sor[1])
    hazszam.append(sor[2])
    sav.append(sor[3])
    terulet.append(int(sor[4]))
forras.close()

# 2
print(f'2. feladat. A mintában {len(adoszam)} telek szerepel.')

# 3
bekert = int(input('3. feladat. Egy tulajdonos adószáma: '))
vanbekert = False
for i in range(len(adoszam)):
    if adoszam[i] == bekert:
        print(f'{utcanev[i]} utca {hazszam[i]}')
        vanbekert = True
if not vanbekert:
    print('Nem szerepel az állományban.')

# 4
def ado(adosav, alapterulet):
    if adosav == 'A':
        vissza = a_sav * alapterulet
    elif adosav == 'B':
        vissza = b_sav * alapterulet
    elif adosav == 'C':
        vissza = c_sav * alapterulet
    if vissza >= 10000:
        return vissza
    else:
        return 0


# 5
a_adok = []
b_adok = []
c_adok = []
for i in range(len(adoszam)):
    if sav[i] == 'A':
        a_adok.append(ado('A', terulet[i]))
    elif sav[i] == 'B':
        b_adok.append(ado('B', terulet[i]))
    elif sav[i] == 'C':
        c_adok.append(ado('C', terulet[i]))
print(f'5. feladat\n'
      f'A sávba {len(a_adok)} telek esik, az adó {sum(a_adok)} Ft.\n'
      f'B sávba {len(b_adok)} telek esik, az adó {sum(b_adok)} Ft.\n'
      f'C sávba {len(c_adok)} telek esik, az adó {sum(c_adok)} Ft.')

# 6
utcanevek = []
for i in range(len(adoszam)):
    for k in range(i+1, len(adoszam)):
        if utcanev[i] == utcanev[k]:
            if sav[i] != sav[k] and utcanev[i] not in utcanevek:
                utcanevek.append(utcanev[i])
print('6. feladat. A több sávba sorolt utcák:')
for i in utcanevek:
    print(i)

# 7
kimenet = open('fizetendo.txt', 'w', encoding='utf-8')
for i in range(len(adoszam)):
    print(f'{adoszam[i]} {ado(sav[i], terulet[i])}', file=kimenet)
kimenet.close()

"""2. feladat. A mintában 543 telek szerepel.
3. feladat. Egy tulajdonos adószáma: 68396
Harmat utca 22
Szepesi utca 17
5. feladat
A sávba 165 telek esik, az adó 20805600 Ft.
B sávba 144 telek esik, az adó 13107000 Ft.
C sávba 234 telek esik, az adó 3479600 Ft.
6. feladat. A több sávba sorolt utcák:
Besztercei
Gyurgyalag
Icce
Kurta
Rezeda
Szepesi"""