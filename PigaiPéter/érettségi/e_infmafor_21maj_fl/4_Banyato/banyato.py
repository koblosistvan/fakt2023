forras = open("PigaiPéter/érettségi/e_infmafor_21maj_fl/4_Banyato/melyseg.txt", mode="r", encoding="utf-8")
SOR = int(forras.readline())
OSZLOP = int(forras.readline())
sorok = []
for sor in forras:
    adat = sor.strip().split(" ")
    sorok.append([])
    for i in range(len(adat)):
        sorok[-1].append(int(adat[i]))
forras.close()

#2
print("2. feladat")
sorinput = int(input("A mérés sorának azonosítója="))
oszlopinput = int(input("A mérés oszlopának azonosítója="))
print(f"A mért mélység az adott helyen {sorok[sorinput][oszlopinput]}dm")

#3
print("3. feladat")
osszmelyseg = 0
nempart = 0
felszin = 0
for i in range(len(sorok)):
    felszin += len(sorok[i]) - sorok[i].count(0)
    for j in range(len(sorok[i])):
        if sorok[i][j] != 0:
            osszmelyseg += sorok[i][j]/10
            nempart += 1
print(f"A tó felszíne: {felszin} m2, átlagos mélysége: {osszmelyseg/nempart:.3} m")

#4
print("4. feladat")
maxmelyseg = sorok[0][0]
for i in range(len(sorok)):
    if max(sorok[i]) > maxmelyseg:
        maxmelyseg = max(sorok[i])
print(f"A tó legnagyobb mélysége: {maxmelyseg} dm")
print("A legmélyebb helyek sor-oszlop koordinátái:")
kord = []
for i in range(len(sorok)):
    for j in range(len(sorok[i])):
        if maxmelyseg == sorok[i][j]:
            kord.append(f"({i+1}; {j+1})")
print("\t".join(kord))

#5
print("5. feladat")
partvonal = 0
for i in range(len(sorok)-1):
    for j in range(len(sorok[i])-1):
        if sorok[i][j] == 0 and sorok[i][j+1] != 0 or sorok[i][j] != 0 and sorok[i][j+1] == 0:
            partvonal += 1
        if sorok[i][j] == 0 and sorok[i+1][j] != 0 or sorok[i][j] != 0 and sorok[i+1][j] == 0:
            partvonal += 1
print(f"A tó partvonala {partvonal} m hosszú")

#6
print("6. feladat")
vizsgaltoszlop = int(input("A vizsgált szelvény oszlopának azonosítója="))
diagram = open("PigaiPéter/érettségi/e_infmafor_21maj_fl/4_Banyato/diagram.txt", mode="w", encoding="utf-8")
for i in range(len(sorok)):
    diagram.write(f"{i+1:02d}{'*'*round(sorok[i][vizsgaltoszlop-1]/10)}\n")
    