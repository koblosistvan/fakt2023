forras = open("bedat.txt", mode="r", encoding="utf-8")
kod = []
idopont = []
tipus = []
for sor in forras:
    adat = sor.strip().split(" ")
    kod.append(adat[0])
    idopont.append(adat[1])
    tipus.append(int(adat[2]))
forras.close()

def ido(b):
    a = b.split(":")
    a = int(a[1]) + int(a[0])*60
    return a
#2
print("2. feladat")
print(f"Az első tanuló {idopont[0]}-kor lépett be a főkapun.")
print(f"Az utolsó tanuló {idopont[-1]}-kor lépett ki a főkapun.")

#3
output = open("kesok.txt", mode="w", encoding="utf-8")
kesok = []
for i in range(len(idopont)):
    perc = ido(idopont[i])
    if 50 + 7 * 60 < perc <= 8 * 60 + 15:
        kesok.append(" ".join([idopont[i], kod[i]]))
output.write("\n".join(kesok))

#4
print("4. feladat")
print(f"A menzán aznap {tipus.count(3)} tanuló ebédelt.")

#5
print("5.feladat")
kolcsonzesek = 0
megvolt = []
for i in range(len(tipus)):
    if tipus[i] == 4 and kod[i] not in megvolt:
        kolcsonzesek += 1
        megvolt.append(kod[i])
print(f"Aznap {kolcsonzesek} tanuló kölcsönzött a könyvtárból.")
if tipus.count(3) < kolcsonzesek:
    print("Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")

#6
print("6. feladat")
print("Az érintett tanulók")
erintett = []
for i in range(len(kod)):
    belep = 0
    belepelso = "0:0"
    kilep = 0
    if 10*60 + 50 <= ido(idopont[i]) <= 11*60:
        for j in range(len(kod)):
            if 10*60 + 50 <= ido(idopont[j]) <= 11*60:
                if kod[i] == kod[j]:
                    if tipus[j] == 1:
                        belep += 1
                    elif tipus == 2:
                        kilep[j] += 1
    for j in range(len(kod)):
        if kod[i] == kod[j]:
            if tipus[j] == 1 and belepelso == "0:0":
                 belepelso = idopont[j]
    if belep != kilep and (10*60 + 50 >= ido(belepelso) or ido(belepelso) >= 11*60) :
        erintett.append(kod[i])
print(erintett)
#7
print("7.feladat")
bekert = input("Egy tanuló azonosítója:")
volt = False
erkezes = ""
tavozas = ""
for i in range(len(idopont)):
    if kod[i] == bekert:
        if tipus[i] == 1 and erkezes == "":
            erkezes = idopont[i]
        elif tipus[i] == 2:
            tavozas = idopont[i]
        volt = True
if volt:
    eltelt = ido(tavozas)-ido(erkezes)
    print(f"A tanuló érkezése és távozása között {eltelt//60} óra {eltelt%60} perc telt el.")
else:
    print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")