forras = open('beosztas.txt', mode='r', encoding='utf-8')

nev = []
tantargy = []
osztaly = []
heti_ora = []

i = 1
for sor in forras:
    adat = sor.strip()
    if i % 4 == 1:
        nev.append(adat)
    elif i % 4 == 2:
        tantargy.append(adat)
    elif i % 4 == 3:
        osztaly.append(adat)
    elif i % 4 == 0:
        heti_ora.append(int(adat))
    i += 1
forras.close()

print('2. feladat')
print(f'A fájlban {len(nev)} bejegyzés van.')

print('3. feladat')
print(f'Az iskolában a heti összóraszám: {sum(heti_ora)}')

tanar = input('Egy tanár neve=')
orak = 0
for i in range(len(nev)):
    if nev[i] == tanar:
        orak += heti_ora[i]
print(f'A tanár heti óraszáma: {orak}')

kiiras = open('of.txt', mode='w', encoding='utf-8')

for i in range(len(nev)):
    if tantargy[i] == 'osztalyfonoki':
        print(f'{osztaly[i]} - {nev[i]}', file=kiiras)

kiiras.close()

print('6.feladat')
be_osztaly = input('Osztály=')
be_tantargy = input('Tantárgy=')

szamlalo = 0
for i in range(len(nev)):
    if osztaly[i] == be_osztaly and tantargy[i] == be_tantargy:
        szamlalo += 1
if szamlalo == 1:
    print('Osztályszinten tanulják.')
else:
    print('Csoportbontásbna tanulják.')

print('7. feladat')
tanarok = []
for i in range(len(nev)):
    if nev[i] not in tanarok:
        tanarok.append(nev[i])
print(f'Az iskolában {len(tanarok)} tanár tanít.')