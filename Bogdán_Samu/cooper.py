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

forrás = open('cooper-extra.txt', mode='r', encoding='utf-8')
forrás.readline()
név = []
tavaly = []
idén = []
for i in forrás:
	sor = i.strip().split('	')
	név.append(str(sor[0]))
	tavaly.append(int(sor[1]))
	idén.append(int(sor[2]))
forrás.close()

# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.

print(f'A teszten {len(név)} diák vett részt.')

# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.

háromezer = 0
for i in range(len(név)):
	if idén[i] >= 3000:
		háromezer += 1
if háromezer > 0:
	print(f'Idén {háromezer} diák futott legalább 3000 m-t.')
else:
	print('Idén egy diák sem futott legalább 3000 m-t.')

# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén?
# minta: Az idei legjobb eredmény 3450 m volt.
# minta-extra: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.

index = idén.index(max(idén))
print(f'Az idei legjobb eredményt {név[index]} érte el {idén[index]} m-es távval.')

# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás (azaz az idei-tavalyi eredmény maximális értéke)?
# minta: A legnagyobb javítás 231 m volt.
# minta-extra: A legtöbbet Gáz Áron javított, ő 265 m-rel futott többet idén, mint tavaly.

javítás = idén[0] - tavaly[0]
index = 0
for i in range(len(név)-1):
	if idén[i+1] - tavaly[i+1] > idén[i] - tavaly[i]:
		javítás = idén[i+1] - tavaly[i+1]
		index = i + 1
print(f'A legtöbbet {név[index]} javított, ő {javítás} m-rel futott többet idén, mint tavaly.')

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

for i in range(len(név)):
	if idén[i] >= 3000:
		print(név[i], idén[i])
