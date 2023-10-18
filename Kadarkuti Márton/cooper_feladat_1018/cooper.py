# olvasd be az adatokat tartalmazó fájlok egyikét
# 	a cooper.txt minden számadatot tartalmaz, de a neveket nem, ezzel lesz egyszerűbb dolgoznod
# 	a cooper-extra.txt a neveket és egy fejlécet is tartalmaz, ezzel oldhatod meg az extra feladatokat is
# --------------------------------------------------------------------------------------------------------
# mindkét fájl a 11. évfolyam Cooper tesztjének eredményét tartalmazza, azaz hogy tavaly és idén 
# hány métert tudtak futni a diákok 12 perc alatt
# a programodat a megjegyzésként beírt szövegrészek után (közé) írd be
# figyelj a minta szövegre, annak megfelelően formázd a saját kiírásaidat is

# --------------------------------------------------------------------------------------------------------
# 1. feladat: adatok beolvasása és tárolása

def vonal():
	print("-"*30)

nev = []
eredmeny_tavaly = []
eredmeny_iden = []

with open("cooper-extra.txt", "r", encoding="utf-8") as f:
	f.readline()
	for sor in f:
		adat = sor.strip().split("\t")
		adat[1], adat[2] = int( adat[1] ), int( adat[2] )
		nev.append( adat[0] )
		eredmeny_tavaly.append( adat[1] )
		eredmeny_iden.append( adat[2] )

l = len(nev) # mindhárom lista hossza egyenlő
vonal()
# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.

print(f"A teszten {l} diák vett részt.")
vonal()
# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.

legalabb_3km_iden = 0
for i in range(l):
	if eredmeny_iden[i] >= 3000:
		legalabb_3km_iden += 1

print(f"Idén {legalabb_3km_iden} diák futott legalább 3000m-t.")
vonal()
# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén?
# minta: Az idei legjobb eredmény 3450 m volt.
# minta-extra: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.

legjobb_iden = 0  # indexet ment el
for i in range(l):
	if eredmeny_iden[legjobb_iden] < eredmeny_iden[i]:
		legjobb_iden = i

print(f"Az idei legjobb eredményt {nev[legjobb_iden]} érte el {eredmeny_iden[legjobb_iden]} m-es távval.")
vonal()

# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás (azaz az idei-tavalyi eredmény maximális értéke)?
# minta: A legnagyobb javítás 231 m volt.
# minta-extra: A legtöbbet Gáz Áron javított, ő 265 m-rel futott többet idén, mint tavaly.

legnagyobb_javitas = 0  # indexet ment el
d = 0  # különbség
d_max = 0 # ideiglenes legnagyobb különbség
for i in range(l):
	d = eredmeny_iden[i] - eredmeny_tavaly[i]
	if d <= 0:
		continue
	d_max = eredmeny_iden[legnagyobb_javitas] - eredmeny_tavaly[legnagyobb_javitas]
	if d > d_max:
		legnagyobb_javitas = i
if bool(legnagyobb_javitas):
	print(f"A legtöbbet {nev[legnagyobb_javitas]} javított, ő {eredmeny_iden[legnagyobb_javitas] - eredmeny_tavaly[legnagyobb_javitas]} m-rel futott többet idén, mint tavaly.")
else:
	print("Senki nem javított.")
vonal()
# --------------------------------------------------------------------------------------------------------
# 6. feladat: listázd ki az idei 3000 m felett teljesítőket
# minta: 
# 3124
# 3187
# ...
# minta-extra: 
# Mekk Elek    3143
# Kis Miska    3251
# Kő Pál       3423
# ...

haromezer_felett = []
for i in range(l):
	if eredmeny_iden[i] >= 3000:
		haromezer_felett.append(i)

print("- 3000m FELETT TELJESÍTŐK -")
for i in range(len(haromezer_felett)):
	print(f"{ nev[ haromezer_felett[i] ] } -=- {eredmeny_iden[ haromezer_felett[i] ]}m ")
vonal()