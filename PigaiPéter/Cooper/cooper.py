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
forras = open('cooper-extra.txt', mode='r', encoding='utf-8')
forras.readline()
nevek = []
tavaly = []
iden = []

for i in forras:
	sor = i.strip().split('\t')
	nevek.append(sor[0])
	tavaly.append(sor[1])
	iden.appen(sor[2])
forras.close
# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.
diakszam = 0

for i in range(len(tavaly)):
	diakszam +=1
print(f'A teszten {diakszam} diák vett részt.')

# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.

minhe = 0
for i in range(len(iden)):
	if iden[i] > 3000:
		minhe += 1
print(f'Idén {minhe} diák futott legalább 3000 m-t.')
# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén?
# minta: Az idei legjobb eredmény 3450 m volt.
# minta-extra: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.
legjobbember = ''
legjobb = 999999999
for i in range(len(iden)):
	if iden[i] > legjobb:
		legjobb = iden[i]
		legjobbember = nevek[i]
print(f'Az idei legjobb eredmény {legjobb} m volt.')
print(f'Az idei legjobb eredményt {legjobbember} érte el {legjobb} m-es távval.')
# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás (azaz az idei-tavalyi eredmény maximális értéke)?
# minta: A legnagyobb javítás 231 m volt.
# minta-extra: A legtöbbet Gáz Áron javított, ő 265 m-rel futott többet idén, mint tavaly.
javitasember = ''
javitas = 0
for i in range(len(tavaly)):
	if tavaly[i] - iden[i] > javitas:
		javitas = tavaly[i] - iden[i]
		javitasember = nevek[i]
print(f'A legnagyobb javítás {javitas} m volt.')
print(f'A legtöbbet {javitasember} javított, ő {javitas} m-rel futott többet idén, mint tavaly.')
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

for i in range(len(iden)):
	if iden[i] > 3000:
		print(f'{nevek[i]} \t {iden[i]}')
