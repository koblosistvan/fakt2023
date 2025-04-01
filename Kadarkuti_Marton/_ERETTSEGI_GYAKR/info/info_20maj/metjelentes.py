PATH = "Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\info\\info_20maj\\Informatika_forrasok_E1921\\4_Meteorologiai_jelentes\\"

class Sor:
    def __init__(self, data):
        self.varos = data[0]
        self.ora = int(data[1][:2])
        self.perc = int(data[1][2:])
        self.irany = data[2][:3]
        self.vrb = True if self.irany=="VRB" else False
        if not self.vrb:
            self.irany = int(self.irany)
        self.ero = int(data[2][3:])
        self.fok = int(data[3])
        self.szelcsend = True if "00000" == data[2] else False
    
    def __str__(self):
        if self.vrb:
            return f"{self.varos} {self.ora:02d}{self.perc:02d} VRB{self.ero:02d} {self.fok:02d}"
        else:
            return f"{self.varos} {self.ora:02d}{self.perc:02d} {self.irany:03d}{self.ero:02d} {self.fok:02d}"

    def f_ido(self):
        return f"{self.ora:02d}:{self.perc:02d}"


sorok:list[Sor] = []

# 1. 
with open(PATH + "tavirathu13.txt",'r',encoding="utf-8") as f:
    for sor in f:
        sorok.append(Sor(sor.strip().split(' ')))

# 2. 
print("2. feladat")
prompt = input("Adja meg egy település kódját! Település: ").strip()

for i in range(len(sorok)):
    if prompt == sorok[len(sorok)-i-1].varos:
        print(f"Az utolsó mérési adat a megadott településről {sorok[len(sorok)-i-1].f_ido()}-kor érkezett. ")
        break

# 3. 
print("3. feladat")
min = 0
max = 0
for i in range(len(sorok)):
    if sorok[i].fok < sorok[min].fok:
        min = i
    if sorok[i].fok > sorok[max].fok:
        max = i

print(f"A legalacsonyabb hőmérséklet: {sorok[min].varos} {sorok[min].f_ido()} {sorok[min].fok} fok.")
print(f"A legmagasabb hőmérséklet: {sorok[max].varos} {sorok[max].f_ido()} {sorok[max].fok} fok. ")

# 4. 
print("4. feladat")
szelcsendek = []
for i in range(len(sorok)):
    if sorok[i].szelcsend:
        szelcsendek.append(i)

if szelcsendek:
    for sz in szelcsendek:
        print(f"{sorok[sz].varos} {sorok[sz].f_ido()}")
else:
    print("Nem volt szélcsend a mérések idején.")

# 5. 
homero = {}

for i in sorok:
    if i.varos not in homero.keys():
        homero[i.varos] = {
            "flag":[], # ezzel lesz ellenorizve, hogy mind a 4 idokozben volt-e meres
            "ertekek":[], # ide lesznek kigyujtve az 1,7,13,19 orakor mert ertekek
            "min":100, # az ingadozas kiszamitasahoz kellenek
            "max":0,
        } 

# a.
for i in sorok:
    if i.ora in [1,7,13,19]:
        homero[i.varos]["flag"].append(i.ora)
        homero[i.varos]["ertekek"].append(i.fok)

for i in homero.keys():
    if (1 not in homero[i]["flag"]) or (7 not in homero[i]["flag"]) or (13 not in homero[i]["flag"]) or (19 not in homero[i]["flag"]):
        homero[i]["ertekek"] = "NA"
    else:
        homero[i]["ertekek"] = 'Középhőmérséklet: ' + str(round( sum(homero[i]["ertekek"])/len(homero[i]["ertekek"]) ))

# b.
for k in homero.keys():
    for s in sorok:
        if s.varos == k:
            if s.fok > homero[k]["max"]:
                homero[k]["max"] = s.fok
            if s.fok < homero[k]["min"]:
                homero[k]["min"] = s.fok
    
    print(f"{k} {homero[k]['ertekek']}; Hőmérséklet-ingadozás: {homero[k]['max']-homero[k]['min']}")

# 6. 

print("6. feladat")
for k in homero.keys():
    with open(PATH + k + ".txt",'w',encoding="utf-8") as x:
        x.write(k+'\n')
        for i in sorok:
            if i.varos == k:
                x.write(f"{i.f_ido()} {'#'*i.ero}\n")
print("A fájlok elkészültek. ")