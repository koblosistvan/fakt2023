PATH:str = "C:\\xampp\\htdocs\\fakt2023\\fakt2023\\Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\23maj22\\Forras\\3_Utemezes\\"
BEMENET:str = "taborok.txt"
KIMENET:str = "egytanulo.txt"

class Tabor:
    JOINED = ""
    LEGTOBB_JELENTKEZO:int = 0
    def __init__(self, data):
        self.kezd_honap:int = int(data[0])
        self.kezd_nap:int = int(data[1])
        self.veg_honap:int = int(data[2])
        self.veg_nap:int = int(data[3])
        self.diakok:str = data[4]
        self.tema:str = data[5]

        # 4. feladat
        if len(self.diakok) > Tabor.LEGTOBB_JELENTKEZO:
            Tabor.LEGTOBB_JELENTKEZO = len(self.diakok)
        
        Tabor.JOINED += self.diakok
    
    def __str__(self):
        return f"{self.kezd_honap} {self.kezd_nap} {self.veg_honap} {self.veg_nap} {self.diakok} {self.tema}"

# 1. 
taborok:list[Tabor] = []
tmp = ""

with open(PATH+BEMENET,'r',encoding="utf-8") as f:
    for sor in f:
        taborok.append( Tabor(sor.strip().split('\t')) )

print(taborok[0])

# 2. 
print("2. feladat:")
print("Az adatsorok száma:",len(taborok))
print("Az először rögzített tábor témája:",taborok[0].tema)
print("Az utoljára rögzített tábor témája:",taborok[-1].tema)

# 3. 
zenei_taborok:list[Tabor] = [i for i in taborok if i.tema == "zenei"]
if zenei_taborok:
    for tabor in zenei_taborok:
        print(f"Zenei tábor kezdődik {tabor.kezd_honap}. hó {tabor.kezd_nap}. napján.")
else:
    print("Nem volt zenei tábor.")

# 4. 
legtobb_jelentkezos_taborok:list[Tabor] = []
for tabor in taborok:
    if len(tabor.diakok) == Tabor.LEGTOBB_JELENTKEZO:
        legtobb_jelentkezos_taborok.append(tabor)
print("Legnépszerűbbek:")
for i in legtobb_jelentkezos_taborok:
    print(f"{i.kezd_honap} {i.kezd_nap} {i.tema}")

# 5.
def sorszam(honap:int, nap:int)->int:
    if honap==6: # junius
        honap = 0
    elif honap==7: # julius
        honap = 30
    else: # augusztus
        honap = 30+31
    return honap - 16 + nap + 1

# 6.
print("6. feladat:")
prompt_sorszam:int = sorszam(int(input("hó: ").strip()), int(input("nap: ").strip()))
aktiv_taborok:int = 0

for tabor in taborok:
    if sorszam(tabor.kezd_honap, tabor.kezd_nap) <= prompt_sorszam <= sorszam(tabor.veg_honap, tabor.veg_nap):
        aktiv_taborok += 1

print("Ekkor éppen",aktiv_taborok,"tábor tart.")

# 7.
print("7. feladat:")
prompt_betu:str = input("Adja meg egy tanuló betűjelét: ").strip()
erdeklodes:list[Tabor] = []

for tabor in taborok:
    if prompt_betu in tabor.diakok:
        erdeklodes.append(tabor)
erdeklodes = sorted(erdeklodes, key=lambda t: sorszam(t.kezd_honap, t.kezd_nap))

with open(PATH+KIMENET,'w',encoding="utf-8") as x:
    for tabor in erdeklodes:
        x.write(f"{tabor.kezd_honap}.{tabor.kezd_nap}-{tabor.veg_honap}.{tabor.veg_nap}. {tabor.tema}\n")

hetes_feladat_sorszamok:list[int] = []
hetes_feladat_flag:bool = False
tmp = 0

def sorszam_range(tabor:Tabor)->list[int]:
    return list(range(sorszam(tabor.kezd_honap, tabor.kezd_nap), \
                      1+sorszam(tabor.veg_honap, tabor.veg_nap)))

for tabor in erdeklodes: # minden naphoz rendel egy egyedi sorszamot
    hetes_feladat_sorszamok += sorszam_range(tabor)
for i in hetes_feladat_sorszamok:
    if hetes_feladat_sorszamok.count(i) > 1: # ha egy nap ketszer szerepel akkor nem mehet el mindegyikbe
        hetes_feladat_flag = True
        break

if hetes_feladat_flag:
    print("Nem mehet el mindegyik táborba.")
else:
    print("Mindegyik táborba elmehet.")