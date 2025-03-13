PATH = ""

class Sor:
    def __init__(self, data)->None:
        self.id = data[0]
        self.ora = int(data[1].split(':')[0])
        self.perc = int(data[1].split(':')[1])
        self.tipus = int(data[2])
    
    def __str__(self) -> str:
        return f"{self.id} {self.ora:02d}:{self.perc:02d} {self.tipus}"
    
    def f_ido(self)->str:
        return f"{self.ora:02d}:{self.perc:02d}"
    
    def ido(self)->int:
        return self.perc + 60*self.ora

# 1. 

sorok:list[Sor] = []

with open(PATH+"bedat.txt",'r',encoding="utf-8") as f:
    for i in f:
        sorok.append( Sor( i.strip().split(' ') ) )

# 2. 

print("2. feladat")

# a feladatban le van irva, hogy az elso egy belepes es az utolso egy kilepes
print(f"Az első tanuló {sorok[0].f_ido()}-kor lépett be a főkapun.")
print(f"Az utolsó tanuló {sorok[-1].f_ido()}-kor lépett ki a főkapun.")

# 3. 

with open(PATH + "kesok.txt",'w',encoding="utf-8") as kesok:
    for s in sorok:
        if s.tipus == 1 and (7*60+50) < s.ido() <= (8*60+15):
            kesok.write(f"{s.f_ido()} {s.id}\n")

# 4. 
print("4. feladat")
print(f"A menzán aznap {len([True for i in sorok if i.tipus==3])} tanuló ebédelt.")

# 5. 
kolcson_ctr = 0
koncsonzott_id = []

for s in sorok:
    if s.tipus==4 and s.id not in koncsonzott_id:
        kolcson_ctr += 1
        koncsonzott_id.append(s.id)
print("5. feladat")
print(f"Aznap {kolcson_ctr} tanuló kölcsönzött a könyvtárban.")

if kolcson_ctr > len([True for i in sorok if i.tipus==3]):
    print("Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")

# 6. 

volt_szunet_elott = [s.id for s in sorok if s.tipus == 1 and s.ido() < (10*60+45)]
szabalyosan_lepett_ki = [s.id for s in sorok if s.tipus == 2 and (10*60+45) <= s.ido() <= (11*60)]
erintett_tanulok = []

for s in sorok:
    if (10*60+50) < s.ido() < (11*60) and (s.tipus == 1) and (s.id in volt_szunet_elott) and (s.id not in szabalyosan_lepett_ki):
        erintett_tanulok.append(s.id)
print("6. feladat")
print("Az érintett tanulók:")
print(' '.join(erintett_tanulok))

# 7. 
print("7. feladat")
prompt = input("Egy tanuló azonosítója=").strip()

# ido percben
elso_belepes = 0
utolso_kilepes = 0
idokoz = 0

for s in sorok:
    if s.id == prompt and s.tipus == 1:
        elso_belepes = s.ido()
        break

if elso_belepes: # ha ez nem 0, csak akkor van ertelme folytatni
    
    for s in sorok[::-1]: # array reverse shorthand
        if s.id == prompt and s.tipus == 2:
            utolso_kilepes = s.ido()
            break
    
    idokoz = utolso_kilepes-elso_belepes
    print(f"A tanuló érkezése és távozása között {idokoz//60} óra {idokoz%60} perc telt el.")

else:
    print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")