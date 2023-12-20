forrás = open("kozut.txt", mode="r", encoding="utf-8")

időpont = []
sebesség = []
rendszám = []

forrás.readline()

for sor in forrás:
    adat = sor.strip().split(" ")
    időpont.append(":".join(adat[0:3]))
    sebesség.append(int(adat[3]))
    rendszám.append(adat[4])

forrás.close()

print(f"A kozut.txt fájlból beolvastam {len(időpont)} sort.")

print("1.feladat")
gyorsabban = 0
for i in range(len(időpont)):
    if sebesség[i] > 50:
        gyorsabban += 1
print(f"{gyorsabban} autó volt gyorsabb a megengedett 50 km/h-nál.")

print("2.feladat")
gyorsabb_55 = False
for i in range(len(időpont)):
    if sebesség[i] > 55:
        gyorsabb_55 = True
        break
if gyorsabb_55 == False:
    print("Nem volt 55 km/h-nál gyorsabb autó")
else:
    print("Volt volt 55 km/h-nál gyorsabb autó")

print("3.feladat")
leggyorsabb = 0
leggyorsabb_id = 0
for i in range(len(időpont)):
    if sebesség[i] > leggyorsabb:
        leggyorsabb = sebesség[i]
        leggyorsabb_id = i
print(f"A leggyorsabb autó rendszáma: {rendszám[leggyorsabb_id]}, {sebesség[leggyorsabb_id]} km/h sebességgel ment.")

print("4.feladat")
sebesség_összes = 0
for i in range(len(időpont)):
    sebesség_összes += sebesség[i]
print(f"Az áthaladó autók átlagsebessége {sebesség_összes/len(sebesség):.2f} km/h volt.")

kimenet = open("kozut-kimenet.txt", mode="w", encoding="utf-8")

for i in range(len(időpont)):
    if sebesség[i] < 30:
        print(f"{időpont[i]} - {rendszám[i]} - {sebesség[i]}", file=kimenet)

kimenet.close()

kimenet_extra = open("kozut-rendezett.txt", mode="w", encoding="utf-8")

for i in range(len(időpont)):
    if sebesség[i] > 50:
        print(f"{időpont[i]} - {rendszám[i]} - {sebesség[i]}", file=kimenet_extra)

kimenet_extra.close()