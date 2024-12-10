import statistics as st

def vonal()->None:
    print('-'*30)

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

    # shortcut a 12. feladathoz:
    def __sub__(self, other)->float:
        return self.felhasznalas - other.felhasznalas
    
    def orszag_felhasz_format(self)->list:
        return [self.orszag, self.felhasznalas]
    def orszag_kapac_format(self)->list:
        return [self.orszag, self.kapacitas]

adatsorok:list[Adatsor]= []

with open("Kadarkuti_Marton\\okolabnyom_1201\\NFA light.csv",'r',encoding="utf-8") as f:
    f.readline()
    for sor in f:
        adatsorok.append(Adatsor(sor.strip()))

# 1. feladat:
print(f"Az adatforrás {len(adatsorok)} sort tartalmaz")
vonal()

# 2. feladat:
print(f"{len([i for i in adatsorok if i.ev==2014])} országnak van adata 2014-ről.")
vonal()

# 3. feladat:
print(f"Az adatok {Adatsor.EV_MIN}-{Adatsor.EV_MAX} közötti időszakra vonatkoznak.")
vonal()

# 4. feladat:
temp = adatsorok[0]
for adat in adatsorok:
    if temp.kapacitas < adat.kapacitas:
        temp = adat

print(f"{temp.orszag} kapacitása a legnagyobb, értéke {temp.kapacitas:,} hektár.")
vonal()

# 5. feladat:
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
vonal()

# 6. feladat:
temp = [0,0,0,0] # 2000 kapacitás, 2000 felhasználás, 2014 kapacitás, 2014 felhasználás
for adat in adatsorok:
    if adat.ev == 2000:
        temp[0] += adat.kapacitas
        temp[1] += adat.felhasznalas
    elif adat.ev == 2014:
        temp[2] += adat.kapacitas
        temp[3] += adat.felhasznalas
temp = list(map(int, temp)) # kerekites
print(f"A kapacitás 2000-től 2014-ig {temp[0]:,}-ről {temp[2]:,}-re változott,\nmíg a felhasználás {temp[1]:,}-ről {temp[3]:,}-re.")

# 7. feladat:

temp.append(temp[0]/temp[1]) # 2000 arány
temp.append(temp[2]/temp[3]) # 2014 arány
if temp[4] > temp[5]:
    temp = "csökkent"
elif temp[4] < temp[5]:
    temp = "nőtt"
else: # ilyen nem lesz
    temp = "nem változott"
print(f"A két érték aránya {temp}.")
vonal()

# 8. feladat:
temp = [0,0,0,0] # össz felhasz 2000, össz lakossag 2000, össz felhasz 2014, össz lakossag 2014,
for adat in adatsorok:
    if adat.ev == 2000:
        temp[0] += adat.felhasznalas
        temp[1] += adat.lakossag
    elif adat.ev == 2014:
        temp[2] += adat.felhasznalas
        temp[3] += adat.lakossag

temp.append(temp[0]/temp[1])
temp.append(temp[2]/temp[3])
temp.append(100*temp[5]//temp[4] -100)

if temp[6] > 0:
    temp[6] = f"{temp[6]:.0f}%-os növekedést"
else:
    temp[6] = f"{abs(temp[6]):.0f}%-os csökkenést"


print(f"Az egy főre jutó átlagos felhasználás 2000-ben {temp[4]:.2f} hektár volt,\n2014-re {temp[5]:.2f}-re változott, ami {temp[6]} jelent.")
vonal()

# 9. feladat:
temp = [0,0,0,0] # össz kapacitas 2000, össz lakossag 2000, össz kapacitas 2014, össz lakossag 2014,
for adat in adatsorok:
    if adat.ev == 2000:
        temp[0] += adat.kapacitas
        temp[1] += adat.lakossag
    elif adat.ev == 2014:
        temp[2] += adat.kapacitas
        temp[3] += adat.lakossag

temp.append(temp[0]/temp[1])
temp.append(temp[2]/temp[3])
temp.append(100*temp[5]//temp[4] -100)

if temp[6] > 0:
    temp[6] = f"{temp[6]:.0f}%-os növekedést"
else:
    temp[6] = f"{abs(temp[6]):.0f}%-os csökkenést"


print(f"Az egy főre jutó átlagos kapacitás 2000-ben {temp[4]:.2f} hektár volt,\n2014-re {temp[5]:.2f}-re változott, ami {temp[6]} jelent.")
vonal()

# 10. feladat:
prompt:float = 15#prompt:float = float(input("Adj meg egy értéket hektárban: ").strip())
temp = [adat for adat in adatsorok if adat.felhasznalas/adat.lakossag > prompt] # adatsorok, amiben a felhasznalas/lakossag arany nagyobb mint prompt

print(f"Az alábbi országokban volt az egy főre jutó felhasználás {prompt} hektár fölötti: ")
for adat in temp:
    print(f"{adat.orszag} - {adat.ev}: {adat.felhasznalas/adat.lakossag:.2f} hektár")

vonal()

# 11. feladat:
temp = [] # kulonbozo orszagok (nem akartam set-ezni)

for adat in adatsorok:
    if adat.orszag not in temp:
        temp.append(adat.orszag)

print(len(temp), "ország adatai vannak az adatbázisban.")
vonal()

# 12. feladat:
temp = [0, adatsorok[1]-adatsorok[0]] # max valtozas egy orszagban ket ev kozott. az adatsor indexe es a kulonbseg lesz elmentve

for i in range(1, len(adatsorok)-1):
    if adatsorok[i].orszag == adatsorok[i+1].orszag:
        if adatsorok[i+1]-adatsorok[i] > temp[1]:
            temp = [i, adatsorok[i+1]-adatsorok[i]]
print(f"A legnagyobb növekedés a felhasználás értékében {adatsorok[temp[0]].orszag}-ban {adatsorok[temp[0]].ev}-ben történt: ")
print(f"{adatsorok[temp[0]].felhasznalas:,.0f} => {adatsorok[1+temp[0]].felhasznalas:,.0f}.")
vonal()

# 13. feladat:
# el lett irva a doksiba csak ugyanazt a sorszamozast akartam

# 14. feladat:

temp = -1 # az elso olyan adatsor indexe, ahol csokkent a felhasznalas (ha nincs akkor marad -1)
# itt gondoltam eleg 1 peldat talalni

for i in range(len(adatsorok)-1):
    if adatsorok[i+1]-adatsorok[i] < 0:
        temp = i # i lesz elmentve, de i+1 a keresett
        break

if temp == -1:
    print("Nem volt olyan ország, ahol csökkent a felhasználás.")
else:
    temp = adatsorok[temp]
    print(f"{temp.orszag} felhasználása csökkent {temp.ev} évről {1+temp.ev} évre.")
vonal()

# 15. feladat
felhasznalas_szerint = []
temp = [] # orszag-felhasznalas lesz csak mentve

for adat in adatsorok:
    temp.append(adat.orszag_felhasz_format())
temp = sorted(temp, reverse=True, key=lambda i: i[1])

for i in temp:
    if len(felhasznalas_szerint) != 10 and i[0] not in felhasznalas_szerint:
        felhasznalas_szerint.append(i[0])
felhasznalas_szerint.sort()

print("A legnagyobb felhasználók:")
print(', '.join(felhasznalas_szerint))
vonal()

# 16. feladat
kapacitas_szerint = []
temp = [] # orszag-kapacitas lesz csak mentve

for adat in adatsorok:
    temp.append(adat.orszag_kapac_format())
temp = sorted(temp, reverse=True, key=lambda i: i[1])

for i in temp:
    if len(kapacitas_szerint) != 10 and i[0] not in kapacitas_szerint:
        kapacitas_szerint.append(i[0])
kapacitas_szerint.sort()

print("A legnagyobb kapacitás:")
print(', '.join(kapacitas_szerint))
vonal()

# 17. feladat:
felhasznalas_szerint = set(felhasznalas_szerint)
kapacitas_szerint = set(kapacitas_szerint)

unio = list(felhasznalas_szerint.union(kapacitas_szerint))
metszet = list(felhasznalas_szerint.intersection(kapacitas_szerint))
unio.sort()
metszet.sort()

print("A két csoport úniója:")
print(', '.join(unio))
print("A két csoport metszete:")
print(', '.join(metszet))
vonal()

# 18. feladat:
temp = sorted([adat.felhasznalas/adat.lakossag for adat in adatsorok if adat.ev==2014])

print("A 2014-es adatok statisztikai mutatói:")
print(f"átlag:     {sum(temp)/len(temp):>16.3f} hektár")
print(f"minimum:   {temp[0]:>16.3f} hektár")
print(f"maximum:   {temp[-1]:>16.3f} hektár")
print(f"terjedelem:{max(temp)-min(temp):>16.3f} hektár")
print(f"medián:    {st.median(temp):>16.3f} hektár")
print(f"szórás:    {st.stdev(temp):>16.3f} hektár")