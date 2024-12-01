class Adatsor:
    evmax = 0
    evmin = 9999
    kapmax = 0
    kaporszag = ""
    gdpmin = 10**999
    gdpminorszag = ""
    kap2000 = 0
    kap2014 = 0
    lakossag2000 = 0
    lakossag2014 = 0
    felh2000 = 0
    felh2014 = 0
    orszagok = []
    def __init__(self,adatsor) -> None:
        self.eredeti = adatsor
        adatsor = adatsor.split(',')
        self.kód  = adatsor[0]
        self.ország = adatsor[1]
        self.régió = adatsor[2]
        self.év = int(adatsor[3])
        self.felhasználá = float(adatsor[4])
        self.kapacitá = float(adatsor[5])
        self.lakosság = int(adatsor[6])
        self.gdp = None if adatsor[7] == "None" else float(adatsor[7])
        if Adatsor.evmax < self.év:
            Adatsor.evmax = self.év
        if Adatsor.evmin > self.év:
            Adatsor.evmin = self.év
        if Adatsor.kapmax < self.kapacitá:
            Adatsor.kaporszag = self.ország
            Adatsor.kapmax = self.kapacitá
        if self.gdp != None and Adatsor.gdpmin > self.gdp:
            Adatsor.gdpmin = self.gdp
            Adatsor.gdpminorszag = self.ország
        if self.év == 2000:
            Adatsor.kap2000 += self.kapacitá
            Adatsor.felh2000 += self.felhasználá
            Adatsor.lakossag2000 += self.lakosság
        if self.év == 2014:
            Adatsor.kap2014 += self.kapacitá
            Adatsor.felh2014 += self.felhasználá
            Adatsor.lakossag2014 += self.lakosság
        if self.ország not in Adatsor.orszagok:
            Adatsor.orszagok.append(self.ország)
    def __str__(self) -> str:
        return self.eredeti
adatok = []
with open("PigaiPéter\\okolabynom\\NFA light.csv", mode="r", encoding="utf-8") as forras:
    forras.readline()
    for sor in forras:
        adatok.append(Adatsor(sor.strip()))

print(f"{len(adatok)} sort tartalmaz")

print(f"{len([i for i in adatok if i.év == 2014])} országnak van 2014-es adata")

print(f"{Adatsor.evmin}-{Adatsor.evmax} közötti mérések")

print(f"A legnagyobb kapacitású ország {Adatsor.kaporszag} és {Adatsor.kapmax} a kapacitása")

print(f"Legkisebb gdp-vel rendelkező ország: {Adatsor.gdpminorszag}, {Adatsor.gdpmin}")

print(f"2000-ben: {Adatsor.kap2000} volt a kapacitás, {Adatsor.felh2000} volt a felhasználás\n2014-ben: {Adatsor.kap2014} volt a kapacitás, {Adatsor.felh2014} volt a felhasználás")

if Adatsor.felh2000/Adatsor.kap2000 > Adatsor.felh2014/Adatsor.kap2014:
    print("A két érték aránya csökkent")
elif Adatsor.felh2000/Adatsor.kap2000 < Adatsor.felh2014/Adatsor.kap2014:
    print("A két érték aránya nőtt")
else:
    print("A két érték aránya nem változott")

print(f"2010-ben egy főre jutó átlagos felhasználás: {Adatsor.felh2000/Adatsor.lakossag2000}, 2014-ben egy főre jutó átlagos felhasználás: {Adatsor.felh2014/Adatsor.lakossag2014}")
if Adatsor.felh2000/Adatsor.lakossag2000 > Adatsor.felh2014/Adatsor.lakossag2014:
    print(f"{abs((Adatsor.felh2014/Adatsor.lakossag2014) / (Adatsor.felh2000/Adatsor.lakossag2000) * 100 - 100)}% csökkent")
elif Adatsor.felh2000/Adatsor.lakossag2000 < Adatsor.felh2014/Adatsor.lakossag2014:
    print(f"{(Adatsor.felh2014/Adatsor.lakossag2014) / (Adatsor.felh2000/Adatsor.lakossag2000) * 100 - 100}% nőtt")
else:
    print("Az egy főre jutó felhasználás aránya nem változott")

print(f"2010-ben egy főre jutó átlagos kapacitás: {Adatsor.kap2000/Adatsor.lakossag2000}, 2014-ben: {Adatsor.kap2014/Adatsor.lakossag2014}")
if Adatsor.kap2000/Adatsor.lakossag2000 > Adatsor.kap2014/Adatsor.lakossag2014:
    print(f"{abs((Adatsor.kap2014/Adatsor.lakossag2014) / (Adatsor.kap2000/Adatsor.lakossag2000) * 100 - 100)}% csökkent")
elif Adatsor.felh2000/Adatsor.lakossag2000 < Adatsor.felh2014/Adatsor.lakossag2014:
    print(f"{(Adatsor.kap2014/Adatsor.lakossag2014) / (Adatsor.kap2000/Adatsor.lakossag2000) * 100 - 100}% nőtt")
else:
    print("Az egy főre jutó kapacitás aránya nem változott")

határ = int(input("Adjon meg egy határt:"))
print(f"Az alábbi országokban volt az egy főre jutó felhasználás {határ} hektár fölött")
for i in range(len(adatok)):
    if adatok[i].felhasználá / adatok[i].lakosság > határ:
        print(f"{adatok[i].ország} - {adatok[i].év}: {adatok[i].felhasználá / adatok[i].lakosság} hektár")

print(f"Az adatok {len(Adatsor.orszagok)} ország adatait tartalmazzák.")

maxfelhaszn = 0
maxfelhorszag = ""
maxfelhev = 0
maxfelhasznelőző = 0
for i in range(len(adatok) - 1):
    if adatok[i].ország == adatok[i+1].ország and adatok[i+1].felhasználá - adatok[i].felhasználá > maxfelhaszn:
        maxfelhasznelőző = maxfelhaszn
        maxfelhaszn = adatok[i + 1].felhasználá - adatok[i].felhasználá
        maxfelhev = adatok[i + 1].év
        maxfelhorszag = adatok[i + 1].ország
print(f"A legnagyobb növekedés a felhasználás értékében {maxfelhorszag}-ban {maxfelhev}-ben történt: \n{maxfelhasznelőző} => {maxfelhaszn}.")

for i in range(len(adatok) - 1):
    if adatok[i].ország == adatok[i+1].ország and adatok[i+1].felhasználá - adatok[i].felhasználá < 0:
        print(f"{adatok[i].ország} felhasználása csökkent {adatok[i].év} évről {adatok[i+1].év}évre")

összfelh = []
for i in range(len(adatok) - 1):
    összfelh.append(adatok[i].felhasználá)
sortedösszfelh = összfelh.copy()
sortedösszfelh.sort()
sortedösszfelh.reverse()
felhországok = []
for i in range(len(sortedösszfelh)):
    if adatok[összfelh.index(sortedösszfelh[i])].ország not in felhországok and len(felhországok) != 10:
        felhországok.append(adatok[összfelh.index(sortedösszfelh[i])].ország)
felhországok.sort()
print(f"legnagyobb felhasználók:\n{', '.join(felhországok)}")

összkap = []
for i in range(len(adatok) - 1):
    összkap.append(adatok[i].kapacitá)
sortedösszkap = összkap.copy()
sortedösszkap.sort()
sortedösszkap.reverse()
kapországok = []
for i in range(len(sortedösszkap)):
    if adatok[összkap.index(sortedösszkap[i])].ország not in kapországok and len(kapországok) != 10:
        kapországok.append(adatok[összkap.index(sortedösszkap[i])].ország)
kapországok.sort()
print(f"legnagyobb kapacitás:\n{', '.join(kapországok)}")

felhországokset = set(felhországok)
kapországokset = set(kapországok)
unio = felhországokset.union(kapországokset)
metszet = felhországokset.intersection(kapországokset)
unio = list(unio)
metszet = list(metszet)
unio.sort()
metszet.sort()
print(f"A két csoport úniója:\n{', '.join(unio)}\nA jét csoport metszete:\n{', '.join(metszet)}")
