import random

forras = open('csapatnevek.txt', mode='r', encoding='utf-8')

cspatok = []

for sor in forras:
    adat = sor.strip()
    cspatok.append(adat)

forras.close()

merkozesek = input('Melyik 2 csapat játszott?(csapat1-csapat2) ')

eredmenyek = input('Mi lett az eredmény?(golok1:golok2) ')

def x12(gól1,gól2):
    if gól1 > gól2:
        return '1'
    elif gól2 > gól1:
        return '2'
    else:
        return 'X'

csapatok_másolat = cspatok.copy()
meccsek = []

for i in range(7):
    hazai = random.choice(csapatok_másolat)
    csapatok_másolat.remove(hazai)
    hazai_gol = random.randint(0, 5)

    vendég = random.choice(csapatok_másolat)
    csapatok_másolat.remove(vendég)
    vendeg_gol = random.randint(0, 5)

    meccsek.append([hazai, hazai_gol, vendég, vendeg_gol])

print('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:')
for meccs in meccsek:
    print(f"{meccs[0]} - {meccs[2]} {meccs[1]}:{meccs[3]} {x12(meccs[1], meccs[3])}")




print('Vége')