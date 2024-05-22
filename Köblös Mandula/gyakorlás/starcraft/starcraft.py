class starcraft:
    def __init__(self, egyseg: str, faj: str, pajzs: int, hp: int, fold_ellen: int, levego_ellen: int):
        self.egyseg = egyseg
        self.faj = faj
        self.pajzs = pajzs
        self.hp = hp
        self.fold_ellen = fold_ellen
        self.levego_ellen = levego_ellen

egysegek = []
forras = open('starcraft.txt', mode='r', encoding='utf-8')
forras.readline()
for sor in forras:
    adat = sor.strip().split('\t')
    egysegek.append(starcraft(egyseg=str(adat[0]), faj=str(adat[1]), pajzs=int(adat[2]), hp=int(adat[3]), fold_ellen=int(adat[4]), levego_ellen=int(adat[5])))
forras.close()

# 1. feladat
print(f'{len(egysegek)} egység adatait tartalmazza az állomány.')

# 2. feladat
legerosebb = egysegek[0].hp
legerosebb_id = 0
for i in range(len(egysegek)):
    if egysegek[i].hp > legerosebb:
        legerosebb = egysegek[i].hp
        legerosebb_id = i
print(f'A legerősebb egységnek {legerosebb} HP-ja van. A {egysegek[legerosebb_id].faj} fajhoz tartozik és {egysegek[legerosebb_id].egyseg} a neve.')

# 3. feladat
foldellen_tamado = 0
for i in range(len(egysegek)):
    if egysegek[i].faj == "Protoss" and egysegek[i].fold_ellen > 0:
        foldellen_tamado += 1
print(f'{foldellen_tamado} olyan egysége van a Protossoknak ami tud földi célpontokat támadni.')

kimenet = open('starcraft-támadók.txt', mode='w', encoding='utf-8')

# 4. feladat
for i in range(len(egysegek)):
    if egysegek[i].fold_ellen > 0 and egysegek[i].levego_ellen > 0:
        print(f'{egysegek[i].egyseg} {egysegek[i].faj} {egysegek[i].pajzs} {egysegek[i].hp} {egysegek[i].fold_ellen} {egysegek[i].levego_ellen}', file=kimenet)

kimenet.close()

# 5. feladat
for i in range(len(egysegek)):
    if egysegek[i].faj == "Zerg" and (egysegek[i].fold_ellen > 100 or egysegek[i].levego_ellen > 100):
        print(f'Van olyan Zerg egység, amely 100-nál többet sebez.')
        break
    else:
        print(f'Nincs olyan Zerg egység, amely 100-nál többet sebez.')

# 6. feladat
atlagos_hp = 0
terranok = 0
for i in range(len(egysegek)):
    if egysegek[i].faj == 'Terran':
        terranok += 1
        atlagos_hp += egysegek[i].hp
print(f'A Terran egységnek átlagosan {atlagos_hp/terranok} HP-ja van.')