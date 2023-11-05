# olvasd be a fizetesek.txt.txt fájl tartalmát és tárold el
# egy sor azt mutatja meg, hogy adott évnyi munkatapasztalattal
# mennyi az éves átlagkereset az USA-ban

# 1. feladat: adatok beolvasása és tárolása
# figyelj, hogy az adatokat milyen típusra konvertálod

forras = open('fizetesek.txt', 'r', encoding='utf-8')
munkatapasztalat = []
eves_atlagkereset = []
forras.readline()
for sor in forras:
    adat = sor.strip().split(';')
    munkatapasztalat.append(float(adat[0]))
    eves_atlagkereset.append(int(adat[1]))
forras.close()


# 2. feladat: hány adatsort tartalmaz az adatfájl?
# minta: "A fájl 18 sort tartalmaz."

print(f'A fájl {len(munkatapasztalat)} sort tartalmaz.')


# 3. feladat: hány esetben csökkent a fizetés a tapasztalat növekedésével?
# minta: "5 esetben csökkent az átlagfizetés."

csokkenes = 0
for i in range(len(munkatapasztalat) - 1):
    if munkatapasztalat[i] / eves_atlagkereset[i] > munkatapasztalat[i+1] / eves_atlagkereset[i+1]:
        csokkenes += 1
print(f'{csokkenes} esetben csökkent az átlagfizetés.')


# 4. feladat: mekkora munkatapasztalattal kaphatunk legmagasabb fizetést?
# minta: "a Legmagasabb fizetést 7,8 év munkatapasztalattal lehet kapni."
# figyelj arra, hogy a minta szerinti legyen a szám megjelenítése

legmagasabb = 0
for i in range(len(munkatapasztalat)):
    if eves_atlagkereset[i] > legmagasabb:
        legmagasabb = eves_atlagkereset[i]
        i_4 = i
legmagasabb = str(munkatapasztalat[i_4])
legmagasabb = legmagasabb.strip().split('.')
print(f'A legmagasabb fizetést {legmagasabb[0]},{legmagasabb[1]} év munkatapasztalattal lehet kapni.')


# 5. feladat: listázd ki, hogy mely sorok jelentenek visszaeseést a fizetésben!
# minta: "4,2 év: $56 547"
# minta extra: "4,1 -> 4,2 év: $57 247 -> $56 547 (-1 300)"

for i in range(len(munkatapasztalat) - 1):
    if eves_atlagkereset[i] > eves_atlagkereset[i+1]:
        i_5 = i
print(f'{munkatapasztalat[i_5]} -> {munkatapasztalat[i_5 + 1]}, év: {eves_atlagkereset[i_5]} -> {eves_atlagkereset[i_5 + 1]} ({eves_atlagkereset[i_5 + 1] - eves_atlagkereset[i_5]})')



# 6. feladat: a megoldást commitold és pushold
# fizetesek.txt.py néven nyersen, ahogy megírtad jegyzettömbben
# fizetesek.txt-javitott.py néven miután PyCharm-ban kijavítottad