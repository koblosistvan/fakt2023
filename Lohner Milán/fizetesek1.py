# olvasd be a fizetesek.txt fájl tartalmát és tárold el
# egy sor azt mutatja meg, hogy adott évnyi munkatapasztalattal 
# mennyi az éves átlagkereset az USA-ban

# 1. feladat: adatok beolvasása és tárolása
# figyelj, hogy az adatokat milyen típusra konvertálod

forras = open('fizetesek.txt', mode='r', encoding='utf-8' )

munkatap = []

fizetes = []

for sor in forras:
	adat = sor.strip().split(';')
	munkatap.append(adat[0])
	fizetes.append(adat[1])
	





# 2. feladat: hány adatsort tartalmaz az adatfájl?
# minta: "A fájl 18 sort tartalmaz."

sordarab = forras.readline()

print(f'A fájl {sordarab} sort tartalmaz.')


# 3. feladat: hány esetben csökkent a fizetés a tapasztalat növekedésével?
# minta: "5 esetben csökkent az átlagfizetés."

esetek = 0

for i in range(len(fizetes)):
	if fizetes[i] < fizetes[i-1]:
		esetek += 1

print(f'{esetek} esetben csökkent az átlagfizetés.')
 


# 4. feladat: mekkora munkatapasztalattal kaphatunk legmagasabb fizetést?
# minta: "a Legmagasabb fizetést 7,8 év munkatapasztalattal lehet kapni."
# figyelj arra, hogy a minta szerinti legyen a szám megjelenítése

print(f'A legmagasabb fizetést {(max(munkatap))} év munkatapasztalattal lehet kapni')
	

# 5. feladat: listázd ki, hogy mely sorok jelentenek visszaeseést a fizetésben!
# minta: "4,2 év: $56 547"
# minta extra: "4,1 -> 4,2 év: $57 247 -> $56 547 (-1 300)"




	




# 6. feladat: a megoldást commitold és pushold 
# fizetesek.py néven nyersen, ahogy megírtad jegyzettömbben
# fizetesek-javitott.py néven miután PyCharm-ban kijavítottad
