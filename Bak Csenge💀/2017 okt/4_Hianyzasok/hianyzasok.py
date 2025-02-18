def fel(x):
    print(f"{x}. feladat")

forrás = open("naplo.txt", mode="r", encoding="utf-8")

dátum = []
név = []
hiányzás = []
aktuális_dátum = "0000"

for sor in forrás:
    adat = sor.strip().split(" ")
    if adat[0] == "#":
        aktuális_dátum = adat[1] + adat[2]
    else:
        dátum.append(aktuális_dátum)
        név.append(adat[0] + " " + adat[1])
        hiányzás.append(adat[2])

#2. feladat
fel(2)

valami = []
másik_változo = set(valami)

















