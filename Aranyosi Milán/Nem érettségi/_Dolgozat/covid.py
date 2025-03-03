forras = open('covid.txt')

adott_nap = []
napi_fertozottek = []
napi_halalok = []


for sor in forras:
    adat = sor.strip().split(';')
    adott_nap.append(adat[0])
    napi_fertozottek.append(int(adat[1]))
    napi_halalok.append(adat[2])

print(f'1.feladat \nAz állomány {len(napi_halalok)} nap adatait tartalmazza.')

osszeshalal = 0
osszesfertozott = 0
for i in range(len(napi_halalok)):
    osszeshalal += int(napi_halalok[i])
    osszesfertozott += int(napi_fertozottek[i])
print(f'2. feladat\nA két év alatt összesen {osszesfertozott:,} fertőzöttet és {osszeshalal:,} halottat regisztráltak.')

s100ezeralattinapok = 0
for i in range(len(napi_fertozottek)):
    if int(napi_fertozottek[i]) < 100000:
        s100ezeralattinapok += 1
print(f'3. feladat\nA fertőzöttek száma {s100ezeralattinapok} napon volt 100e fő alatt.')

legtobbenhaltakmeg = int(napi_halalok[0])
legtobbenhaltakmeg_id = adott_nap[0]
azonanapon_fertozottek = napi_fertozottek[0]
for i in range(len(napi_halalok)):
    if int(napi_halalok[i]) > legtobbenhaltakmeg:
        legtobbenhaltakmeg = int(napi_halalok[i])
        legtobbenhaltakmeg_id = adott_nap[i]
        azonanapon_fertozottek = int(napi_fertozottek[i])
print(f'4. feladat\nLegtöbben {legtobbenhaltakmeg_id} napon haltak meg:\n\t{legtobbenhaltakmeg:,} halott\n\t{azonanapon_fertozottek:,} fertőzött.')

legnagyobbaranyfertozottek = napi_fertozottek[1] // napi_fertozottek[0]
legnagyobbaranyfertozottek_id = napi_fertozottek[1]
for i in range(len(napi_fertozottek)-1):
    if napi_fertozottek[i+1] / napi_fertozottek[i] > legnagyobbaranyfertozottek:
        legnagyobbaranyfertozottek = napi_fertozottek[i + 1] / napi_fertozottek[i]
        legnagyobbaranyfertozottek_id = adott_nap[i+1]
print(f'5. feladat\nA legnagyobb arányú növekedés {legnagyobbaranyfertozottek_id} napon volt, amikor az előző nap {legnagyobbaranyfertozottek}-szorosa volt a fertőzöttek száma.')

tobbhalalozas = 0
kevesebbhalalozas = 0

for i in range(len(napi_halalok)-1):
    if napi_halalok[i+1] > napi_halalok[i]:
        tobbhalalozas += 1
    if napi_halalok[i+1] < napi_halalok[i]:
        kevesebbhalalozas += 1
print(f'6, feladat\nA napi halálozások száma {tobbhalalozas} napon nőtt és {kevesebbhalalozas} napon csökkent az előző naphoz képest.')

halaozasok_atlag = 0
halalozasok_osszes = 0
for i in range(len(napi_halalok)):
    halalozasok_osszes += int(napi_halalok[i])
halaozasok_atlag = halalozasok_osszes / len(napi_halalok)
print(halaozasok_atlag)