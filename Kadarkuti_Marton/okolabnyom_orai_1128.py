
class Adatsor:
    EV_MAX:int = 0
    EV_MIN:int = 3000

    def __init__(self, adatsor) -> None:
        self.eredeti = adatsor
        adatsor = adatsor.split(',')

        self.kod = adatsor[0]
        self.orszag = adatsor[1]
        self.regio = adatsor[2]
        self.ev = int(adatsor[3])
        self.felhasznalas = float(adatsor[4])
        self.kapacitas = float(adatsor[5])
        self.lakossag = float(adatsor[6])
        self.gdp = None if adatsor[7]=="None" else float(adatsor[7])

        # aggregacio
        if Adatsor.EV_MAX < self.ev:
            Adatsor.EV_MAX = self.ev
        if Adatsor.EV_MIN > self.ev:
            Adatsor.EV_MIN = self.ev
    
    def __str__(self) -> str:
        return self.eredeti

adatsorok:list[Adatsor]= []

with open("okolabnyom\\NFA light.csv",'r',encoding="utf-8") as f:
    f.readline()
    for sor in f:
        adatsorok.append(Adatsor(sor.strip()))

# alap1:
print(f"Az adatforrás {len(adatsorok)} sort tartalmaz")

# alap2:
print(f"{len([i for i in adatsorok if i.ev==2014])} országnak van adata 2014-ről.")

# alap3:
print(f"Az adatok {Adatsor.EV_MIN}-{Adatsor.EV_MAX} közötti időszakra vonatkoznak.")

# alap4:
temp = adatsorok[0]
for adat in adatsorok:
    if temp.kapacitas < adat.kapacitas:
        temp = adat

print(f"{temp.orszag} kapacitása a legnagyobb, értéke {temp.kapacitas} hektár.")

# alap5:
temp = adatsorok[0]

# megkeresi az elsot ami nem none
if temp.gdp == None:
    for adat in adatsorok:
        if adat.gdp:
            temp = adat
            break

# megkeresi a min gdp-t
for adat in adatsorok:
    if adat.gdp:
        if adat.gdp < temp.gdp:
            temp = adat
print(f"A legkisebb egy főre jutó GDP-je {temp.orszag}-nak volt {temp.ev} évben. Értéke: {temp.gdp} USD/fő")

# alap6:
temp = [0,0,0,0] # 2000 kapacitás, 2000 felhasználás, 2014 kapacitás, 2014 felhasználás
for adat in adatsorok:
    if adat.ev == 2000:
        temp[0] += adat.kapacitas
        temp[1] += adat.felhasznalas
    elif adat.ev == 2014:
        temp[2] += adat.kapacitas
        temp[3] += adat.felhasznalas
temp = list(map(int, temp)) # kerekites
print(f"\nA kapacitás 2000-től 2014-ig {temp[0]}-ről {temp[2]}-re változott,\nmíg a felhasználás {temp[1]}-ről {temp[3]}-re.")

# alap7:

temp.append(temp[0]/temp[1]) # 2000 arány
temp.append(temp[2]/temp[3]) # 2014 arány
if temp[4] > temp[5]:
    temp = "csökkent"
elif temp[4] < temp[5]:
    temp = "nőtt"
else: # ilyen nem lesz
    temp = "nem változott"
print(f"A két érték aránya {temp}.\n")

# alap8:
temp = [0,0,0,0] # össz felhasználás, össz lakossag; 2000-re és 2014-re
for adat in adatsorok:
    if adat.ev == 2000:
        temp[0] += adat.felhasznalas
        temp[1] += adat.lakossag
    elif adat.ev == 2014:
        temp[2] += adat.felhasznalas
        temp[3] += adat.lakossag

temp.append(temp[0]/temp[1])
temp.append(temp[2]/temp[3])
temp.append(100*temp[4]/temp[5])


print(f"Az egy főre jutó átlagos felhasználás 2014-ben {temp[4]} hektár volt,\n2014-re {temp[5]}-re változott, ami {temp[6]}%-os változást jelent.")
