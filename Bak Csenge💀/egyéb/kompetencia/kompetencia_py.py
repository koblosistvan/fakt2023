def fel(a):
    print(f"\n{a}. feladat")

forrás = open("okm-2023-7.csv", mode="r", encoding="UTF-8")

azon = []
matek_pont_22_23 = []
matek_pont_23_24 = []
matek_pont_vegleg_23_24 = []
matek_szint_22_23 = []
matek_szint_23_24 = []
matek_szint_vegleg_23_24 = []
szoveg_pont_22_23 = []
szoveg_pont_23_24 = []
szoveg_pont_vegleg_23_24 = []
szoveg_szint_22_23 = []
szoveg_szint_23_24 = []
szoveg_szint_vegleg_23_24 = []


for sor in list(forrás)[3:]:
    adat = sor.strip().split(";")
    azon.append(adat[2])
    matek_pont_22_23.append(int(adat[9]))
    matek_pont_23_24.append(int(adat[11]))
    matek_pont_vegleg_23_24.append((adat[13]))
    matek_szint_22_23.append(int(adat[10]))
    matek_szint_23_24.append(int(adat[12]))
    matek_szint_vegleg_23_24.append((adat[14]))
    szoveg_pont_22_23.append(int(adat[3]))
    szoveg_pont_23_24.append(int(adat[5]))
    szoveg_pont_vegleg_23_24.append((adat[7]))
    szoveg_szint_22_23.append(int(adat[4]))
    szoveg_szint_23_24.append(int(adat[6]))
    szoveg_szint_vegleg_23_24.append((adat[8]))

forrás.close()

#2.feadat
fel(2)

print(f"{len(set(azon))} diák azonosítója szerepel.")

#3. feladat
fel(3)

print(f"A legjobb szöveg pontszamu diák a(z) {azon[szoveg_szint_23_24.index(max(szoveg_szint_23_24))]} azonosítójú diák")

#4. feadat
fel(4)

szamlallo = 0

for i in range(len(azon)):
    if szoveg_pont_23_24[i] != szoveg_pont_vegleg_23_24[i]:
        szamlallo += 1

print(f"{szamlallo} diaknak valtotzott a végleges eredménye")

#5. feladat
fel(5)

valtozott_azon = []
print(f"Ellenkező irányba változó azonosítók:")
for i in range(len(azon)):
    búl1 = (szoveg_pont_22_23[i] > szoveg_pont_23_24[i]) and (matek_pont_22_23[i] < matek_pont_23_24[i])
    búl2 = (szoveg_pont_22_23[i] < szoveg_pont_23_24[i]) and (matek_pont_22_23[i] > matek_pont_23_24[i])
    if búl1 or búl2:
        valtozott_azon += azon[i]
        print(azon[i])

#6. feladat
fel(6)

for i in range(len(azon)):
    if matek_pont_22_23[i] - matek_pont_23_24[i] > 150:
        print("Volt olyan diák akinek 150-nél többet válltozott a pont matekbol")
else:
    print("Nem volt olyan diák akinek 150-nél többet válltozott a pont matekbol")

#7. feladat
fel(7)










