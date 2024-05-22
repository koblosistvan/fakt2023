class Starcraft:
    def __init__(self, egyseg: str, faj: str, pajzs: int, hp: int, fold: int, levego: int):
        self.egyseg = egyseg
        self.faj = faj
        self.pajzs = pajzs
        self.hp = hp
        self.fold = fold
        self.levego = levego

#
forras = open("PigaiPéter\\starcraft\starcraft.txt", "r", encoding="utf-8")
forras.readline()
data = []
for i in forras:
    adat = i.strip().split("\t")
    data.append(Starcraft(egyseg=str(adat[0]), faj=str(adat[1]), pajzs=int(adat[2]), hp=int(adat[3]), fold=int(adat[4]), levego=int(adat[5])))
forras.close()

#
print(f'{len(data)} db egység van a listában')

#
legerosebb = data[0].fold + data[0].levego
counter = 0
for i in data:
    if (i.fold + i.levego) > legerosebb:
        legerosebb = i.fold + i.levego
        eroindex = counter
    counter += 1
print(f"A legerősebb egység HP-ja {data[eroindex].hp}, {data[eroindex].faj}, {data[eroindex].egyseg}")

#
protosskezdo = 0
protossvegzo = 0
for i in data:
    protosskezdo += 1
    if i.faj == "Protoss":
        break
for i in data:
    if i.faj == "Zerg":
        break
    protossvegzo += 1
foldi = 0
for i in range(protosskezdo, protossvegzo):
    if data[i].fold != 0:
        foldi += 1
print(f'{foldi} db földi Protoss egység van')

#
kiir = open("PigaiPéter\\starcraft\starcraft-támadók.txt", "w", encoding="utf-8")
for i in data:
    if i.fold != 0 and i.levego != 0:
        sor = [i.egyseg, i.faj, str(i.pajzs), str(i.hp), str(i.fold), str(i.levego), "\n"]
        sor = " ".join(sor)
        kiir.write(f"{sor}")

#
van = False
for i in range(protossvegzo + 1, len(adat)):
    if i.fold > 100 or i.levego > 100:
        van = True
if van:
    print("Van olyan Zerg egység ami 100-nál többet sebez")
else:
    print("Nincs olyan Zerg egység ami 100-nál többet sebez")

#
osszdamage = 0
for i in range(0, protosskezdo-1):
    osszdamage += data[i].fold + data[i].levego
print(f"A Terran egységek átlag damage {osszdamage/i}")

    