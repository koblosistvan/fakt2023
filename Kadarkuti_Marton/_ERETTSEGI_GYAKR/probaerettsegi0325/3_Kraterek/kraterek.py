from math import sqrt as gyok

class Krater:
    def __init__(self, data) -> None:
        self.x = float(data[0])
        self.y = float(data[1])
        self.r = float(data[2])
        self.nev = data[3]
    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.r} {self.nev}"
    
    def tav(self, other)->float:
        return tavolsag(self.x, self.y, other.x, other.y)
    def sugarak_osszege(self,other)->float:
        return self.r+other.r
    
    def tartalmazza(self,other)->bool:
        if self.r <= other.r:
            return False
        return True if (self.tav(other) < abs(self.r-other.r)) else False

kraterek:list[Krater] = []

# 1. 
with open("felszin_tpont.txt",'r',encoding="utf-8") as f:
    for i in f:
        kraterek.append(Krater(i.strip().split('\t')))
l = len(kraterek)

# 2. 
print("2. feladat")
print("A kráterek száma:",l)

# 3.
print("3. feladat")
prompt = input("Kérem egy kráter nevét: ").strip()

if prompt in [i.nev for i in kraterek]:
    prompt = [i for i in kraterek if i.nev == prompt][0]
    print(f"A(z) {prompt.nev} középpontja X={prompt.x} Y={prompt.y} sugara R={prompt.r}.")
else:
    print("Nincs ilyen nevű kráter.")

# 4.
legnagyobb_sugar_index = 0
for k in range(l):
    if kraterek[k].r > kraterek[legnagyobb_sugar_index].r:
        legnagyobb_sugar_index = k

print("4. feladat")
print(f"A legnagyobb kráter neve és sugara: {kraterek[legnagyobb_sugar_index].nev} {kraterek[legnagyobb_sugar_index].r}")

# 5. 
def tavolsag(x1:float, y1:float, x2:float, y2:float)->float:
    tavolsag = gyok( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )

    return tavolsag

# 6. 
print("6. feladat")
prompt = input("Kérem egy kráter nevét: ").strip()

if prompt in [i.nev for i in kraterek]:
    prompt = [i for i in kraterek if i.nev == prompt][0]

    hatos_feladat_nevek = []
    for k in kraterek:
        if prompt.tav(k) > prompt.sugarak_osszege(k):
            hatos_feladat_nevek.append(k.nev)
    if hatos_feladat_nevek:
        print("Nincs közös része: ",", ".join(hatos_feladat_nevek),'.',sep='')

# 7. 
tartalmaz_indexek = [] # az indexeket menti el egy-egy listaba az alapjan, hogy az adott indexu krater melyik masikakat tartalmazza
for k in kraterek:
    tartalmaz_indexek.append([])

for i in range(l):
    for j in range(l):
        if kraterek[i].tartalmazza(kraterek[j]):
            tartalmaz_indexek[i].append(j)

print("7. feladat")

kiirt_szamparok = []
for i in range(l):
    for j in tartalmaz_indexek[i]:
        if {i,j} not in kiirt_szamparok:
            kiirt_szamparok.append({i,j})
            print(f"A(z) {kraterek[i].nev} kráter tartalmazza a(z) {kraterek[j].nev} krátert.")

# 8. 
with open("terulet.txt",'w',encoding="utf-8") as x:
    for k in kraterek:
        
        x.write(f"{round(k.r*k.r*3.14, 2)}\t{k.nev}\n")