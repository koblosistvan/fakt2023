forras = open('fogado.txt', mode='r', encoding='utf-8')

nev = []
idopont = []
foglalas = []

for sor in forras:
    adat = sor.strip().split(' ')
    nev.append(f'{adat[0]} {adat[1]}')
    idopont.append(adat[2])
    foglalas.append(adat[3])

forras.close()

print('2. feladat')
print(f'Foglalások száma: {len(nev)}')

print('\n3. feladat')
tanar = input('Adjon meg egy nevet: ')
foglalasok = 0
for i in range(len(nev)):
    if nev[i] == tanar:
        foglalasok += 1

if foglalasok == 0:
    print('A megadott néven nincs időpontfoglalás.')
else:
    print(f'{tanar} néven {foglalasok} időpontfoglalás van.')

print('\n4. feladat')
ido = input('Adjon meg egy érvényes időpontot (pl. 17:10): ')
nevek = []
for i in range(len(nev)):
    if ido == idopont[i]:
        nevek.append(nev[i])
print('\n'.join(sorted(nevek)))

kiiras = open(f'{ido[0]}{ido[1]}{ido[3]}{ido[4]}.txt', mode='w', encoding='utf-8')

print('\n'.join(sorted(nevek)), file=kiiras)

kiiras.close()

print('\n5. feladat')

for i in range(len(nev)):
    if foglalas[i] == min(foglalas):
        print(f'Tanár neve: {nev[i]}')
        print(f'Foglalási időpont: {idopont[i]}')
        print(f'Foglalás ideje: {foglalas[i]}')

print('\n6. feladat')
idopontok = ['16:00', '16:10', '16:20', '16:30', '16:40', '16:50', '17:00', '17:10', '17:20', '17:30', '17:40', '17:50']
barna = []

for i in range(len(nev)):
    if nev[i] == 'Barna Eszter':
        idopontok.remove(idopont[i])
        barna.append(idopont[i])

print('\n'.join(idopontok))

utolso = max(barna)
if utolso[3] == '5':
    tavozhat = str(int(utolso[:2])+1)+':00'
else:
    tavozhat = utolso[:3]+str(int(utolso[3:])+10)

print(f'Barna Eszter legkorábban távozhat: {tavozhat}')