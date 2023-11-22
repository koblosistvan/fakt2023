# olvasd be a fizetesek.txt fájl tartalmát és tárold el
# egy sor azt mutatja meg, hogy adott évnyi munkatapasztalattal
# mennyi az éves átlagkereset az USA-ban

def vonal():
	print("-"*30)

munkatapasztalat = []
fizetes = []

with open("fizetesek.txt", "r", encoding="utf-8") as f:
	f.readline()

	# 1. feladat: adatok beolvasása és tárolása
	# figyelj, hogy az adatokat milyen típusra konvertálod

	for sor in f:
		adat = sor.strip().split(";")
		munkatapasztalat.append( float(adat[0]) )
		fizetes.append( int(adat[1]) )
vonal()

# 2. feladat: hány adatsort tartalmaz az adatfájl?
# minta: "A fájl 18 sort tartalmaz."

l = len(munkatapasztalat)
print(f"A fájl {l} sort tartalmaz.")
vonal()

# 3. feladat: hány esetben csökkent a fizetés a tapasztalat növekedésével?
# minta: "5 esetben csökkent az átlagfizetés."

csokkent_atlagfizetes = 0

for i in range( l-1 ):
	if ( munkatapasztalat[i+1] > munkatapasztalat[i] ) and ( fizetes[i+1] < fizetes[i] ):
		csokkent_atlagfizetes += 1
print(f"{ csokkent_atlagfizetes  } esetben csökkent az átlagfizetés.")
vonal()

# 4. feladat: mekkora munkatapasztalattal kaphatunk legmagasabb fizetést?
# minta: "a Legmagasabb fizetést 7,8 év munkatapasztalattal lehet kapni."
# figyelj arra, hogy a minta szerinti legyen a szám megjelenítése

legnagyobb_fizetes_index = munkatapasztalat[ fizetes.index( max(fizetes) ) ]

def tizedesjegy(t):
	if str(t)[-1] == "0":
		return str( int(t) )

	else:
		t = str(t)
		t = t.split(".")[0] + "," + t.split(".")[1]
		return t

print(f"A legmagasabb fizetést { tizedesjegy( legnagyobb_fizetes_index ) } év munkatapasztalattal lehet kapni.")
vonal()

# 5. feladat: listázd ki, hogy mely sorok jelentenek visszaeseést a fizetésben!
# minta: "4,2 év: $56 547"
# minta extra: "4,1 -> 4,2 év: $57 247 -> $56 547 (-1 300)"

lista_tizedes = munkatapasztalat

for i in range(l):
	lista_tizedes[i] = tizedesjegy( lista_tizedes[i] )

visszaesett = []  #indexet menti el
for i in range( l-1 ):
	if fizetes[i+1] < fizetes[i]:
		visszaesett.append(i)

print("  ADATTÁBLA")
for i in range( len(visszaesett) -1):
    d = fizetes[ visszaesett[i] ] - fizetes[ visszaesett[i+1] ]
    if d < 0:
	    print(f"{lista_tizedes[ visszaesett[i] ]} -> {lista_tizedes[ visszaesett[i+1] ]} év: ${fizetes[ visszaesett[i] ]} -> ${fizetes[ visszaesett[i+1] ]} ({d})")


# 6. feladat: a megoldást commitold és pushold
# fizetesek.py néven nyersen, ahogy megírtad jegyzettömbben
# fizetesek-javitott.py néven miután PyCharm-ban kijavítottad
