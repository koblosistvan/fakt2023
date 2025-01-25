forras = open("PigaiPéter\\érettségi\\2022oktdigi\\3_Viragagyasok\\felajanlas.txt", mode="r", encoding="utf-8")
agyasszam = int(forras.readline())
ajanlasok = []
counter = 0
for sor in forras:
    ajanlasok.append([])
    adat = sor.strip().split(" ")
    ajanlasok[counter].append(int(adat[0]))
    ajanlasok[counter].append(int(adat[1]))
    ajanlasok[counter].append(adat[2])
    counter += 1

#2
print(f"2. feladat \nA felajánlások száma: {len(ajanlasok)} ")

#3
mindektoldalon = []
for i in range(len(ajanlasok)):
    if ajanlasok[i][0] > ajanlasok[i][1]:
        mindektoldalon.append(str(i+1))
print(f"3. feladat \nA bejárat mindkét oldalán ültetők: {' '.join(mindektoldalon)}")

#4
print("4. feladat")
bekertsorszam = int(input("Adja meg az ágyás sorszámát!"))
szerepel = 0
szin = ""
osszszin = []
for i in range(len(ajanlasok)):
    if ajanlasok[i][0] <= bekertsorszam <= ajanlasok[i][1]:
        szerepel += 1
        if szin == "":
            szin = ajanlasok[i][2]
        osszszin.append(ajanlasok[i][2])
osszszin = set(osszszin)
osszszin = list(osszszin)
print(f"A felajánlók száma: {szerepel}")
if szin != "":
    print(f"A virágágyás színe, ha csak az első ültet: {szin}")
    print(f"A virágágyás színei: {' '.join(osszszin)}")
else:
    print("Ezt az ágyást nem ültetik be.")

#5
print("5. feladat ")
osszajanlottagyas = []
osszagyas = []
for i in range(1, agyasszam+1):
    osszagyas.append(i)
for i in range(len(ajanlasok)):
    for j in range(ajanlasok[i][0], ajanlasok[i][1]+1):
        osszajanlottagyas.append(j)
ajanlottagyasmennyiseg = len(osszajanlottagyas)
osszajanlottagyas = set(osszajanlottagyas)
osszajanlottagyas = list(osszajanlottagyas)
beultetheto = True
for i in range(len(osszagyas)):
    if osszagyas[i] not in osszajanlottagyas:
        beultetheto = False
if beultetheto:
    print("Minden ágyás beültetésére van jelentkező.")
else:
    if ajanlottagyasmennyiseg >= agyasszam:
        print("Átszervezéssel megoldható a beültetés.")
    else:
        print("A beültetés nem oldható meg.")

#6
szinek = open("PigaiPéter\\érettségi\\2022oktdigi\\3_Viragagyasok\\szinek.txt", mode="w", encoding="utf-8")
for i in range(0, len(osszagyas)):
    volt = False
    for j in range(len(ajanlasok)):
        if ajanlasok[j][0] <= osszagyas[i] <= ajanlasok[j][1]:
            szinek.write(f"{j+1} {ajanlasok[j][2]}\n")
            volt = True
            break
    if not volt:
        szinek.write("# 0\n")