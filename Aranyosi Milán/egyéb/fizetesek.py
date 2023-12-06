# olvasd be a fizetesek.txt fájl tartalmát és tárold el
# egy sor azt mutatja meg, hogy adott évnyi munkatapasztalattal
# mennyi az éves átlagkereset az USA-ban

# 1. feladat: adatok beolvasása és tárolása
# figyelj, hogy az adatokat milyen típusra konvertálod
forras = open('fizetesek.txt', mode='r', encoding='utf-8')

munkatapasztalat = []
fizetes = []

for sor in range(forras):
    adat = sor.strip().split(';')
    munkatapasztalat.append(float(adat[0]))
    fizetes.apped(int(adat[1]))

forras.readline()

forras.close()

# 2. feladat: hány adatsort tartalmaz az adatfájl?
# minta: "A fájl 18 sort tartalmaz."

print(f'A fájl {len(fizetes)} sort tartalmaz.')

# 3. feladat: hány esetben csökkent a fizetés a tapasztalat növekedésével?
# minta: "5 esetben csökkent az átlagfizetés."

csokkent_a_fizetes = 0

for i in range(len(munkatapasztalat)):
    if munkatapasztalat[i] < munkatapasztalat[i+1] and fizetes[i] > fizetes[i+1]
        csokkent_a_fizetes += 1

print(f'{csokkent_a_fizetes} esetben csökkent az átlagfizetés.')

# 4. feladat: mekkora munkatapasztalattal kaphatunk legmagasabb fizetést?
# minta: "a Legmagasabb fizetést 7,8 év munkatapasztalattal lehet kapni."
# figyelj arra, hogy a minta szerinti legyen a szám megjelenítése

legnagyobb_fizetes_tapasztalat = munkatapasztalat[0]
lenagyobb_fiz = fizetes[0]

for i in range(len(fizetes)-1):
    if fizetes[i] < fizetes[i+1]:
        legnagyobb_fiz = fizetes[i+1]
        legnagyobb_fizetes_tapasztalat = munkatapasztalat[i+1]

print(f'a Legmagasabb fizetést {legnagyobb_fizetes_tapasztalat} év munkatasztalattal lehet kapni.')



# 5. feladat: listázd ki, hogy mely sorok jelentenek visszaeseést a fizetésben!
# minta: "4,2 év: $56 547"
# minta extra: "4,1 -> 4,2 év: $57 247 -> $56 547 (-1 300)"

errol_az_evrol = munkatapasztalat[i]
erre_az_evre = munkatapasztalat[i+1]
errol_a_fiz = fizetes[i]
erre_a_fiz = fizetes[i+1]

for i in range(len(munktapasztalat)):
    if munkatapasztalat[i] < munkatapasztalat[i+1] and fizetes[i] > fizetes[i+1]:
        errol_az_evrol = munkatapasztalat[i]
        erre_az_evre = munkatapasztalat[i+1]
        errol_a_fiz = fizetes[i]
        erre_a_fiz = fizetes[i+1]

kulonbseg =  erre_a_fiz - errol_a_fiz

print(f'{errol_az_evrol} -> {erre_az_evre} év: ${errol_a_fiz} -> ${erre_a_fiz} ({kulonbseg})')

# 6. feladat: a megoldást commitold és pushold
# fizetesek.py néven nyersen, ahogy megírtad jegyzettömbben
# fizetesek-javitott.py néven miután PyCharm-ban kijavítottad