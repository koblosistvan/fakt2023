LISTAHOSSZ = 25
# a feladatban megadott korongok száma 25

import math

def gcd(a,b): # legkisebb közös többszörös
    if math.gcd(a,b) != 1:
        return True
    else:
        return False

def is_prime(n):  # prímteszt
    n = abs(n)
    if n in (1, 0):
        return False

    for i in range(2, int(n / 2) + 1):
        if n%i == 0:
            return False
    else:
        return True

def primtenyezok(n):  # listába gyűjti egy szám prímtényezőit, növekvő sorrendben, ismétléssel, 1-et is beleértve
    n = abs(n)
    if n == 0: # hibaüzenet, ha ezzel lenne gond
        print(f"-------\nROSSZ\n-------")
        quit()

    n = abs(n)
    if n == 1:
        return [1]

    if is_prime(n):
        return [1,n]

    factors = [1]
    while n%2 == 0:
        factors.append(2)
        n = int(n/2)
    for i in range(3, int(n/2 + 0.5) , 2):
        while n%i == 0:
            factors.append(i)
            n = int(n/i)
    return factors

def prtld(a,b):   # két szám prímtényezőinek számának különbsége nagyobb-e, mint 1? (2)-nél kell.
    d = len(primtenyezok(a)) - len(primtenyezok(b))
    d = abs(d)
    if d > 1:
        return True
    else:
        return False

def vonal():
    print("-"*30)

def rovidebb(l, ll):  # két lista közül eldönti, melyik hosszabb (végül nem kellett)
    if len(l) <= len(ll):
        return len(l)
    else:
        return len(ll)

def compareFactors(x, y):  # (végül nem kellett)
    x = primtenyezok(x)
    y = primtenyezok(y)
    for i in range(rovidebb(x,y)):
        if x[i] != y[i]:
            return False
    return True

class Szamok:  # ide lesz mentve, hogy egy szám még hozzátehető-e egy oszlophoz
    futtatva = 0
    def __init__(self, szam):
        Szamok.futtatva += 1
        self.szam = szam
        self.elerheto = True
        self.prim = is_prime(self.szam)
        self.index = self.szam -1
        self.hasznalhato = False
    def __str__(self):
        return f"{self.szam}"
lista = [Szamok(i+1) for i in range(LISTAHOSSZ)]

szabad = [i+1 for i in range(LISTAHOSSZ)]  # ki lesz ejtve innen minden elem, ami használható

#print(szabad)
#print(len(lista),Szamok.futtatva,len(szabad))

primek = [] # (végül nem kellett)
for i in range(LISTAHOSSZ):
    if lista[i].prim:
        primek.append(lista[i].szam)

def debugPrint(): # ellenőrzéshez kellett
    print("SZÁM: | ELÉRHETŐSÉG:")
    for i in range(LISTAHOSSZ):
        print(f"{lista[i].szam} - {lista[i].elerheto}")

oszlopok = [] # tartalmazza az oszlopokat listákként
hasznalt = set() # tartalmazza az oszlopokban lévő számokat
hasznaltHalmazHossza = 0 # rossz bemenet esetére kell

# BEMENET:
print("KöMaL 2023. október: i600 feladat")
vonal()
print("Hány oszlop van?")
try:
    oszlopSzam = int(input("  [>] Az oszlopok száma: "))
    print("Add meg a számokat <szóközzel> elválasztva")
    for i in range(oszlopSzam):
        adat = input(f"  [>] {i+1}. oszlop: ")
        adat = adat.strip().split(" ")
        for j in range(len(adat)):
            adat[j] = int(adat[j])
        oszlopok.append( [adat[k] for k in range(len(adat))] )
        for k in range(len(adat)):
            hasznalt.add(adat[k])
            hasznaltHalmazHossza += 1
    hasznalt = sorted(hasznalt)
except:
    vonal()
    print("\nÉrvénytelen a beírt érték.")
    quit()

#print(hasznalt)
#print(oszlopok)
#print(hasznalt)

#ELLENŐRZÉS:
def oszlopHibaUzenet():
    vonal()
    print("\nÉrvénytelen a beírt oszlop.")
    quit()

if len(hasznalt) != hasznaltHalmazHossza:  # többször beírt számok esetén
    oszlopHibaUzenet()
if max(hasznalt) > 25 or min(hasznalt) < 1: # hibás intervallum esetén
    oszlopHibaUzenet()

def ervenyesOszlop(x): # érvénytelen bemenet esetén
    for i in range(len(x)-1):
        if x[i+1] % x[i] != 0:
            oszlopHibaUzenet()
for i in range(len(oszlopok)):
    ervenyesOszlop(oszlopok[i])

# a beírt korongokat nem elérhetővé teszi
for i in range(LISTAHOSSZ):
    if lista[i].szam in hasznalt:
        lista[i].elerheto = False
for i in range(len(hasznalt)):
        szabad.remove(hasznalt[i])
#print(szabad)
#print(len(szabad))

# SZÁMÍTÁS:
# (1) kerülhet-e korong az első alá?
# (2) kerülhet-e korong bármely két köztes közé?
# (3) kerülhet-e korong az utolsó felé?
# hatékonyabb a (2) feladatot utoljára futtatni


# speciális eset: két elemű oszlop
for ciklus in range(oszlopSzam):
    if len(oszlopok[ciklus]) == 2:
        for i in range(len(szabad)):
            if szabad[i] == None:
                continue
            if lista[szabad[i]-1].elerheto:
                if szabad[i]%oszlopok[ciklus][0] == 0 and oszlopok[ciklus][1]%szabad[i] == 0:
                    lista[szabad[i]-1].elerheto = False
                    lista[szabad[i]-1].hasznalhato = True
                    szabad[i] = None


#(1): első elem
for ciklus in range(oszlopSzam):
    for i in range(len(szabad)):
        if szabad[i] == None:
            continue
        if oszlopok[ciklus][0]%szabad[i] == 0 and lista[szabad[i]-1].elerheto:
            lista[szabad[i]-1].elerheto = False
            lista[szabad[i]-1].hasznalhato = True
            szabad[i] = None

#(3): utolsó elem
for ciklus in range(oszlopSzam):
    for i in range(len(szabad)):
        if szabad[i] == None:
            continue
        if szabad[i]%oszlopok[ciklus][-1] == 0 and lista[szabad[i]-1].elerheto:
            #print(i)
            lista[szabad[i]-1].elerheto = False
            lista[szabad[i]-1].hasznalhato = True
            szabad[i] = None

#(2): középső elemek
for ciklus in range(oszlopSzam):
    for i in range(len(oszlopok[ciklus])-1):
        if prtld(oszlopok[ciklus][i], oszlopok[ciklus][i+1]):
            for j in range(len(szabad)):
                if szabad[j] == None:
                    continue
                if lista[szabad[j]-1].elerheto:
                    if szabad[j]%oszlopok[ciklus][i] == 0 and oszlopok[ciklus][i+1]%szabad[j] == 0:
                        lista[szabad[j]-1].elerheto = False
                        lista[szabad[j]-1].hasznalhato = True
                        szabad[i] = None

# EREDMÉNY KIÍRÁSA:
hasznalhato = []
for i in range(len(lista)):
    if lista[i].hasznalhato:
        hasznalhato.append(lista[i].szam)

#print("EZEK MÉG HASZNÁLHATÓK:")
#print(hasznalhato)

szabad_korongok_print = [i+1 for i in range(LISTAHOSSZ)]
szabadKorongokSzoveg = ""
nem_hozzateheto_print = [i+1 for i in range(LISTAHOSSZ)]
nemHozzatehetoSzoveg = ""
hasznalhatoKorongokSzoveg = ""

for i in range(len(hasznalt)):
    szabad_korongok_print.remove(hasznalt[i])
for i in range(len(szabad_korongok_print)):
    szabadKorongokSzoveg += f"{szabad_korongok_print[i]} "

for i in range(len(hasznalhato)):
    nem_hozzateheto_print.remove(hasznalhato[i])
for i in range(len(nem_hozzateheto_print)):
    nemHozzatehetoSzoveg += f"{nem_hozzateheto_print[i]} "

for i in range(len(hasznalhato)):
    hasznalhatoKorongokSzoveg += f"{hasznalhato[i]} "

vonal()
print(f"SZABAD KORONGOK: {szabadKorongokSzoveg}")
print(f"NEM HOZZÁTEHETŐ KORONGOK: {nemHozzatehetoSzoveg}")
vonal()
print(f"HOZZÁTEHETŐ KORONGOK: {hasznalhatoKorongokSzoveg}")
vonal()
