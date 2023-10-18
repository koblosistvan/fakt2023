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

forras = open('cooper-extra.txt', 'r', encoding='utf-8')
nevek = []
tavaly = []
iden = []
forras.readline()
for sor in forras:
	adat = sor.strip().split('\t')
	nevek.append('{adat[0]} {adat[1]}')
	tavaly.append(int(adat[2]))
	iden.append(int(adat[3]))
forras.close()


# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.

print(f'A teszten {len(nevek)} diák vett részt.')


# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.

legalabb_3000 = []
for i in range(len(iden)):
	if iden[i] >= 3000:
	legalabb_3000.append(iden[i])
print(f'Idén {len(legalabb_3000)} diák futott legalább 3000m-t.')


# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén?
# minta: Az idei legjobb eredmény 3450 m volt.
# minta-extra: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.

legjobb_iden = 0
for i in range(len(iden)):
	if iden[i] > legjobb_iden:
		legjobb_iden = iden[i]
		i_ertek = i
print(f'Az idei legjobb eredményt {nevek[i_ertek]} érte el {legjobb_iden} m-es távval.')


# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás (azaz az idei-tavalyi eredmény maximális értéke)?
# minta: A legnagyobb javítás 231 m volt.
# minta-extra: A legtöbbet Gáz Áron javított, ő 265 m-rel futott többet idén, mint tavaly.

legnagyobb_javitas = 0
for i in range(len(iden)):
	if iden[i] - tavaly[i] > legnagyobb_javitas:
		legnagyobb_javitas = iden[i] - tavaly[i]:
		i_5 = i
print(f'A legtöbbet {nevek[i_5]} javított, ő {legnagyobb_javitas} m-rel futott többet idén, mint tavaly.')


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

for i in range(len(legalabb_3000)):
	segedvaltozo = nevek.index(legalabb_3000[i]) + 1
	print(f'{nevek[segedvaltozo]}	{legalabb_3000[i]}')

