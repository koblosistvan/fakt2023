# olvasd be a fizetesek.txt fájl tartalmát és tárold el
# egy sor azt mutatja meg, hogy adott évnyi munkatapasztalattal 
# mennyi az éves átlagkereset az USA-ban

def fel(x):
	print(f"\n{x}. feladat:", end=" ")

# 1. feladat: adatok beolvasása és tárolása
# figyelj, hogy az adatokat milyen típusra konvertálod

forrás = open("fizetesek.txt", mode="r", encoding="utf-8")

felirat = forrás.readline()

év = []
kereset = []

for sor in forrás:
	adat = sor.strip().split(";")
	év.append(float(adat[0]))
	kereset.append(int(adat[1]))

forrás.close()

# 2. feladat: hány adatsort tartalmaz az adatfájl?
# minta: "A fájl 18 sort tartalmaz."

fel(2)

print(f"A fájl {len(év)} sort tartalmaz.")

# 3. feladat: hány esetben csökkent a fizetés a tapasztalat növekedésével?
# minta: "5 esetben csökkent az átlagfizetés."

fel(3)

csökkent_a_fizu = 0

for i in range(1, len(év)):
	if év[i-1] < év[i] and kereset[i-1] > kereset[i]:
		csökkent_a_fizu += 1

print(f"{csökkent_a_fizu} esetben csökkent az átlagfizetés.")

# 4. feladat: mekkora munkatapasztalattal kaphatunk legmagasabb fizetést?
# minta: "a Legmagasabb fizetést 7,8 év munkatapasztalattal lehet kapni."
# figyelj arra, hogy a minta szerinti legyen a szám megjelenítése

fel(4)

print(f"a legmagasabb fizetést {év[kereset.index(max([kereset[i] for i in range(len(kereset))]))]} év munkatapasztalattal lehet kapni.")

# 5. feladat: listázd ki, hogy mely sorok jelentenek visszaeseést a fizetésben!
# minta: "4,2 év: $56 547"
# minta extra: "4,1 -> 4,2 év: $57 247 -> $56 547 (-1 300)"

fel(5)

print()

for i in range(1, len(év)):
	if év[i-1] < év[i] and kereset[i-1] > kereset[i]:
		print(f"{év[i-1]} -> {év[i]} év: ${kereset[i-1]} -> ${kereset[i]} ({kereset[i]-kereset[i-1]})")

# 6. feladat: a megoldást commitold és pushold 
# fizetesek.py néven nyersen, ahogy megírtad jegyzettömbben
# fizetesek-javitott.py néven miután PyCharm-ban kijavítottad
