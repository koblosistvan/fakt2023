feladatCounter = 0
def feladat():
    global feladatCounter
    feladatCounter += 1
    print("\n" + "-" * 30 + f"\n{feladatCounter}. feladat:")
#################################################

ido = []
sebesseg = []
rendszam = []

def oraKonvert(h, m, s):
    return h*3600 + m*60 + s

print("Adatok beolvasása...")

with open("kozut.txt","r",encoding="utf-8") as f:
    f.readline()
    for sor in f:
        adat = sor.strip().split(" ")
        rendszam.append(adat[4])
        adat = list(map(int, adat[:4] ))
        ido.append(oraKonvert(adat[0], adat[1], adat[2]))
        sebesseg.append(adat[3])
print(f"A kozut.txt fájlból beolvastam {len(ido)} sort.")

# 1.
feladat()
megengedettFelett = 0
for i in sebesseg:
    if i > 50:
        megengedettFelett += 1
print(f"{megengedettFelett} autó volt gyorsabb a megengedett 50 km/h-nál.")

# 2.
feladat()
kettesVoltGyorsabb = False
for i in sebesseg:
    if i > 55:
        kettesVoltGyorsabb = True
        break
kettesVoltGyorsabb = "Volt" if kettesVoltGyorsabb else "Nem volt"
print(f"{kettesVoltGyorsabb} 55 km/h-nál gyorsabb autó.")

# 3.
feladat()
leggyorsabbIndex = 0
for i in range(len(sebesseg)):
    if sebesseg[i] > sebesseg[leggyorsabbIndex]:
        leggyorsabbIndex = i
print(f"A leggyorsabb autó rendszáma: {rendszam[leggyorsabbIndex]}, {sebesseg[leggyorsabbIndex]} km/h sebességgel ment. ")

# 4.
feladat()
atlagSebesseg = sum(sebesseg) / len(sebesseg)
print(f"Az áthaladó autók átlagsebessége {atlagSebesseg:.2f} volt.")

# 5.
feladat()
harmincAlattIndex = []
for i in range(len(sebesseg)):
    if sebesseg[i] < 30:
        harmincAlattIndex.append(i)

def oraVissza(ido):
    return str(ido//3600) + ":" + str(ido//60 % 60) + ":" + str(ido%60)

try:
    ki = open("kozut-kimenet.txt","w",encoding="utf-8")
    ki.write("")
    ki.close()
except:
    pass

try:
    with open("kozut-kimenet.txt","a",encoding="utf-8") as ki:
        for i in harmincAlattIndex:
            sor = oraVissza(ido[i]) + " - "
            sor += rendszam[i] + " - "
            sor += str(sebesseg[i]) + " km/h\n"
            ki.write(sor)
    print("kozut-kimenet.txt sikeresen legenerálva.")
    print("A fájlban a 30 km/h sebesség alatt haladó autók listája található.")
except:
    print("Hiba történt a fájl generálásakor.")

print("\n" + "="*45)