forras = open('kozut.txt')

print('Adatok bolvasasa...')

elsosor = forras.readline().strip()
print(f'A fajl {elsosor}db sort tartalmaz')


darab = int(elsosor.split(' ')[0])
print(darab)

rendszamok = []

sebessegek = []

idok = []

for sor in forras:
    adat = sor.strip().split(' ')
    sebessegek.append(adat[3])
    rendszamok.append(adat[4])
    idok.append(' '.join(adat[:-2]))
    print(f'Időpont: {":".join(adat[:-2])}')

forras.close()

