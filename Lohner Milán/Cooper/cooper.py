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

forras = open('cooper.txt', mode='r', encoding='utf-8')

tavaly = []
iden = []

for sor in range(forras):
	adat = sor.strip().split('\t')
	iden.append(int(adat[1]))
	tavaly.append(int(adat[0])) 

forras.close
# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.

for i in range(len(adat)):
	szamolas = adat.count /2
	print('A teszten {szamolas} diák vett részt.')
	
# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.

for sor in range(len(iden)):
	haromnagy= sum(1, if iden[i] >= 3000):
		print('Idén {haromnagy} diák futott legalább 3000 m-t.')
# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén?
# minta: Az idei legjobb eredmény 3450 m volt.
# minta-extra: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.
legjobb = iden[0]

for sor in range(len(iden)):
	if iden[0] > legjobb:
		legjobb = idei[i]
Az idei legjobb eredmény {legjobb} volt.
	
# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás (azaz az idei-tavalyi eredmény maximális értéke)?
# minta: A legnagyobb javítás 231 m volt.
# minta-extra: A legtöbbet Gáz Áron javított, ő 265 m-rel futott többet idén, mint tavaly.

legnagyobb_jav = iden[0] - tavaly[0]
for i in range(len(iden)):
	kulonbseg = iden[i] - tavaly[i]
	if kulonbseg > legnagyobb_jav:
		legnagyobb_jav == kulonbseg

print('A legnagyobb javítás {legnagyobb_jav}m volt.')
	
	
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

for i in range(len(iden))

