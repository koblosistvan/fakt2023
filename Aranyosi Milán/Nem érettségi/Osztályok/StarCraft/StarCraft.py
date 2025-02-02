class Starcraft:
    def __init__(self, egyseg, faj, pajzs, hp, foldiseb, legiseb):
        self.egyseg = egyseg
        self.faj = faj
        self.pajzs = pajzs
        self.hp = hp
        self.foldiseb = foldiseb
        self.legiseb = legiseb

starcraft = []
forras = open('StarCraft.txt', encoding='utf-8', mode='r')
forras.readline()
for sor in forras:
    adat = sor.strip().split('\t')
    starcraft.append(Starcraft(egyseg=adat[0], faj=adat[1], pajzs=int(adat[2]), hp=int(adat[3]), foldiseb=int(adat[4]), legiseb=int(adat[5])))
forras.close()

#1. feladat
print(f'{len(starcraft)} egységet tartalmaz az állomány.')

#2. feladat
legtobbhp = starcraft[0].hp
legtobbhp_faj = starcraft[0].faj
legtobbhp_nev = starcraft[0].egyseg
for i in range(len(starcraft)):
    if starcraft[i].hp > legtobbhp:
        legtobbhp = starcraft[i].hp
        legtobbhp_faj = starcraft[i].faj
        legtobbhp_nev = starcraft[i].egyseg
print(f'A legtöbb hp-val rendelkező faja: {legtobbhp_faj}, neve: {legtobbhp_nev}.')

#3. feladat
szamlalo = 0
for i in range(len(starcraft)):
    if starcraft[i].faj == 'Protoss' and starcraft[i].foldiseb > 0:
        szamlalo += 1
print(f'{szamlalo} eleme van a Protossoknak ami földi célpontokat is tud támadni.')

#4. feladat
kimenet = open('starcraft-tamadók.txt', mode='w', encoding='utf-8')

for i in range(len(starcraft)):
    if starcraft[i].foldiseb > 0 and starcraft[i].legiseb > 0:
        print(f'{starcraft[i].egyseg} {starcraft[i].faj} {starcraft[i].pajzs} {starcraft[i].hp} {starcraft[i].foldiseb} {starcraft[i].legiseb}', file=kimenet)

#5. feladat
szamlalo2 = 0
for i in range(len(starcraft)):
    if starcraft[i].faj == 'Zerg' and starcraft[i].foldiseb > 100 or starcraft[i].legiseb > 100:
        szamlalo2 += 1
        break

if szamlalo2 == 1:
    print('Van ilyen.')

#6. feladat
osszhp = 0
terranszamlalo = 0
for i in range(len(starcraft)):
    if starcraft[i].faj == 'Terran':
        osszhp += starcraft[i].hp
        terranszamlalo += 1
print(f'A Terran egységeg átlagos hp-ja: {osszhp // terranszamlalo}.')

#7. feladat
goliath_hp = 0
goliath_tamadas= 0
for i in range(len(starcraft)):
    if starcraft[i].egyseg == 'Goliath':
        goliath_hp = starcraft[i].hp
        goliath_tamadas = starcraft[i].foldiseb
        break

hidralisk_hp = 0
hidralisk_tamadas = 0
for i in range(len(starcraft)):
    if starcraft[i].egyseg == 'Hydralisk':
        hidralisk_hp = starcraft[i].hp
        hidralisk_tamadas = starcraft[i].foldiseb
        break

harc_1resz = goliath_hp / hidralisk_tamadas
harc_2resz = hidralisk_hp / goliath_tamadas

if harc_1resz < harc_2resz:
    print('Hidralisk nyerne.')
elif harc_1resz == harc_2resz:
    print('Döntetlen')
else:
    print('Goliath nyerne.')







