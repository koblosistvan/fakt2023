feladat_ctr:int = 0
def feladat()->None:
    global feladat_ctr
    feladat_ctr += 1
    print('\n',feladat_ctr,". feladat:",sep='')

FORRAS_PATH:str = "Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\23okt25info\\Forras\\4_Tarsas\\"
HOME_PATH:str = "Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\23okt25info\\" # lud.py mappaja

# 1
feladat_ctr += 1

dobasok:list[int] = []
osvenyek:list[str] = []

with open(FORRAS_PATH+"dobasok.txt",'r',encoding="utf-8") as f:
    dobasok = list(map(int, f.readline().strip().split(' ')))
osvenyek = [sor.strip() for sor in open(FORRAS_PATH+"osvenyek.txt")]

# 2
feladat()
print("A dobások száma:",len(dobasok))
print("Az ösvények száma:",len(osvenyek))

# 3
feladat()
legh_osveny_index = 0
for i in range(len(osvenyek)):
    if len(osvenyek[i]) > len(osvenyek[legh_osveny_index]):
        legh_osveny_index = i
print(f"Az egyik leghosszabb a(z) {legh_osveny_index+1}. ösvény, hossza: {len(osvenyek[legh_osveny_index])} ")

# 4
feladat()
jatek_osveny:int = int(input("Adja meg egy ösvény sorszámát! ")) -1 # indexeles korrekcio
if jatek_osveny < 0 or jatek_osveny > len(osvenyek)-1: # ellenorzes
    while jatek_osveny < 0 or jatek_osveny > len(osvenyek)-1:
        print(f"A sorszám 1 és {len(osvenyek)} között legyen!")
        jatek_osveny:int = int(input("Adja meg egy ösvény sorszámát! ")) -1

jatekosok:int = int(input("Adja meg a játékosok számát! "))
if jatekosok > 5 or jatekosok < 2: # ellenorzes
    while jatekosok > 5 or jatekosok < 2:
        print("A játékosok száma minimum 2, maximum 5 lehet!")
        jatekosok:int = int(input("Adja meg a játékosok számát! "))

jatek_osveny_hossza = len(osvenyek[jatek_osveny]) -1

# 5
feladat()
statisztika:list[int] = [0,0,0] # [M,V,E]
for mezo in osvenyek[jatek_osveny]:
    if mezo == "M":
        statisztika[0] += 1
    elif mezo == "V":
        statisztika[1] += 1
    else:
        statisztika[2] += 1

if statisztika[0]:
    print(f"M: {statisztika[0]} darab")
if statisztika[1]:
    print(f"V: {statisztika[1]} darab")
if statisztika[2]:
    print(f"E: {statisztika[2]} darab")

# 6
feladat_ctr += 1

with open(HOME_PATH+"kulonleges.txt",'w',encoding="utf-8") as x:
    for i in range(len(osvenyek[jatek_osveny])):
        if osvenyek[jatek_osveny][i] == 'E':
            x.write(f"{i+1}\tE\n")
        elif osvenyek[jatek_osveny][i] == 'V':
            x.write(f"{i+1}\tV\n")

# 7
feladat()

def lejatszas(osveny:str, minden_mezo_ures:bool=False)->list:
    vege = [] # return val a feladathoz kello infokkal

    dobas_kurzor = -1 # vegigfut a 'dobasok' listan, kezdeti erteke 0 lesz
    jelen_dobas = 0 # mindig a dobasok[dobas_kurzor] lesz
    poziciok = [-1]*jatekosok # nincsenek rajta a palyan az elso dobasig
    jelen_jatekos = -1 # kezdo erteke 0 lesz, ami az 1. jatekos
    
    debug_poziciok = []

    jatek_fut = True
    osveny_hossza = len(osveny)-1
    if minden_mezo_ures:
        osveny = 'M'*(osveny_hossza+1)

    while jatek_fut:
        dobas_kurzor += 1
        jelen_dobas = dobasok[dobas_kurzor] 
        jelen_jatekos = (jelen_jatekos +1)%jatekosok
        
        poziciok[jelen_jatekos] += jelen_dobas
        if poziciok[jelen_jatekos] <= osveny_hossza:
            if osveny[ poziciok[jelen_jatekos] ] == 'E':
                poziciok[jelen_jatekos] += jelen_dobas
            elif osveny[ poziciok[jelen_jatekos] ] == 'V':
                poziciok[jelen_jatekos] -= jelen_dobas
        
        # ellenorzes minden kor vegen
        if jelen_jatekos == jatekosok-1: # adott kor vege
            for i in range(jatekosok):
                if poziciok[i] >= osveny_hossza:
                    jatek_fut = False
    
    # visszateresi ertek
    vege = poziciok.copy() # vegso poziciok
    vege.append(1+dobas_kurzor//jatekosok) # hanyadik kor a vege
    return vege

feladat7eredmeny = lejatszas(osveny=osvenyek[jatek_osveny], minden_mezo_ures=True)
feladat7nyertes = ' '.join([str(i+1) for i in range(jatekosok) if feladat7eredmeny[i] >= jatek_osveny_hossza])

print(f"A játék a(z) {feladat7eredmeny[-1]}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {feladat7nyertes}")

# 8
feladat()
feladat8eredmeny = lejatszas(osveny=osvenyek[jatek_osveny])
feladat8nyertes = ' '.join([str(i+1) for i in range(jatekosok) if feladat8eredmeny[i] >= jatek_osveny_hossza])
feladat8szoveg = ""
for i in range(jatekosok):
    if feladat8eredmeny[i] < jatek_osveny_hossza:
        feladat8szoveg += f"{i+1}. játékos, {1+feladat8eredmeny[i]}. mező\n"

print("Nyertes(ek):",feladat8nyertes)
print("A többiek pozíciója:")
print(feladat8szoveg)



"""
    print("JATEK KEZDODIK")
    while jatek_fut:
        # dobokocka szimulator
        dobas_kurzor += 1
        jelen_dobas = dobasok[dobas_kurzor]
        elmozdulas = jelen_dobas
        jelen_jatekos = dobas_kurzor%jatekosok
        # elorelepes
        poziciok[jelen_jatekos] += elmozdulas
        # uj mezo tipusa 
        if osveny[ poziciok[jelen_jatekos] ] == 'E':
            poziciok[jelen_jatekos] += elmozdulas
        elif osveny[ poziciok[jelen_jatekos] ] == 'V':
            poziciok[jelen_jatekos] -= elmozdulas
        
        # ================= DEBUG =================
        debug_poziciok = poziciok.copy()
        debug_poziciok[jelen_jatekos] = f"{debug_poziciok[jelen_jatekos]-elmozdulas}+{elmozdulas}"

        print(f"{'-'*10} {dobas_kurzor//jatekosok}. KÖR")
        print("kurzor\tdobas\tmezo\tmozgas\tjatekos\tpoziciok")
        print(dobas_kurzor,'\t',jelen_dobas,'\t',mezo,'\t',elmozdulas,'\t',jelen_jatekos+1,'\t',debug_poziciok)
        # ================= DEBUG =================

        # teszt hogy vege van-e
        if dobas_kurzor%jatekosok == jatekosok-1:
            print("CHECKSUM",osveny_hossza)
            for i in range(jatekosok):
                if poziciok[i] >= osveny_hossza:
                    poziciok[i] = osveny_hossza
                    jatek_fut = False
            # ================= DEBUG =================
                    print(f"{1+i} JATEKOS OVER 9000")
                else:
                    print(f"{1+i} JATEKOS OK",poziciok[i])
            # ================= DEBUG =================
            print("END OF CHECKSUM")
    
    print("\nmain for ciklus vege")
    print(poziciok)
    print(dobas_kurzor)
"""