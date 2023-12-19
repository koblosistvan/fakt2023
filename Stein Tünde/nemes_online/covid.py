forras = open('covid.txt', 'r', encoding='utf-8')
datumok = []
fertozottek = []
halalozasok = []
for i in forras:
    adat = i.strip().split(';')
    datumok.append(adat[0])
    fertozottek.append(int(adat[1]))
    halalozasok.append(int(adat[2]))
forras.close()
print(f'1. feladat:\n{len(datumok)} nap adatai.\n')

ossz_fertozott = 0
ossz_halaleset = 0
for i in range(len(fertozottek)):
    ossz_fertozott += fertozottek[i]
    ossz_halaleset += halalozasok[i]
print(f'2. feladat:\n{ossz_fertozott:,} regisztrált fertőzött, és {ossz_halaleset:,} haláleset volt 2 év alatt.\n')

_100ealatti = 0
for i in fertozottek:
    if i < 100000:
        _100ealatti += 1
print(f'3. feladat:\nA fertőzöttek száma {_100ealatti} napon volt 100e alatt.\n')

legtobb_halal = 0
index_4 = 0
for i in range(len(halalozasok)):
    if halalozasok[i] > legtobb_halal:
        legtobb_halal = halalozasok[i]
        index_4 = i
print('4. feladat:')
print(f'A legtöbben {datumok[index_4]} napon haltak meg:\n\t{fertozottek[index_4]:,} fertőzött\n\t{halalozasok[index_4]:,} halott\n')

legmagasabb_arany = 0
for i in range(len(fertozottek)-1):
    if fertozottek[i+1]/fertozottek[i] > legmagasabb_arany:
        legmagasabb_arany = fertozottek[i+1]/fertozottek[i]
        index_5 = i+1
if bool(legmagasabb_arany):
    print(f'5. feladat\nA legnagyobb arányú növekedés {datumok[index_5]} napon volt, amikor az előző napi adat {legmagasabb_arany}-szorosa volt a fertőzöttek száma.\n')

csokkent = 0
nott = 0
for i in range(len(halalozasok)-1):
    if halalozasok[i] > halalozasok[i+1]:
        csokkent += 1
    elif halalozasok[i] < halalozasok[i+1]:
        nott += 1
print(f'6. feladat:\n{csokkent} napon csökkent, és {nott} napon nőtt a halálozások száma az előző naphoz képest.\n')

print(f'7. feladat:\nA napi halálozások átlagos száma {ossz_halaleset/len(halalozasok):,} volt.')
