forras = open('utca.txt', mode='r', encoding='utf-8')

elso_sor = forras.readline().strip().split(' ')
A_osszeg = int(elso_sor[0])
B_osszeg = int(elso_sor[1])
C_osszeg = int(elso_sor[2])

tulajdonos = []
utca = []
hazszam = []
adosav = []
alapterulet = []

for sor in forras:
    adat = sor.strip().split(' ')
    tulajdonos.append(int(adat[0]))
    utca.append(adat[1])
    hazszam.append(adat[2])
    adosav.append(adat[3])
    alapterulet.append(int(adat[4]))

forras.close()

print(f'2. feladat. A mintában {len(tulajdonos)} telek szerepel.')

print('3. feladat.', end=' ')
adoszam = int(input('Egy tulajdonos adószáma: '))
adoszam_db = 0
for i in range(len(tulajdonos)):
    if tulajdonos[i] == adoszam:
        print(f'{utca[i]} utca {hazszam[i]}')
        adoszam_db += 1
if adoszam_db == 0:
    print('Nem szerepel az adatállományban.')

def ado(adosav, alapterulet):
    if adosav == 'A':
        return A_osszeg * alapterulet
    elif adosav == 'B':
        return B_osszeg * alapterulet
    elif adosav == 'C':
        return C_osszeg * alapterulet

print('5. feladat')
telek_A = 0
telek_B = 0
telek_C = 0
ado_A = 0
ado_B = 0
ado_C = 0

for i in range(len(tulajdonos)):
    if adosav[i] == 'A':
        telek_A += 1
        ado_A += ado(adosav[i], alapterulet[i])
    elif adosav[i] == 'B':
        telek_B += 1
        ado_B += ado(adosav[i], alapterulet[i])
    elif adosav[i] == 'C':
        telek_C += 1
        ado_C += ado(adosav[i], alapterulet[i])

print(f'A sávba {telek_A} telek esik, az adó {ado_A} Ft.')
print(f'B sávba {telek_B} telek esik, az adó {ado_B} Ft.')
print(f'C sávba {telek_C} telek esik, az adó {ado_C} Ft.')

print('6. feladat. A több sávba sorolt utcák:')

utcak = []
for i in range(len(tulajdonos)-1):
    if utca[i] == utca[i+1] and adosav[i] != adosav[i+1]:
        utcak.append(utca[i])
print('\n'.join(set(utcak)))

kimenet = open('fizetendo.txt', mode='w', encoding='utf-8')


for i in range(len(tulajdonos)):
    fizetendo_ado = 0
    for j in range(len(tulajdonos)):
        if tulajdonos[i] == tulajdonos[j] and ado(adosav[j], alapterulet[j]) >= 10000:
            fizetendo_ado += ado(adosav[j], alapterulet[j])
    print(f'{tulajdonos[i]} {fizetendo_ado}', file=kimenet)