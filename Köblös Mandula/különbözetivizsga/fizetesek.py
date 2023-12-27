# olvasd be a fizetesek.txt fájl tartalmát és tárold el
# egy sor azt mutatja meg, hogy adott évnyi munkatapasztalattal
# mennyi az éves átlagkereset az USA-ban

# 1. feladat: adatok beolvasása és tárolása
# figyelj, hogy az adatokat milyen típusra konvertálod

forrás = open("fizetesek.txt", mode="r", encoding="utf-8")

munkatapasztalat = []
kereslet = []

forrás.readline()

for sor in forrás:
    adat = sor.strip().split(";")
    munkatapasztalat.append(int(adat[0]))
    kereslet.append(int(adat[1]))
    

forrás.close()

# 2. feladat: hány adatsort tartalmaz az adatfájl?
# minta: "A fájl 18 sort tartalmaz."
print(f"A fájl {len(munkatapasztalat)} sort tartalmaz.")

# 3. feladat: hány esetben csökkent a fizetés a tapasztalat növekedésével?
# minta: "5 esetben csökkent az átlagfizetés."
csökken = 0
for i in range(len(munkatapasztalat)-1):
    if kereslet[i] > kereslet[i+1]:
        csökken += 1
print(f"{csökken} esetben csökkent az átlagfizetés.")

# 4. feladat: mekkora munkatapasztalattal kaphatunk legmagasabb fizetést?
# minta: "a Legmagasabb fizetést 7,8 év munkatapasztalattal lehet kapni."
# figyelj arra, hogy a minta szerinti legyen a szám megjelenítése
legmagasabb = 0
for i in range(len(munkatapsztalat)):
    if kereslet[i] > kereslet[legmagasabb]:
        legmagasabb = kereslet[i]
print(f"a Legmagasabb fizetést {legmagasabb:.1f} év munkatapasztalattal lehet kapni.")

# 5. feladat: listázd ki, hogy mely sorok jelentenek visszaeseést a fizetésben!
# minta: "4,2 év: $56 547"
# minta extra: "4,1 -> 4,2 év: $57 247 -> $56 547 (-1 300)"
for i in range(len(munkatapasztalat)-1):
    if kereslet[i] > kereslet[i+1]:
        print(f"{munkatapasztalat[i+1]} év: {kereslet[i+1]")

# 6. feladat: a megoldást commitold és pushold
# fizetesek.py néven nyersen, ahogy megírtad jegyzettömbben
# fizetesek-javitott.py néven miután PyCharm-ban kijavítottad