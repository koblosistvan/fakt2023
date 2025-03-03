forras = open('szallit.txt', mode='r', encoding='utf-8')

elsosor = forras.readline().split(' ')

maxtav = int(elsosor[0])
elmozdulashoz_ido = int(elsosor[1])

mikor_tettek = []
honnan = []
hova = []
tomeg = []



for sor in forras:
    adat = sor.strip().split(' ')
    mikor_tettek.append(int(adat[0]))
    honnan.append(int(adat[1]))
    hova.append(int(adat[2]))
    tomeg.append(int(adat[3]))

forras.close()


print('2. feladat')
melyiksorszam = int(input('Adja meg, melyik adatsorra kíváncsi!'))
print(f'Honnan: {honnan[melyiksorszam-1]} Hova: {hova[melyiksorszam-1]}')


def tav(szalaghossz, indulashelye, erkezeshelye):
    if indulashelye > erkezeshelye:
        return szalaghossz - indulashelye + erkezeshelye
    else:
        return erkezeshelye - indulashelye


print('4.feladat')
szallitasok = []
for i in range(len(honnan)):
    adott_tav = tav(maxtav, honnan[i], hova[i])
    szallitasok.append(adott_tav)

legnagyobbtav = max(szallitasok)
legnagyobbtav_indexek = ''

for i in range(len(szallitasok)):
    if szallitasok[i] == legnagyobbtav:
        legnagyobbtav_indexek += f' {i+1}'

print(f'A legnagyobb távolság: {legnagyobbtav}')
print(f'A maximális távolságú szállítások sorszáma:{legnagyobbtav_indexek}')


print('5. feladat')

osszestomeg = 0

for i in range(len(hova)):
    if honnan[i] > hova[i]:
        osszestomeg += tomeg[i]
print(f'A kezdőpont előtt elhaladó rekeszek össztömege: {osszestomeg}')


print('6. feladat')

szallitott_rekeszek = ''

bekert_idopont = int(input('Adja meg a kívánt időpontot!'))
for i in range(len(mikor_tettek)):
    if mikor_tettek[i] <= bekert_idopont <= mikor_tettek[i] + tav(maxtav, honnan[i], hova[i]) * elmozdulashoz_ido:
        szallitott_rekeszek += f' {i+1}'

if szallitott_rekeszek == '':
    szallitott_rekeszek += ' üres'

print(f'A szállított rekeszek halmaza:{szallitott_rekeszek}')


kimenet = open('tomeg.txt', mode='w', encoding='utf-8')

for i in range(len(honnan)):
    adotthelytomege = 0
    if i+1 in honnan:
        adotthelytomege = tomeg[honnan.index(i+1)]
    if adotthelytomege > 0:
        print(f'{i+1} {adotthelytomege}', file=kimenet)
kimenet.close()
