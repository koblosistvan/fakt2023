# olvasd be a fizetesek.txt fájl tartalmát és tárold el
# egy sor azt mutatja meg, hogy adott évnyi munkatapasztalattal
# mennyi az éves átlagkereset az USA-ban

# 1. feladat: adatok beolvasása és tárolása
# figyelj, hogy az adatokat milyen típusra konvertálod

forras = open('fizetesek.txt', mode='r', encoding='utf-8')
munkaxp = []
fizetes = []
forras.readline()
for sor in forras:
    adat = sor.strip().split(';')
    munkaxp.append(float(adat[0]))
    fizetes.append(int(adat[1]))

# 2. feladat: hány adatsort tartalmaz az adatfájl?
# minta: "A fájl 18 sort tartalmaz."

sorokszama = len(fizetes)

print(f"A fájl {sorokszama} sort tartalmaz.")

# 3. feladat: hány esetben csökkent a fizetés a tapasztalat növekedésével?
# minta: "5 esetben csökkent az átlagfizetés."

csesetek = 0
csfizetes = []
csmunkaxp = []
for i in range(len(munkaxp)-1):
    if fizetes[i] > fizetes[i+1]:
        csesetek += 1
        csfizetes.append(fizetes[i]), csfizetes.append(fizetes[i+1])
        csmunkaxp.append(munkaxp[i]), csmunkaxp.append(munkaxp[i+1])

print(f"{csesetek} esetben csökkent az átlagfizetés.")

# 4. feladat: mekkora munkatapasztalattal kaphatunk legmagasabb fizetést?
# minta: "a Legmagasabb fizetést 7,8 év munkatapasztalattal lehet kapni."
# figyelj arra, hogy a minta szerinti legyen a szám megjelenítése

magasfizetesindex = fizetes.index(max(fizetes))
magasfizetes = str(munkaxp[magasfizetesindex]).split('.')
print(f"a Legmagasabb fizetést {magasfizetes[0]},{magasfizetes[1]} év munkatapasztalattal lehet kapni.")

# 5. feladat: listázd ki, hogy mely sorok jelentenek visszaeseést a fizetésben!
# minta: "4,2 év: $56 547"
# minta extra: "4,1 -> 4,2 év: $57 247 -> $56 547 (-1 300)"

a = 2
b = 3

print(f"{csmunkaxp[0]} -> {csmunkaxp[1]} év: ${csfizetes[0]} -> ${csfizetes[1]} ({csfizetes[1]-csfizetes[0]})")
for i in range(len(csmunkaxp)):
    print(f"{csmunkaxp[a]} -> {csmunkaxp[b]} év: ${csfizetes[a]} -> ${csfizetes[b]} ({csfizetes[b]-csfizetes[a]})")
    a += 2
    b += 2

# 6. feladat: a megoldást commitold és pushold
# fizetesek.py néven nyersen, ahogy megírtad jegyzettömbben
# fizetesek-javitott.py néven miután PyCharm-ban kijavítottad
