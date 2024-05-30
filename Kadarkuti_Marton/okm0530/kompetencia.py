import math
import statistics

feladatCounter = 1
def feladat():
    global feladatCounter
    feladatCounter+=1
    print("-"*30 + "\n")
    print(f"{feladatCounter}. feladat\n")

def recordFilter(lst):
    for i in range(len(lst)):
        if (lst[i]=='Nincs'):
            lst[i] = None
            continue

        if (lst[i].isdigit()):
            lst[i] = int(lst[i])
    return lst

def rtized(n):
    return round(n,1)

class Unit:
    instanceIndex = -1
    uniqueIdCount = set() # 2. feladat
    szovegertesMaxPont = [0,None] # 3. feladat
    szintek = [0]*8 # 2023/24 matematika előzetes szint

    def __init__(self, *args):
        args = args[0]
        self.evfolyam, self.tancsoport, self.id = args[:3]
        self.szoveg_tavaly_pont, self.szoveg_tavaly_szint, self.szoveg_eloz_pont, self.szoveg_eloz_szint, self.szoveg_vegso_pont, self.szoveg_vegso_szint = args[3:9]
        self.matek_tavaly_pont, self.matek_tavaly_szint, self.matek_eloz_pont, self.matek_eloz_szint, self.matek_vegso_pont, self.matek_vegso_szint = args[9:15]
        self.term_tavaly_pont, self.term_tavaly_szint, self.term_eloz_pont, self.term_eloz_szint, self.term_vegso_pont, self.term_vegso_szint = args[15:21]
        self.angol_tavaly_pont, self.angol_tavaly_szint, self.angol_eloz_pont, self.angol_eloz_szint, self.angol_vegso_pont, self.angol_vegso_szint = args[21:27]
        self.nemet_tavaly_pont, self.nemet_tavaly_szint, self.nemet_eloz_pont, self.nemet_eloz_szint, self.nemet_vegso_pont, self.nemet_vegso_szint = args[27:]

        Unit.instanceIndex += 1
        Unit.uniqueIdCount.add(self.id) # 2. feladat

        if (Unit.szovegertesMaxPont[0] < self.szoveg_eloz_pont):
            Unit.szovegertesMaxPont = [self.szoveg_eloz_pont, Unit.instanceIndex] # 3. feladat
        
        # 4. feladat
        self.szovegertes_valtozott = False
        if (self.szoveg_vegso_pont != None):
            self.szovegertes_valtozott = False if (self.szoveg_eloz_pont == self.szoveg_vegso_pont) else True

        # 5.feladat
        self.ellenkezo_irany = []
        self.ellenkezo_irany.append(self.matek_tavaly_pont > self.matek_eloz_pont)
        self.ellenkezo_irany.append(self.szoveg_tavaly_pont > self.szoveg_eloz_pont)
        self.ellenkezo_irany = not(self.ellenkezo_irany[0] and self.ellenkezo_irany[1])

        # 7. feladat
        Unit.szintek[self.matek_eloz_szint] += 1

        # 9. feladat
        self.matek_javitott_pont = self.matek_eloz_pont - self.matek_tavaly_pont # ha negativ az is valid

units = []
with open("Kadarkuti_Marton\\okm0530\\okm-2023-7.csv","r",encoding="utf-8") as f:
    for _ in range(3):
        f.readline()
    for sor in f:
        units.append( Unit( recordFilter( sor.strip().split(';') ) ) )

feladat()
print(f'{len(Unit.uniqueIdCount)} diák adatai szerepelnek a táblázatban.')

feladat()
print(f'Idén a legmagasabb szövegértés pontszámot {units[Unit.szovegertesMaxPont[1]].id} érte el.')

feladat()
print(f'{[unit.szovegertes_valtozott for unit in units].count(True)} diáknak változott a szövegértés pontszáma az előzetes eredményhez képest.')

feladat()
otosFeladat = [unit.id for unit in units if (unit.ellenkezo_irany)]
with open('Kadarkuti_Marton\\okm0530\\ellenkezo_iranyba_valtozott.txt','w',encoding="utf-8") as w:
    w.write(f'A következő {len(otosFeladat)} diák matematika és szövegértés pontszáma ellenkező irányban változott a tavalyihoz képest:\n')
    for line in range(len(otosFeladat)):
        w.write('\n' + otosFeladat[line])
    print("Az 'ellenkezo_iranyba_valtozott.txt' fájl sikeresen létre lett hozva.")

feladat()
hatosFeladat = 'Nem volt'
for unit in units:
    if (unit.matek_tavaly_pont - unit.matek_eloz_pont > 150):
        hatosFeladat = 'Volt'
        break

print(f'{hatosFeladat} olyan diák, akinek a matematika pontszáma 150+ ponttan csökkent.')

feladat()
hetesFeladatUnit = max(Unit.szintek)//12
print("- DIAGRAM -")
print("szint    darab    arány")

for i in range(len(Unit.szintek)):
    temp = Unit.szintek[i]//hetesFeladatUnit
    print("")
    print(f'{i} {Unit.szintek[i]:>10}     { ("▓"* temp) + ("░"*(12-temp)) :<5}')

feladat()
nyolcasFeladat = sorted([unit.matek_eloz_pont for unit in units])
print("2023/24 előzetes matematika pontok statisztikai jellemzői:")
print(f"• Átlag: {rtized( sum(nyolcasFeladat)/len(nyolcasFeladat)) }")
print(f"• Medián: {rtized( statistics.median(nyolcasFeladat) )}")
print(f"• Alsó kvartilis: {rtized( statistics.quantiles(nyolcasFeladat)[0] )}")
print(f"• Felső kvartilis: {rtized( statistics.quantiles(nyolcasFeladat)[2] )}")
print(f"• Szórás: {rtized( statistics.stdev(nyolcasFeladat) )}")
print(f"• Terjedelem: {max(nyolcasFeladat) - min(nyolcasFeladat)}")


feladat()
with open("javitottak.txt",'w',encoding="utf-8") as x:
    for unit in units:
        if (unit.matek_javitott_pont > 100):
            x.write(f"{unit.id}\t{unit.matek_tavaly_pont}\t{unit.matek_eloz_pont}\n")
print("A 'javitottak.txt' állomány sikeresen létrehozva.")
