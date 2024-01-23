forrás = open("kozut.txt", "r", encoding="utf-8")

adatsor_száma = forrás.readline()

óra = []
perc = []
mp = []
kmperh = []
rendszám = []

for sor in forrás:
    adat = sor.strip().split(" ")
    óra.append(int(adat[0]))
    perc.append(int(adat[1]))
    mp.append(int(adat[2]))
    kmperh.append(int(adat[3]))
    rendszám.append(adat[4])

forrás.close()


#1. feladat

print(f"{len([i for i in kmperh if i > 50])} autó volt gyorsabb a megengedett 50 km/h-nál.")


#2. feladat

voltnemvolt = ""

for i in range(len(kmperh)):
    if kmperh[i] > 55:
        voltnemvolt = "Volt"
        break
else:
    voltnemvolt = "Nem volt"

print(f"{voltnemvolt} 55 km/h-nál gyorsabb autó.")


print(f"A leggyorsabb autó rendszáma: {rendszám[kmperh.index(max(kmperh))]}, {max(kmperh)} km/h sebességgel ment.")


print(f"Az áthaladó autók átlagsebessége {round(sum([i for i in kmperh])/len(kmperh), 2)} km/h volt.")


kimenet = open("kozut-rendezett.txt", "w", encoding="UTF-8")

for i in range(len(rendszám)):
    if kmperh[i] < 30:
        print(f"{óra[i]}:{perc[i]}:{mp[i]} {rendszám[i]} {kmperh[i]} km/h", file=kimenet)







