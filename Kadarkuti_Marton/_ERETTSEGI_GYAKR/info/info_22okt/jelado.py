INPUT_PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_22okt/Informatika_forras_E2212/4_Jelado/jel.txt"
OUTPUT_PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_22okt/kimaradt.txt"


def ido_format(t:int)->str:
    return f"{t//3600}:{t//60%60}:{t%60}"

class Jel:
    def __init__(self, data) -> None:
        self.ora = int(data[0])
        self.perc = int(data[1])
        self.mp = int(data[2])
        self.x = int(data[3])
        self.y = int(data[4])
    def __str__(self) -> str:
        return f"{self.ora} {self.perc} {self.mp} {self.x} {self.y}"
    
    def get_mp(self)->int:
        return self.ora*3600 + self.perc*60 + self.mp
    def elso_harom_arg(self)->str:
        return f"{self.ora} {self.perc} {self.mp}"

    def tavolsag(self,other)->float:
        return pow((self.x-other.x)**2 + (self.y-other.y)**2,0.5)
    def eltelt(self,other)->float:
        return self.get_mp() - other.get_mp()

# 1.
jelek:list[Jel] = []
with open(INPUT_PATH, 'r', encoding="utf-8") as f:
    for sor in f:
        jelek.append( Jel(sor.strip().split(' ')) )

# 2.
print("2. feladat")
prompt:int = int(input("Adja meg a jel sorszámát! ").strip())
prompt -= 1
print(f"x={jelek[prompt].x} y={jelek[prompt].y}")

# 3.
def eltelt(jel1:Jel, jel2:Jel)->int:
    return jel1.get_mp() - jel2.get_mp() # direkt lehet negativ

# 4.
print("\n4. feladat")
print("Időtartam:", ido_format( eltelt(jelek[-1], jelek[0])) )

# 5.
print("\n5. feladat")
min_xy = [10000,10000]
max_xy = [-10000,-10000]

for jel in jelek:
    if jel.x < min_xy[0]:
        min_xy[0] = jel.x
    elif jel.x > max_xy[0]:
        max_xy[0] = jel.x
    
    if jel.y < min_xy[1]:
        min_xy[1] = jel.y
    elif jel.y > max_xy[1]:
        max_xy[1] = jel.y

min_xy = map(str, min_xy)
max_xy = map(str, max_xy)

print(f"Bal alsó: {' '.join(min_xy)}, jobb felső: {' '.join(max_xy)}")

# 6.
print("\n6. feladat")
total_tavolsag:float = 0

for i in range(len(jelek) -1):
    total_tavolsag += jelek[i].tavolsag(jelek[i+1])

print(f"Elmozdulás: {total_tavolsag:.3f} egység")

# 7.
kimaradt:list[list] = []
ido_elter:bool = False
koord_elter:bool = False
ido_diff:int = 0
koord_diff:int = [0, 0, 000] # x, y, a harmadik szam az, hogy legalabb hanyszor 10 egyseget mozdult
# struktura:
# [ [index:int, tipus:str, legalabb:int], [index:int, tipus:str, legalabb:int], ... ]
# tipus: 'i':idő; 'k':koordinata

for i in range(1, len(jelek) ):
    ido_elter = False
    koord_elter = False

    # hanyszor 5 perccel lepte tovabb, kiveve ha oszthato 5-tel, mert akkor az eggyel kevesebbet veszi
    ido_diff = jelek[i].eltelt(jelek[i-1])
    if ido_diff <= 300:
        ido_diff = 0
    else:
        ido_diff = ido_diff // 300

    # koordinata kulonbsegek x es y-ra bontva
    koord_diff[0] = abs( jelek[i].x - jelek[i-1].x )
    koord_diff[1] = abs( jelek[i].y - jelek[i-1].y )
    if koord_diff[0]>10 or koord_diff[1]>10:
        koord_elter = True
        # hanyszor 10 egyseggel lepte tovabb, kiveve ha oszthato 10-zel, mert akkor az eggyel kevesebbet veszi
        if koord_diff[0]>=koord_diff[1]:
                koord_diff[2] = koord_diff[0]-1
        else:
                koord_diff[2] = koord_diff[1]-1
        koord_diff[2] = koord_diff[2]//10

    if ido_diff > 0: # legalabb 1x nagyobb mint 300
        ido_elter = True
    
    if not (ido_elter+koord_elter): # ha egyik se teljesul akkor kovetkezo
        continue
    else:
        # indexkorrekcio
        ido_diff -= 1
        #print(i,':',ido_diff, koord_diff)
    
    if ido_elter and not koord_elter: # idoelteres
        kimaradt.append([i,'i',ido_diff])
    elif koord_elter and not ido_elter: # koord-elteres
        kimaradt.append([i,'k',koord_diff[2]])
    else: # mindketto elter, akkor komparalja
        if koord_diff[2]>=ido_diff: # az lesz, amelyik nagyobb (ha egyenlo, akkor a koord lesz mert barmelyik lehet)
            kimaradt.append([i,'k',koord_diff[2]])
        else:
            kimaradt.append([i,'i',ido_diff])

# kiiras a fajlba
teljes_szovegek = {
    "i":"időeltérés",
    "k":"koordináta-eltérés",
}

with open(OUTPUT_PATH,'w',encoding="utf-8") as x:
    for i in kimaradt:
        x.write(f"{jelek[i[0]].elso_harom_arg()} {teljes_szovegek[i[1]]} {i[2]}\n")
