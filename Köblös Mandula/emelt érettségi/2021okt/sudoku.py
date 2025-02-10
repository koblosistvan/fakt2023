fajl = input('Adja meg a bementi fájl nevét! ')
sorszam = int(input('Adja meg egy sor számát! '))
oszlop = int(input('Adja meg egy oszlop számát! '))
cella= [
    '111222333',
    '111222333',
    '111222333',
    '444555666',
    '444555666',
    '444555666',
    '777888999',
    '777888999',
    '777888999',
]
forras = open(fajl, mode='r', encoding='utf-8')

sorok = []
valtozas = []

for sor in forras:
    adat = list(sor.strip().split(' '))
    if len(adat) > 3:
        sorok.append(adat)
    else:
        valtozas.append(adat)

forras.close()


szam = sorok[sorszam - 1][oszlop - 1]
if szam != '0':
    print(f'Az adott helyen szerplő szám: {szam}')
else:
    print("Az adott helyet még nem töltötték ki.")

print(f'A hely a(z) {cella[sorszam-1][oszlop-1]} résztáblához tartozik.')

ures = 0
for i in range(len(sorok)):
    if sorok[i][i] == '0':
        ures += 1
print(ures)