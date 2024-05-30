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

class Kolcsonzes: # 2. feladat
    uniqueNames = set()
    uniqueNamesList = []
    def __init__(self, *args) -> None: # 3. feladat
        args = args[0]
        self.nev, self.id, self.elvitel_ora, self.elvitel_perc, self.visszahoz_ora, self.visszahoz_perc = args

        Kolcsonzes.uniqueNames.add(self.nev)
        Kolcsonzes.uniqueNamesList.append(self.nev)
    
    def get_elvitel(self):
        return f"{self.elvitel_ora}:{self.elvitel_perc}"
    def get_visszahoz(self):
        return f"{self.visszahoz_perc}:{self.visszahoz_perc}"
    
    def convert_to_sec(self):
        pass
    
    def between_interval(self,elvitel,visszahoz):
        # mindharom hh:mm alakban van
        pass


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
    for nev in range(len( Kolcsonzes.uniqueNamesList )):
        if (Kolcsonzes.uniqueNamesList[nev] == namePrompt):
            print(f"Elviteli idő: {units[nev].get_elvitel()} | Visszahozatali idő: {units[nev].get_visszahoz()}")

feladat()
allowUserInput = True
while allowUserInput:
    datePrompt = input("Adj meg egy időpontot [ÓÓ:PP] alakban: ")
