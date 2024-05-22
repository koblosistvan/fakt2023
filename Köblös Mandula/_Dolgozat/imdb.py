forrás = open("imdb.txt", mode="r", encoding="utf-8")

év = []
hossz = []
értékelés = []
szerző = []
bevétel = []
cím = []

forrás.readline()

for sor in forrás:
    adat = sor.strip().split("\t")
    év.append(int(adat[0]))
    hossz.append(int(adat[1]))
    értékelés.append(adat[2])
    szerző.append(adat[3])
    bevétel.append(int(adat[4]))
    cím.append(adat[5])

forrás.close()

print("1.feladat")
print(f"Az állomány {len(év)} film adatait tartalmazza.")

print("2.feladat")
első = év[0]
for i in range(len(év)):
    if év[i] < első:
        első = év[i]
print(f"Az első film {első}. évben jelent meg.")

print("3.feladat")
hosszabb_2 = 0
for i in range(len(év)):
    if hossz[i]/60 > 2:
        hosszabb_2 += 1
if hosszabb_2 > 0:
    print(f"{hosszabb_2} két óránál hosszabb film volt.")
else:
    print(f"Nincs két óránál hosszabb film.")

print("4.feladat")
for i in range(len(év)):
    if float(értékelés[i]) > 9:
        print(f"Van 9-esnél magasabb értékelés.")
        break
    else:
        print("Nincs 9-esnél magasabb értékelés.")

print("5.feladat")
legjobb = 0
legjobb_id = 0
for i in range(len(év)):
    if float(értékelés[i]) > legjobb:
        legjobb = értékelés[legjobb]
        legjobb_id = i
print(f"Legjobb értékelés kapott film:\n{cím[legjobb_id]} ({szerző[legjobb_id]})")