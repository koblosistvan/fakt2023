feladatCounter = 0
def feladat():
    global feladatCounter
    feladatCounter += 1
    print("\n" + "-" * 30 + f"\n{feladatCounter}. feladat:")
#################################################
import datetime as dt

datum = []
fertozes = []
halaleset = []

with open("covid.txt","r",encoding="utf-8") as f:
    for sor in f:
        adat = sor.strip().split(";")
        adat[0] = list(map( int,adat[0].split(".") ))
        datum.append( dt.datetime( adat[0][0],adat[0][1],adat[0][2] ))
        adat[1],adat[2] = int(adat[1]),int(adat[2])
        fertozes.append(adat[1])
        halaleset.append(adat[2])

# 1.
feladat()
print(f"Az állomány {len(datum)} nap adatait tartalmazza.")

# 2.
feladat()
print(f"A két év alatt összesen {sum(fertozes):,} fertőzöttet és {sum(halaleset):,} halottat regisztráltak.")

# 3.
feladat()
szazezerAlatt = 0
for i in fertozes:
    if i < 10**5:
        szazezerAlatt += 1
print(f"A fertőzöttek száma {szazezerAlatt} napon volt 100,000 fő alatt.")

# 4.
feladat()
negyes = halaleset.index(max(halaleset))
negyesDatetime = datum[negyes].strftime("%Y.%m.%d.")
print(f"A legtöbben {negyesDatetime} napon haltak meg:")
print(f"    {fertozes[negyes]:,} fertőzött")
print(f"    {halaleset[negyes]:,} halott")

# 5.
feladat()
maxRatio = (1,0)  # ( <arány>, <nap_index> )
for i in range(1, len(fertozes)):
    tempRatio = fertozes[i]/fertozes[i-1]
    if tempRatio > maxRatio[0]:
        maxRatio = (tempRatio, i)
otosDatetime = datum[maxRatio[1]].strftime("%Y.%m.%d.")
print(f"A legnagyobb arányú növekedés {otosDatetime} napon volt, amikor az előző napi adat {maxRatio[0]:.2f}-szorosa volt a fertőzöttek száma.")

# 6.
feladat()
novekedett = 0
csokkent = 0
for i in range(1, len(halaleset)):
    tempDifference = halaleset[i] - halaleset[i-1]
    if tempDifference == 0:
        continue
    if tempDifference > 0:
        novekedett += 1
        continue
    csokkent += 1

print(f"A halálozások száma {csokkent} napon csökkent és {novekedett} napon nőtt az előző naphoz képest.")

# 7.
feladat()
halalesetAtlag = sum(halaleset) / len(halaleset)
print(f"A napi halálozások átlagos száma {halalesetAtlag:.1f} volt.\n")

print("="*30)
