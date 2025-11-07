PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_22maj/Informatika_forras_E2211/4_Epitmenyado/"

AR = {
    "A":0,
    "B":0,
    "C":0,
}

class Epitmeny:

    INSTANCEK = {
        "A":0,
        "B":0,
        "C":0,
    }

    def __init__(self, data):
        self.adoszam = data[0]
        self.utca = data[1]
        self.hazszam = data[2]
        self.sav = data[3]
        self.terulet = int(data[4])

        Epitmeny.INSTANCEK[self.sav] += 1

    def __str__(self):
        return f"{self.adoszam} {self.utca} {self.hazszam} {self.sav} {self.terulet}"

epitmenyek:list[Epitmeny] = []

# 1. 
with open(PATH + "utca.txt",'r',encoding="utf-8") as f:
    tmp = f.readline().split(' ')
    AR["A"] = int(tmp[0])
    AR["B"] = int(tmp[1])
    AR["C"] = int(tmp[2])
    
    for sor in f:
        epitmenyek.append(Epitmeny(sor.strip().split(' ')))

# 2. 
print(f"2. feladat. A mintában {len(epitmenyek)} telek szerepel.")

# 3. 
tmp = []
prompt = input("3. feladat. Egy tulajdonos adószáma: ") # 68396
tmp = [f"{i.utca} utca {i.hazszam}" for i in epitmenyek if i.adoszam == prompt]

if tmp:
    print('\n'.join(tmp))
else:
    print("Nem szerepel az adatállományban.")

# 4. 
def ado(adosav, alapterulet):
    osszeg = AR[adosav]*alapterulet
    if osszeg<10000:
        return 0
    else:
        return osszeg
    
# 5. 
osszegek = {
    "A":0,
    "B":0,
    "C":0,
}

for e in epitmenyek:
    osszegek[e.sav] += ado(e.sav, e.terulet)

for i in ["A","B","C"]:
    print(f"A sávba {Epitmeny.INSTANCEK[i]} telek esik, az adó {osszegek[i]} Ft. ")

# 6. 
hatos_fela_utcak = []
for i in range(len(epitmenyek)-1):
    tmp = epitmenyek[i]
    if (tmp.utca == epitmenyek[i+1].utca) and (tmp.sav != epitmenyek[i+1].sav):
        if tmp.utca not in hatos_fela_utcak:
            hatos_fela_utcak.append(tmp.utca)

print("6. feladat. A több sávba sorolt utcák:")
print('\n'.join(hatos_fela_utcak))

# 7. 

fizetendo = {}
for e in epitmenyek:
    fizetendo[e.adoszam] = 0
for e in epitmenyek:
    fizetendo[e.adoszam] += ado(e.sav, e.terulet)

with open(PATH + "fizetendo.txt",'w',encoding="utf-8") as x:
    for i in fizetendo.keys():
        x.write(f"{i} {fizetendo[i]}\n")