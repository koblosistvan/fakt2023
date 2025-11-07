forras1=open('felszin_tpont.txt', mode='r', encoding='utf-8')

xkoord=[]
ykoord=[]
radius=[]
nev=[]

for sor in forras1:
    adat=sor.strip().split('\t')
    xkoord.append(adat[0])
    ykoord.append(adat[1])
    radius.append(adat[2])
    nev.append(adat[3])

forras1.close()

#2


print(f'Az allomanyban {len(nev)}db adat van')

#3


beker=input('Add meg a krater nevet: ')

if beker in nev:
    index = nev.index(beker)
    print(f'A(z) {beker} nevű kráter adatai:')
    print(f'X koordináta: {xkoord[index]}')
    print(f'Y koordináta: {ykoord[index]}')
    print(f'Rádiusz: {radius[index]}')
else:
    print('Nincs ilyen nevű kráter az állományban.')


#4


maxr = float(radius[0])
index = 0

for i in range(1, len(radius)):
    if float(radius[i]) > maxr:
        maxr = float(radius[i])
        index = i

print(f'A legnagyobb kráter neve és sugara: {nev[index]} {maxr}')

#5


import math

def tavolsag(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#6


beker = input('Kérem egy kráter nevét: ')
if beker in nev:
    i = nev.index(beker)
    x1 = float(xkoord[i])
    y1 = float(ykoord[i])
    r1 = float(radius[i])
    nincs_kozos = []

    for j in range(len(nev)):
        if i != j:
            x2 = float(xkoord[j])
            y2 = float(ykoord[j])
            r2 = float(radius[j])
            d = tavolsag(x1, y1, x2, y2)
            if d > r1 + r2:
                nincs_kozos.append(nev[j])

    if nincs_kozos:
        print('Nincs közös része:', ', '.join(nincs_kozos))


#7


print('7. feladat')
for i in range(len(nev)):
    for j in range(len(nev)):
        if i != j:
            x1 = float(xkoord[i])
            y1 = float(ykoord[i])
            r1 = float(radius[i])
            x2 = float(xkoord[j])
            y2 = float(ykoord[j])
            r2 = float(radius[j])
            d = tavolsag(x1, y1, x2, y2)

            if r1 > r2 and d < (r1 - r2):
                print(f'A(z) {nev[i]} kráter tartalmazza a(z) {nev[j]} krátert.')
#8



print('8. feladat')
with open('terulet.txt', mode='w', encoding='utf-8') as f:
    for i in range(len(nev)):
        r = float(radius[i])
        terulet = round(r * r * 3.14, 2)
        f.write(f'{terulet:.2f}\t{nev[i]}\n')
