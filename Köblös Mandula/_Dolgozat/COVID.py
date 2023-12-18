forrás = open("covid.txt", mode="r", encoding="utf-8")

dátum = []
új_fertőzés = []
meghaltak = []

for sor in forrás:
    adat = sor.strip().split(";")
    dátum.append(adat[0])
    új_fertőzés.append(int(adat[1]))
    meghaltak.append(int(adat[2]))

forrás.close()

print("1.feladat")
print(f"Az állomány {len(dátum)} nap adatait tartalmazza.")

print("2.feladat")
fertőzött = 0
haláleset = 0
for i in range(len(dátum)):
    fertőzött += új_fertőzés[i]
    haláleset += meghaltak[i]
print(f"A két év alatt összesen {fertőzött:,} fertőzöttet és {haláleset:,} halottat regisztráltak.")

print("3.feladat")
alatt_100e = 0
for i in range(len(dátum)):
    if új_fertőzés[i] < 100000:
        alatt_100e += 1
print(f"A fertőzöttek száma {alatt_100e} napon volt 100e fő alatt.")

print("4.feladat")
legtöbb = 0
legtöbb_id = 0
for i in range(len(dátum)):
    if meghaltak[i] > legtöbb:
        legtöbb = meghaltak[i]
        legtöbb_id = i
print(f"A legtöbben {dátum[legtöbb_id]} napon haltak meg:\n\t{új_fertőzés[legtöbb_id]:,} fertőzött\n\t{meghaltak[legtöbb_id]:,} halott")

print("5.feladat")
legnagyobb_arány = 0
legnagyobb_arány_id = 0
for i in range(len(dátum)-1):
    if új_fertőzés[i+1]/új_fertőzés[i] > legnagyobb_arány:
        legnagyobb_arány = új_fertőzés[i+1]/új_fertőzés[i]
        legnagyobb_arány_id = i
print(f"A legnagyobb arányú növekedés {dátum[legnagyobb_arány_id+1]} napon volt, amikor az előző napi adat {legnagyobb_arány:.2f}-szorosa volt a fertőzöttek száma.")

print("6.feladat")
nőtt = 0
csökkent = 0
for i in range(len(dátum)-1):
    if meghaltak[i] > meghaltak[i+1]:
        csökkent += 1
    elif meghaltak[i] < meghaltak[i+1]:
        nőtt += 1
print(f"A halálozások száma {csökkent} napon csökkent és {nőtt} napon nőtt az előző naphoz képest.")

print("7.feladat")
összes_halál = 0
for i in range(len(dátum)):
    összes_halál += meghaltak[i]
print(f"A napi halálozások átlaga {összes_halál/len(meghaltak):,.1f} volt.")