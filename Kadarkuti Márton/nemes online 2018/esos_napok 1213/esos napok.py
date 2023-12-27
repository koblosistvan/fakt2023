with open("esos.txt","r",encoding="utf-8") as f:
    f.readline()
    eso = f.readline().strip().split(" ")
    eso = list(map(int,eso))
#print(eso)

feladatCounter = 1
def feladat():
    print("")
    print("𒈙" * 5)
    global feladatCounter
    print(f" < {feladatCounter}.>")
    feladatCounter += 1

# 1.
feladat()

print(f"{sum( [bool(i) for i in eso] )} napon esett az eső.")

# 2.
feladat()
csapadekmentes_idoszakok = "".join([("1" if bool(i) else "0") for i in eso]).split("1")
csapadekmentes_idoszakok = [(len(i) if len(i)>0 else 0) for i in csapadekmentes_idoszakok]
print(f"A leghosszabb csapadékmentes időszak {max(csapadekmentes_idoszakok)} napig tartott.")

# 3.
feladat()

ket_napi_max = 0
for i in range(len(eso)-1):
    temp = eso[i]+eso[i+1]
    if temp > ket_napi_max:
        ket_napi_max = temp
print(f"A legtöbb csapadék két nap között {ket_napi_max} mm.")

# 4.
feladat()

with open("esos.txt","r",encoding="utf-8") as f:
    f.readline()
    binary_eso = f.readline().strip().split(" ")
    binary_eso = [ (1 if bool(int(i)) else 0) for i in binary_eso ]
#print(binary_eso)

#print(binary_eso)

# kömal i603ból lopva:

def join(lista):  # pl: [1,2,3] => 123
    if lista[0] == 0 and len(lista) > 1: # nullával kezdődő részek érvénytelenítése
        return None   # az indexeltség miatt helyettesítő érték kell
    lista = "".join( map(str,lista))
    return int(lista)

# 123 => [1,2,3]
intervallumok = []       # return érték
for i in range(len(binary_eso)):
    for j in range(1 + i, len(binary_eso) + 1):
        intervallumok.append( (i+1, join(binary_eso[i:j])) )
        # adatok mentése így:
            # tuple   ( <intervallum kezdeti nap>, <konkatenált bináris intervallum>)


for i in range(len(intervallumok)): # 0-val kezdődőek
    if None in intervallumok[i]:
        intervallumok[i] = None

for _ in range(intervallumok.count(None)):
    intervallumok.remove(None)

# 0-ra végződőek:
noneCounter = 1
while noneCounter > 0:
    noneCounter = 0   # reset
    for i in range(len(intervallumok)):
        #print(intervallumok[i])
        if str(intervallumok[i][1])[-1] == '0':
            intervallumok[i] = None
            noneCounter += 1
    for _ in range(noneCounter):
        intervallumok.remove(None)

#print(intervallumok)
# lista struktúrája: tuple (<kezdeti nap> , <intervallum ami biztosan 1...1 alakban van> )

import math
jo_inter = []
for i in range(len(intervallumok)):
    c = str(intervallumok[i][1])
    if c.count("1") >= math.ceil(len(c)/2):
        jo_inter.append(intervallumok[i])
#print(jo_inter)
valasz = ""
for i in range(len(jo_inter)):
    if len(str(jo_inter[i][1])) > len(valasz):
        valasz = jo_inter[i]
#print(valasz)
print(f"A leghosszabb intervallum, amelyen legalább a napok felében esett, és az intervallum első és utolsó")
print(f"napján is esett, a {valasz[0]}. naptól a {valasz[0]-1+len(str(valasz[1]))}. napig tartott.")