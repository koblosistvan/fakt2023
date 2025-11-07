PAROS = 0
PARATLAN = 1

forras = open('kerites.txt', mode='r', encoding='utf-8')

oldal = []
szelesseg = []
kerites = []

for sor in forras:
    adat = sor.strip().split(' ')
    oldal.append(int(adat[0]))
    szelesseg.append(int(adat[1]))
    kerites.append(adat[2])

hazszam = []
haz_ps = 0
haz_pt = -1

for i in range(len(oldal)):
    if oldal[i] == PAROS:
        hazszam.append(haz_ps+2)
        haz_ps += 2
    elif oldal[i] == PARATLAN:
        hazszam.append(haz_pt+2)
        haz_pt += 2

forras.close()

print('2. feladat')
print(f'Az eladott telkek száma: {len(oldal)}')

print('\n3. feladat')
if oldal[-1] == 0:
    print(f'A páros oldalon adták el az utolsó telket.')
else:
    print(f'A páratlan oldalon adták el az utolsó telket.')

utolso_oldal = oldal[-1]
hazszam_3 = 0

for i in range(len(oldal)):
    if oldal[i] == utolso_oldal:
        hazszam_3 += 2

if oldal[-1] == PAROS:
    print(f'Az utolsó telek házszáma: {hazszam_3}')
else:
    print(f'Az utolsó telek házszáma: {hazszam_3-1}')

print('\n4. feladat')
szinek = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ugyanolyan_id = 0
ugyanolyan_oldal = 0
for i in range(len(oldal)-1):
    if oldal[i] == oldal[i+1] and kerites[i] in szinek and kerites[i] == kerites[i+1]:
        print(f'A szomszédossal egyezik a kerítés színe: {hazszam[i]}')
        break

print('\n5. feladat')
szam = int(input('Adjon meg egy házszámot! '))
haz_id = 0
for i in range(len(oldal)):
    if hazszam[i] == szam:
        print(f'A kerítés színe/állapota: {kerites[i]}')
        haz_id = i

valasztek = szinek.copy()
valasztek.remove(kerites[haz_id])

for i in range(len(oldal)):
    if hazszam[i] == szam-2:
        valasztek.remove(kerites[i])
    elif hazszam[i] == szam+2:
        valasztek.remove(kerites[i])

print(f'Egy lehetséges festési szín: {valasztek[0]}')

kiiras = open('utcakep.txt', mode='w', encoding='utf-8')

for i in range(len(oldal)):
    if oldal[i] == PARATLAN:
        print(f'{kerites[i]*szelesseg[i]}', end='', file=kiiras)
print('', file=kiiras)
for i in range(len(oldal)):
    if oldal[i] == PARATLAN:
        print(f'{hazszam[i]}{" " * (szelesseg[i]-len(str(hazszam[i])))}', end='', file=kiiras)

kiiras.close()