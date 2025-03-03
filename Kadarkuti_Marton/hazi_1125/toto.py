import random

# 2. feladat
nevek_be = input("Adja meg a két csapat nevét! ").split('-')

# 3. feladat
eredmeny_be = list(map(int, input("Adja meg az eredményt! ").split(':')))

# 4. feladat
def x12(gól1:int, gól2:int)->str:
    if gól1 > gól2:
        return '1'
    else:
        if gól2 > gól1:
            return '2'
        else:
            return 'X'
        
# 5. feladat
CSAPATNEVEK = [sor.strip() for sor in open("Kadarkuti_Marton\\hazi_1125\\csapatnevek.txt",'r',encoding="utf-8")]

# 6. feladat
meccsek = []

class Meccs:
    SORSZAM = 0
    LEGNAGYOBB_KULONBSEG = [0,0] # [ertek, sorszam]
    NULLAS_MERKOZESEK = [] # sorszamok listaja

    def __init__(self, csapat1:str, csapat2:str, gol1:int=-1, gol2:int=-1)->None:
        Meccs.SORSZAM += 1

        # csapatnevek
        self.csapat1 = csapat1
        self.csapat2 = csapat2

        # eredmenyek (manualisan is megadhato)
        if gol1 == -1:
            self.gol1 = random.randint(0,5)
        else:
            self.gol1 = gol1
        
        if gol2 == -1:
            self.gol2 = random.randint(0,5)
        else:
            self.gol2 = gol2
        
        # gyoztes (1,2,X) es a sorszam (1,2,...,7,+1)
        self.gyoztes = x12(self.gol1, self.gol2)
        self.sorszam = str(Meccs.SORSZAM) if Meccs.SORSZAM != 8 else "+1"

        # legnagyobb kulonbseg feladat (8a)
        self.kulonbseg = abs(self.gol1-self.gol2)
        if self.kulonbseg > Meccs.LEGNAGYOBB_KULONBSEG[0]:
            Meccs.LEGNAGYOBB_KULONBSEG = [self.kulonbseg, self.sorszam]
        
        # 0:0 merkozes feladat (8b)
        if not self.gol1+self.gol2:
            Meccs.NULLAS_MERKOZESEK.append(self.sorszam)




    def get_str(self)->str:
        return f"{self.csapat1} - {self.csapat2} {self.gol1}:{self.gol2} {self.gyoztes}"
    
    def get_gyoztes(self)->str:
        if self.gyoztes == '1':
            return self.csapat1
        elif self.gyoztes == '2':
            return self.csapat2
        else:
            return "Döntetlen"
    
    def __str__(self)->str:
        return self.get_str()

    

# randomizalni a csapatokat, mindegyik csak egyszer szerepelhet
csapatok_sorrend = [i for i in range(14)]
random.shuffle(csapatok_sorrend)

for i in range(7):
    print(i,13-i)
    meccsek.append(Meccs(CSAPATNEVEK[csapatok_sorrend[i]], CSAPATNEVEK[csapatok_sorrend[13-i]]))

meccsek.append( Meccs(nevek_be[0], nevek_be[1], eredmeny_be[0], eredmeny_be[1]) )

# 7. feladat
szelveny = open("Kadarkuti_Marton\\hazi_1125\\szelveny.txt",'w',encoding="utf-8")

szelveny.write("Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:")
print("Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:")

for meccs in meccsek:
    szelveny.write('\n')
    szelveny.write(meccs.get_str())
    print(meccs)

# 8a. feladat

print("\nLegnagyobb gólkülönbségű mérkőzések: ", Meccs.LEGNAGYOBB_KULONBSEG[1])

# 8b. feladat

if not Meccs.NULLAS_MERKOZESEK:
    print("\nNem volt 0:0 mérkőzés.")
else:
    print("\n0:0-ás mérkőzések: ", ", ".join(Meccs.NULLAS_MERKOZESEK))

# 9. feladat
legalabb_ketto = []

for meccs in meccsek:
    if meccs.kulonbseg >= 2:
        legalabb_ketto.append(meccs.get_gyoztes())

if not legalabb_ketto:
    print("\nNem volt legalább két gólos győzelem.")
else:
    print("\nLegalább két góllal nyertek: ", ", ".join(legalabb_ketto))