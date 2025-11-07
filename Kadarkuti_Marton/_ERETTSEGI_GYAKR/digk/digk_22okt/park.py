INPUT_PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/digk/digk_22okt/Digitalis_kultura_Forras_E2212/3_Viragagyasok/felajanlas.txt"
OUTPUT_PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/digk/digk_22okt/szinek.txt"

SOROK:int = 0
class Ajanlas:
    def __init__(self, data):
        self.elso = int(data[0])
        self.utolso = int(data[1])
        self.szin = data[2]

        self.atlog = self.elso > self.utolso
    
    def __str__(self):
        return f"{self.elso} {self.utolso} {self.szin}"
    
    def index_range(self):
        if not self.atlog:
            return list(range(self.elso, 1+self.utolso))
        else:
            return list(range(self.elso, 1+SOROK)) + list(range(1, 1+self.utolso))
    def length(self):
        return len(self.index_range())


ajanlasok:list[Ajanlas] = []
szinek = []
ultetok_sorszama = []

# 1. feladat

with open(INPUT_PATH,'r',encoding="utf-8") as f:
    SOROK = int(f.readline().strip())
    for sor in f:
        ajanlasok.append( Ajanlas( sor.strip().split(' ') ) )
szinek = [None]*SOROK
ultetok_sorszama = [None]*SOROK

# 2. feladat
print("2. feladat")
print("A felajánlások száma:",len(ajanlasok))

# 3. feladat
print("\n3. feladat")
atlog_indexek:list[str] = []
for i in range(len(ajanlasok)):
    if ajanlasok[i].atlog:
        atlog_indexek.append(str(1+i))
print("A bejárat mindkét oldalán ültetők:",', '.join(atlog_indexek))

# 4. feladat
print("\n4. feladat") # 1:több, 269:senki
prompt:int = int(input("Adja meg az ágyás sorszámát! ").strip())
felajanlok_szama:int = 0
szinek_ha_tobbet_ultet = []

for ajanlas in ajanlasok:
    if prompt in ajanlas.index_range():
        felajanlok_szama+=1

print("A felajánlók száma:",felajanlok_szama)

for i in range(len(ajanlasok)):
    for agyas in ajanlasok[i].index_range():
        if szinek[agyas -1] == None:
            szinek[agyas -1] = ajanlasok[i].szin
            ultetok_sorszama[agyas -1] = i+1
        if agyas == prompt:
            szinek_ha_tobbet_ultet.append(ajanlasok[i].szin)

if szinek[prompt-1]:
    print("A virágágyás színe, ha csak az első ültet:",szinek[prompt-1])
else:
    print("Ezt az ágyást nem ültetik be.")
    
szinek_ha_tobbet_ultet = list(set(szinek_ha_tobbet_ultet))
if None in szinek_ha_tobbet_ultet:
    szinek_ha_tobbet_ultet.remove(None)

if szinek_ha_tobbet_ultet:
    print("A virágágyás színei:",', '.join(szinek_ha_tobbet_ultet))

# 5. feladat

total_agyasok:int = 0
for ajanlas in ajanlasok:
    total_agyasok += ajanlas.length()

print("\n5. feladat")
if not szinek.count(None):
    print("Minden ágyás beültetésére van jelentkező.")
elif total_agyasok >= SOROK:
    print("Átszervezéssel megoldható a beültetés.")
else:
    print("A beültetés nem oldható meg.")

# 6. feladat
sor = ""
with open(OUTPUT_PATH,'w',encoding="utf-8") as x:
    for i in range(SOROK):
        sor = ""
        if szinek[i]:
            sor += szinek[i] + " " + str(ultetok_sorszama[i]) + '\n'
        else:
            sor = "# 0\n"
        x.write(sor)