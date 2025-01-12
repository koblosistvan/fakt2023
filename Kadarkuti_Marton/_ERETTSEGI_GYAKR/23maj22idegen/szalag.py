IMPORT_PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/23maj22idegen/Forras/4_Szallitoszalag/szallit.txt"
#PATH2:str = "Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\23maj22idegen\\Forras\\4_Szallitoszalag\\szallit.txt"
EXPORT_PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/23maj22idegen/tomeg.txt"

HOSSZ:int = 0
IDOEGYSEG:int = 0
tmp = ""

# 1. feladat

class Rekesz:
    OSSZTOMEGEK:list[int] = []

    def __init__(self, data:list[str])->None:
        self.mikor = int(data[0])
        self.honnan = int(data[1])
        self.hova = int(data[2])
        self.tomeg = int(data[3])

        Rekesz.OSSZTOMEGEK[self.honnan] += self.tomeg
    
    def __str__(self)->str:
        return f"{self.mikor} {self.honnan} {self.hova} {self.tomeg}"
    
    def tav(self)->int:
        return (self.hova - self.honnan)%HOSSZ
    
    def vege_mikor(self)->int:
        return IDOEGYSEG*(self.tav()) + self.mikor
    
    def elhaladt_ekkor(self, ido:int)->bool:
        return self.mikor <= ido < self.vege_mikor()

rekeszek:list[Rekesz] = []

with open(IMPORT_PATH, 'r',encoding="utf-8") as f:
    tmp = f.readline().strip().split(' ')
    HOSSZ = int(tmp[0])
    IDOEGYSEG = int(tmp[1])
    Rekesz.OSSZTOMEGEK = [0]*HOSSZ
    for sor in f:
        rekeszek.append(Rekesz( sor.strip().split(' ') ))

# 2. feladat
prompt = 3#int(input("\n2. feladat:\nAdja meg, melyik adatsorra kíváncsi! ")) -1

print(f"Honnan: {rekeszek[prompt].honnan} Hova: {rekeszek[prompt].hova}")

# 3. feladat

def tav(szalaghossz:int, indulashelye:int, erkezeshelye:int)->int:
    return (erkezeshelye-indulashelye)%szalaghossz

# 4. feladat

max_tav:int = 0
max_indexek:str = []
for rekesz in rekeszek:
    if max_tav < rekesz.tav():
        max_tav = rekesz.tav()

for i in range(len(rekeszek)):
    if max_tav == rekeszek[i].tav():
        max_indexek.append(str(i+1))

print("\n4. feladat:")
print("A legnagyobb távolság:",max_tav)
print("A maximális távolságú szállítások sorszáma:",' '.join(max_indexek))


# 5. feladat

ossz_tomeg:int = 0
for rekesz in rekeszek:
    if rekesz.honnan and rekesz.hova: # egyik se 0
        ossz_tomeg += (rekesz.honnan > rekesz.hova)*rekesz.tomeg

print("A kezdőpont előtt elhaladó rekeszek össztömege:",ossz_tomeg)

# 6. feladat

sorszamok:list[int] = []
prompt = 300#int(input("\n6. feladat:\nAdja meg a kívánt időpontot! "))

for i in range(len(rekeszek)):
    if rekeszek[i].elhaladt_ekkor(prompt):
        sorszamok.append(str(i+1))

print("A szállított rekeszek halmaza:",' '.join(sorszamok))

# 7. feladat
with open(EXPORT_PATH,'w',encoding="utf-8") as x:
    for i in range(HOSSZ):
        if Rekesz.OSSZTOMEGEK[i]:
            x.write(f"{i} {Rekesz.OSSZTOMEGEK[i]}\n")