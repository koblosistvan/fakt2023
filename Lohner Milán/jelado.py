forras = open('jel.txt', mode='r', encoding='utf-8')

oszlop1 = []
oszlop2 = []
oszlop3 = []
oszlop4 = []
oszlop5 = []

for sor in forras:
    adat = sor.strip().split(' ')
    oszlop1.append(int(adat[0]))
    oszlop2.append(int(adat[1]))
    oszlop3.append(int(adat[2]))
    oszlop4.append(int(adat[3]))
    oszlop5.append(int(adat[4]))

# 2.
print("2. feladat")
sorszam = int(input("Adja meg a jel sorszámát! ")) - 1
print(f"x={oszlop4[sorszam]} y={oszlop5[sorszam]}")

# 3.

def eltelt(ido1, ido2):
    ora1, perc1, mp1 = ido1
    ora2, perc2, mp2 = ido2
    return (ora2 - ora1) * 3600 + (perc2 - perc1) * 60 + (mp2 - mp1)

# 4.
print("4. feladat")
elso_ido = (oszlop1[0], oszlop2[0], oszlop3[0])
utolso_ido = (oszlop1[-1], oszlop2[-1], oszlop3[-1])
osszes_masodperc = eltelt(elso_ido, utolso_ido)
ora = osszes_masodperc // 3600
perc = (osszes_masodperc % 3600) // 60
masodperc = osszes_masodperc % 60
print(f"Időtartam: {ora}:{perc:02}:{masodperc:02}")

# 5.
min_x = min(oszlop4)
max_x = max(oszlop4)
min_y = min(oszlop5)
max_y = max(oszlop5)
print(f"Bal alsó: {min_x} {min_y}, jobb felső: {max_x} {max_y}")

# 6.
print("6. feladat")
osszeselmozdulas = 0
for i in range(len(oszlop4) - 1):
    x1, y1 = oszlop4[i], oszlop5[i]
    x2, y2 = oszlop4[i + 1], oszlop5[i + 1]
    osszeselmozdulas += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Elmozdulás: {osszeselmozdulas:.3f} egység")

# 7. feladat
print("7. feladat")
with open("kimaradt.txt", "w", encoding="utf-8") as kimaradt_fajl:
    for i in range(len(oszlop1) - 1):
        ido1 = (oszlop1[i], oszlop2[i], oszlop3[i])
        ido2 = (oszlop1[i + 1], oszlop2[i + 1], oszlop3[i + 1])
        x1, y1 = oszlop4[i], oszlop5[i]
        x2, y2 = oszlop4[i + 1], oszlop5[i + 1]

        ido_kulonbseg = eltelt(ido1, ido2)
        koordinata_kulonbseg = max((x2 - x1) // 10, (y2 - y1) // 10)

        if ido_kulonbseg > 300 or koordinata_kulonbseg > 0:
            kimaradt = max(ido_kulonbseg // 300, koordinata_kulonbseg)
            ok = "időeltérés" if ido_kulonbseg > 300 else "koordináta-eltérés"
            kimaradt_fajl.write(f"{oszlop1[i + 1]} {oszlop2[i + 1]} {oszlop3[i + 1]} {ok} {kimaradt}\n")
