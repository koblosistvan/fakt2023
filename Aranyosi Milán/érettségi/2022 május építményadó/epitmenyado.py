forras = open('utca.txt', mode='r', encoding='utf-8')

A, B, C = forras.readline().split()

tulajok = []
utcanev = []
hazszamok = []
adosavok = []
alapterulet = []

for sor in forras:
    adat = sor.strip().split()
    tulajok.append(int(adat[0]))
    utcanev.append(adat[1])
    hazszamok.append(adat[2])
    adosavok.append(adat[3])
    alapterulet.append(int(adat[4]))

forras.close()

print(tulajok, utcanev, hazszamok, adosavok, alapterulet)
print(A,B,C)

print(f'2. feladat. A mintában {len(hazszamok)} telek szerepel.')

adott_adoszam = int(input(f'3. feladat. Egy tulajdonos adószáma: '))

szaml = 0
for i in range(len(tulajok)):
    if adott_adoszam == tulajok[i]:
        print(f'{utcanev[i]} utca {hazszamok[i]}')
        szaml += 1
if szaml == 0:
    print('Nem szerepel az adatállományban.')

def ado(adosav, alapterulet):
    if adosav == "A":
        osszeg_ado = alapterulet * int(A)
    elif adosav == "B":
        osszeg_ado = alapterulet * int(B)
    else:
        osszeg_ado = alapterulet * int(C)
    return osszeg_ado if osszeg_ado >= 10000 else 0


a_szaml = 0
b_szaml = 0
c_szaml= 0
a_osszeg = 0
b_osszeg = 0
c_osszeg = 0

for i in range(len(adosavok)):
    adott_ado = ado(adosavok[i], alapterulet[i])
    if adosavok[i] == "A":
        a_szaml += 1
        a_osszeg += adott_ado
    elif adosavok[i] == "B":
        b_szaml += 1
        b_osszeg += adott_ado
    else:
        c_szaml += 1
        c_osszeg += adott_ado

print('5. feladat')
print(f'A sávba {a_szaml} telek esik, az adó {a_osszeg} Ft.')
print(f'B sávba {b_szaml} telek esik, az adó {b_osszeg} Ft.')
print(f'C sávba {c_szaml} telek esik, az adó {c_osszeg} Ft.')

print('6. feladat. A több sávba sorolt utcák:')

'''

Besztercei
Gyurgyalag
Icce
Kurta
Rezeda
Szepesi'''