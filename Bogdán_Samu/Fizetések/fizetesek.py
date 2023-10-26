# olvasd be a fizetesek.txt fájl tartalmát és tárold el
# egy sor azt mutatja meg, hogy adott évnyi munkatapasztalattal 
# mennyi az éves átlagkereset az USA-ban

# 1. feladat: adatok beolvasása és tárolása
# figyelj, hogy az adatokat milyen típusra konvertálod

forrás = open('fizetesek.txt', mode='r', encoding='utf-8')
forrás.readline()
tapasztalat = []
fizetés = []
for i in forrás:
	sor = i.strip().split(';')
	tapasztalat.append(float(sor[0]))
	fizetés.append(int(sor[1]))

# 2. feladat: hány adatsort tartalmaz az adatfájl?
# minta: "A fájl 18 sort tartalmaz."

print(f'A fájl {len(tapasztalat)} sort tartalmaz.')

# 3. feladat: hány esetben csökkent a fizetés a tapasztalat növekedésével?
# minta: "5 esetben csökkent az átlagfizetés."

id = 0
for i in range(len(tapasztalat)-1):
	if tapasztalat[i+1] > tapasztalat[i] and fizetés[i+1] < fizetés[i]:
		id += 1
print(f'{id} esetben csökkent az átlagfizetés.')

# 4. feladat: mekkora munkatapasztalattal kaphatunk legmagasabb fizetést?
# minta: "a Legmagasabb fizetést 7,8 év munkatapasztalattal lehet kapni."
# figyelj arra, hogy a minta szerinti legyen a szám megjelenítése

fiz_id = fizetés.index(max(fizetés))
tapaszt1 = round(tapasztalat[fiz_id], 0)
tapaszt2 = tapaszt1 + 1
print(f'A legmagasabb fizetést {tapaszt1},{tapaszt2} év munkatapasztalattal lehet kapni.')

# 5. feladat: listázd ki, hogy mely sorok jelentenek visszaeseést a fizetésben!
# minta: "4,2 év: $56 547"
# minta extra: "4,1 -> 4,2 év: $57 247 -> $56 547 (-1 300)"

for i in range(len(tapasztalat)-1):
	if fizetés[i+1] < fizetés[i]:
		print(f'{tapasztalat[i]} -> {tapasztalat[i+1]} év: ${fizetés[i]} -> ${fizetés[i+1]} ({fizetés[i] - fizetés[i+1]})')

# 6. feladat: a megoldást commitold és pushold 
# fizetesek.py néven nyersen, ahogy megírtad jegyzettömbben
# fizetesek-javitott.py néven miután PyCharm-ban kijavítottad
