# 1
forras = open('szallit.txt', 'r', encoding='utf-8')
seged = forras.readline().strip().split(' ')
szalag_hossz = int(seged[0])
egys_elmozdulas = int(seged[1])
mikor = []
honnan = []
hova = []
suly = []
for i in forras:
    sor = i.strip().split()
    mikor.append(int(sor[0]))
    honnan.append(int(sor[1]))
    hova.append(int(sor[2]))
    suly.append(int(sor[3]))
forras.close()

# 2
adatsor = int(input('2. feladat\nAdja meg, melyik adatsorra kíváncsi! '))
print(f'Honnan: {honnan[adatsor-1]} Hova: {hova[adatsor-1]}')

# 3
def tav(szalaghossz, indulashelye, erkezeshelye):
    szallitas_tavolsaga = 0
    if indulashelye > erkezeshelye:
        szallitas_tavolsaga = szalaghossz-indulashelye+erkezeshelye
    elif indulashelye < erkezeshelye:
        szallitas_tavolsaga = erkezeshelye-indulashelye
    return szallitas_tavolsaga


# 4
maxtav = 0
for i in range(len(honnan)):
    seged = tav(szalag_hossz, honnan[i], hova[i])
    if seged > maxtav:
        maxtav = seged
maxtavok = []
for i in range(len(honnan)):
    if tav(szalag_hossz, honnan[i], hova[i]) == maxtav:
        maxtavok.append(str(i+1))
print(f'4. feladat\n'
      f'A legnagyobb távolság: {maxtav}\n'
      f'A maximális távolságú szállítások sorszáma: {" ".join(maxtavok)}')
# 5
ossztomeg = 0
for i in range(len(suly)):
    if honnan[i] != 0 and hova[i] != 0 and honnan[i] > hova[i]:
        ossztomeg += suly[i]
print(f'5. feladat'
      f'A kezdőpont előtt elhaladó rekeszek össztömege: {ossztomeg}')

# 6
bekert_idopont = int(input('6. feladat\nAdja meg a kívánt időpontot! '))
szallitott_index = []
for i in range(len(mikor)):
    if mikor[i] <= bekert_idopont < mikor[i]+tav(szalag_hossz, honnan[i], hova[i])*egys_elmozdulas:
        szallitott_index.append(str(i+1))
if szallitott_index:
    print(f'A szállított rekeszek halmaza: {" ".join(szallitott_index)}')
else:
    print('üres')

# 7
tomeg = open('tomeg.txt', 'w', encoding='utf-8')
kimenet = []
for i in range(len(mikor)):
    osszelszallitott = 0
    for k in range(len(mikor)):
        if mikor[i] == mikor[k]:
            osszelszallitott += suly[k]
    if [mikor[i], osszelszallitott] not in kimenet:
        kimenet.append([str(mikor[i]), str(osszelszallitott)])
for i in kimenet:
    print(" ".join(i), file=tomeg)
tomeg.close()
"""2. feladat
Adja meg, melyik adatsorra kíváncsi! 3
Honnan: 135 Hova: 54
4. feladat
A legnagyobb távolság: 195
A maximális távolságú szállítások sorszáma: 31 33
5. feladat
A kezdőpont előtt elhaladó rekeszek össztömege: 957
6. feladat
Adja meg a kívánt időpontot! 300
A szállított rekeszek halmaza: 1 2 3 6 7 10 11 """