def fel(a):
    print(f"\n{a}. feladat")


forrás = open("imdb.txt", mode="r", encoding="UTF-8")

megjelenes = []
idotartam = []
értékelés = []
szerző = []
bevétel = []
cím = []

forrás.readline()

for sor in forrás:
    adat = sor.strip().split("\t")
    megjelenes.append(int(adat[0]))
    idotartam.append(int(adat[1]))
    értékelés.append(float(adat[2]))
    szerző.append((adat[3]))
    bevétel.append(int(adat[4]))
    cím.append((adat[5]))

forrás.close()

#1. feladat
fel(1)
print(f"{len(megjelenes)+1} filma adatai vannak az állományban.")

#2. feladat
fel(2)
print(f"Az első film {min(megjelenes)} évben jelent meg.")

#3. feladat
fel(3)

hoszabb_filmek = str(len([i for i in idotartam if i/60 > 2])) + " film van ami hoszabb 2 óránál"
if int(hoszabb_filmek[0]) == 0:
    hoszabb_filmek = "Nincs két óránál hosszabb film."
print(f"{hoszabb_filmek}")

#4. feladat
fel(4)

for i in értékelés:
    if i > 9:
        print("Van 9-es értékelésnél jobb film.")
        break
else:
    print("Nincs 9-es értékelésnél jobb film.")

#5. feladat
fel(5)

print(f"{max(értékelés)} a maximum értékelés")

#6. feladat
fel(6)

tömb_értékelések = []

for i in range(len(értékelés)):
    if értékelés[i] not in tömb_értékelések:
        tömb_értékelések.append(értékelés[i])









