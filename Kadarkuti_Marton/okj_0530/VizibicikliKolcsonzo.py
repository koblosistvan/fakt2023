import math

allowUserInput = True

feladatCounter = 4
def feladat():
    global feladatCounter
    feladatCounter+=1
    print('-'*30 + '\n')
    print(f"{feladatCounter}. feladat:\n")

def testForInt(lst):
    for i in range(len(lst)):
        if (lst[i].isdigit()):
            lst[i]=int(lst[i])
    return lst

def percf(n):
    if (n<10):
        return '0'+ str(n)
    return n

class Kolcsonzes: # 2. feladat
    EGYSEGAR = 2400

    uniqueNames = set()
    namesList = []
    uniqueIds = set()
    IdsList = []


    osszBevetel = 0

    def __init__(self, *args) -> None: # 3. feladat
        args = args[0]
        self.nev, self.id, self.elvitel_ora, self.elvitel_perc, self.visszahoz_ora, self.visszahoz_perc = args

        # idopont percben
        self.elvitel_min = 60*self.elvitel_ora + self.elvitel_perc
        self.visszahoz_min = 60*self.visszahoz_ora + self.visszahoz_perc

        # formazott idopont
        self.elvitelf = f"{self.elvitel_ora}:{percf(self.elvitel_perc)}"
        self.visszahozf = f"{self.visszahoz_ora}:{percf(self.visszahoz_perc)}"

        # idotartam percben
        self.idotartam = self.visszahoz_min - self.elvitel_min

        # fizetett (felorankent egysegar)
        self.fizetett = Kolcsonzes.EGYSEGAR * math.ceil(self.idotartam/30)

        Kolcsonzes.uniqueNames.add(self.nev)
        Kolcsonzes.namesList.append(self.nev)
        Kolcsonzes.uniqueIds.add(self.id)
        Kolcsonzes.IdsList.append(self.id)

        Kolcsonzes.osszBevetel += self.fizetett
    
    def get_elvitel(self) -> str:
        return self.elvitelf
    def get_visszahoz(self) -> str:
        return self.visszahozf
    
    def is_between_interval(self, zone) -> bool:
        # zone: string "hh:pp"
        zone = list(map(int, zone.strip().split(":")))
        zone = 60*zone[0] + zone[1]
        if (zone > self.elvitel_min) and (zone < self.visszahoz_min):
            return True
        else:
            return False

units = []

with open('Kadarkuti_Marton\\okj_0530\\kolcsonzesek.txt','r',encoding="utf-8") as f: # 4.feladat
    f.readline()
    for sor in f:
        units.append( Kolcsonzes( testForInt( sor.strip().split(';') ) ) )

feladat()
print(f"{len(units)} kölcsönzés szerepel az állományban.")

feladat()
while allowUserInput:
    namePrompt = input("Írj be egy nevet: ").lower().capitalize()
    if len(namePrompt) < 1:
        print("Érvénytelen bemenet.")
        continue
    allowUserInput = False

if not(namePrompt in Kolcsonzes.uniqueNames):
    print("Nincs ilyen név az állományban.")
else:
    print("Találatok a kölcsönzésre:")
    for nev in range(len( Kolcsonzes.namesList )):
        if (Kolcsonzes.namesList[nev] == namePrompt):
            print(f"Elviteli idő: {units[nev].get_elvitel()} | Visszahozatali idő: {units[nev].get_visszahoz()}")

feladat()
allowUserInput = True
while allowUserInput:
    datePrompt = input("Adj meg egy időpontot [ÓÓ:PP] alakban: ")
    if (len(datePrompt) < 1) or (datePrompt.count(':') != 1):
        continue
    allowUserInput = False

inBetweenIndexList = []
for unit in enumerate(units):
    if unit[1].is_between_interval(datePrompt):
        inBetweenIndexList.append(unit[0])

print('-'*30)
if ( len(inBetweenIndexList) > 0 ):
    for i in inBetweenIndexList:
        temp = units[i]
        print(f"JÁRMŰ: {temp.id} | NÉV: {temp.nev} | ELVITTE: {temp.elvitelf} | VISSZAHOZTA: {temp.visszahozf}")
else:
    print("Ebben az időpontban egy jármű sem volt kölcsönözve.")

feladat()
print(f"Az egész napos bevétel {Kolcsonzes.osszBevetel} Ft volt.")

feladat()
with open("F.txt",'w',encoding="utf-8") as x:
    for unit in units:
        if (unit.id == 'F'):
            x.write(f"{unit.elvitelf}-{unit.visszahozf} : {unit.nev}\n")
print("Az 'F.txt' állomány sikeresen létrehozva.")

feladat()
sortedIdSet = sorted(list(Kolcsonzes.uniqueIds))
idCounter = [0]*len(sortedIdSet)
for i in Kolcsonzes.IdsList:
    idCounter[sortedIdSet.index(i)] += 1

print("Statisztika:")
for elem in enumerate(idCounter):
    print(f"{sortedIdSet[elem[0]]} - {elem[1]}")
