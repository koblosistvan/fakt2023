forras = open('szallit.txt', mode='r', encoding='utf-8')

elso_sor = forras.readline().split(' ')
szalag_hossz = int(elso_sor[0])
idotartam = int(elso_sor[1])

idoegyseg = []
felkerul = []
lekerul = []
tomeg = []

for sor in forras:
    adat = sor.strip().split(' ')
    idoegyseg.append(int(adat[0]))
    felkerul.append(int(adat[1]))
    lekerul.append(int(adat[2]))
    tomeg.append(int(adat[3]))


print('2.feladat')
sorszam = int(input('Adja meg, melyik adatsorra kíváncsi! '))
print(f'Honnan: {felkerul[sorszam-1]} Hova: {lekerul[sorszam-1]}')

def tav(szalaghossz, indulashelye, erkezeshelye):
    if indulashelye > erkezeshelye:
        hossz = szalaghossz-indulashelye+erkezeshelye
    else:
        hossz = erkezeshelye-indulashelye
    return hossz


print('4.feladat')
legnagyobb_tav = tav(szalag_hossz, felkerul[0], lekerul[0])
for i in range(len(idoegyseg)):
    if tav(szalag_hossz, felkerul[i], lekerul[i]) > legnagyobb_tav:
        legnagyobb_tav = tav(szalag_hossz, felkerul[i], lekerul[i])
print(f'A legnagyobb távolság: {legnagyobb_tav}')
print('A maximális távolságú szállítások sorszáma:', end=' ')
for i in range(len(idoegyseg)):
    if tav(szalag_hossz, felkerul[i], lekerul[i]) == legnagyobb_tav:
        print(i+1, end=' ')

print(f'\n 5.feladat')
athaladt_ossztomeg = 0
for i in range(len(idoegyseg)):
    if felkerul[i] > lekerul[i] and felkerul[i] != 0 and lekerul[i] != 0:
        athaladt_ossztomeg += tomeg[i]
print(f'A kezdőpont előtt elhaladó rekeszek össztömege: {athaladt_ossztomeg}')

print('6.feladat')
celbaeres = []
for i in range(len(idoegyseg)):
    celbaeres.append((idoegyseg[i]+tav(szalag_hossz, felkerul[i], lekerul[i]))*idotartam)

print(f'A szállított rekeszek halmaza: ', end=' ')
bekert_idopont = int(input('Adja meg a kívánt időpontot! '))
volt_csomag_ekkor = False
for i in range(len(idoegyseg)):
    if idoegyseg[i] <= bekert_idopont < celbaeres[i]:
        print(i+1, end=' ')
        volt_csomag_ekkor = True
if not volt_csomag_ekkor:
    print('üres')

print('\n')

kiiras = open('tomeg.txt', mode='w', encoding='utf-8')

helyek = sorted(set(felkerul.copy()))
print(helyek)

for hely in helyek:
    ossztomeg = 0
    for j in range(len(idoegyseg)):
        if felkerul[j] == hely:
            ossztomeg += tomeg[j]
    print(f'{hely} {ossztomeg}', file=kiiras)

kiiras.close()