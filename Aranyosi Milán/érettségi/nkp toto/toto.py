import random

forras = open('csapatnevek.txt', mode = 'r', encoding='utf-8')

csapatok = []

for sor in forras:
    adat = sor.strip()
    csapatok.append(adat)
forras.close()

csapatnevek = input('Add meg a két csapat nevét! ')
eredmeny = input('Adja meg az eredményt! ')


eredmenyek = eredmeny.strip().split(':')
gol1 = int(eredmenyek[0])
gol2 = int(eredmenyek[1])

def x12(gol1, gol2):
    if gol1 > gol2:
        return '1'
    elif gol2 > gol1:
        return '2'
    else:
        return 'x'

csapatok_masolat = csapatok.copy()
meccsek = []

for i in range(7):
    hazai = random.choice(csapatok_masolat)
    csapatok_masolat.remove(hazai)
    hazai_gol = random.randint(0, 5)

    vendeg = random.choice(csapatok_masolat)
    csapatok_masolat.remove(vendeg)
    vendeg_gol = random.randint(0, 5)

    meccsek.append([hazai, hazai_gol, vendeg, vendeg_gol])

print('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:')
for meccs in meccsek:
    print(f'{meccs[0]} - {meccs[2]} {meccs[1]}:{meccs[3]} {x12(meccs[1], meccs[3])} ')



