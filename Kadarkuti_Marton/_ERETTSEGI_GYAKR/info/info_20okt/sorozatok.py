import datetime as dt
INPUT_PATH:str = "Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\info\\info_20okt\\Informatika_emelt_gyakorlati_forrasok_1811\\4_Sorozatok\\lista.txt"
OUTPUT_PATH:str = "Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\info\\info_20okt\\summa.txt"

class Sor:
    IDO = 0
    def __init__(self, data):
        self.datum = data[0] if data[0]!="Ni" else "" # bool("") false erteket ad
        self.cim = data[1]
        self.evad = int(data[2].split('x')[0])
        self.epizod = int(data[2].split('x')[1])
        self.ido = int(data[3])
        self.latta = bool(int(data[4]))

        Sor.IDO += self.ido*self.latta

    def get_dt(self):
        t = self.datum.split('.')
        return dt.datetime(int(t[0]), int(t[1]), int(t[2]))
    
    def get_hetnapja(self):
        t = self.datum.split('.')
        return Hetnapja(int(t[0]), int(t[1]), int(t[2]))
    
    def __str__(self):
        return f"{self.datum} {self.cim} {self.evad}x{self.epizod} {self.ido} {self.latta}"
sorok:list[Sor] = []

# 1. 
sor = ""
adat = ""
f = open(INPUT_PATH,'r',encoding="utf-8")
for i in range(400*5):
    if not i%5 and i:
        sorok.append( Sor(adat.strip().split('\n')) )
        adat = ""
    sor = f.readline()
    if not sor:
        break
    adat += sor
f.close()

# 2.
print("2. feladat")
print(f"A listában {len([1 for i in sorok if i.datum != 'NI'])} db vetítési dátummal rendelkező epizód van.\n")

# 3. 
arany = 100*len([1 for i in sorok if i.latta])/len(sorok)
arany = round(arany, 2)
arany = str(arany).replace('.',',') + '%'
print("3. feladat")
print(f"A listában lévő epizódok {arany}-át látta.\n")

# 4. 
print("4. feladat")
print(f"Sorozatnézéssel {Sor.IDO//(60*24)} napot {(Sor.IDO//60)%24} órát és {Sor.IDO%60} percet töltött.\n")

# 5. 
print("5. feladat")
prompt = input("Adjon meg egy dátumot! Dátum= ").strip()
prompt = prompt.split('.')
prompt = dt.datetime(int(prompt[0]), int(prompt[1]), int(prompt[2]))

for s in sorok:
    if s.datum == "NI" or s.latta:
        continue
    if s.get_dt() <= prompt:
        print(f"{s.evad}x{s.epizod:02d}\t{s.cim}")

# 6. 
def Hetnapja(ev:int, ho:int, nap:int) -> str:
    napok:list[str] = ["v","h","k","sze","cs","p","szo"]
    honapok:list[int] = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    ev -= ho<3

    return napok[(ev + ev//4 - ev//100 + ev//400 + honapok[ho-1] + nap) % 7]

# 7. 
print("\n7. feladat")
prompt = input("Adja meg a hét egy napját (például cs)! Nap= ").strip().lower()

hetes_fela = []
for s in sorok:
    if s.datum == "NI":
        continue
    if prompt == s.get_hetnapja():
        if s.cim not in hetes_fela:
            hetes_fela.append(s.cim)
            print(s.cim)

if not hetes_fela:
    print("Az adott napon nem kerül adásba sorozat.")

# 8. 
sorozatok_data = {}
for s in sorok:
    if s.cim not in sorozatok_data.keys():
        sorozatok_data[s.cim] = [0,0]
    sorozatok_data[s.cim][0] += s.ido
    sorozatok_data[s.cim][1] += 1

with open(OUTPUT_PATH,'w',encoding="utf-8") as x:
    for i in sorozatok_data.keys():
        x.write(f"{i} {sorozatok_data[i][0]} {sorozatok_data[i][1]}\n")