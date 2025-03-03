import random

forras = open('csapatnevek.txt', mode = 'r', encoding='utf-8')

csapatok = []

for sor in forras:
    adat = sor.strip()
    csapatok.append(adat)
forras.close()

csapatnevek = input('Add meg a két csapat nevét! ')
eredmeny = input('Adja meg az eredményt! ')


eredmenylista = []

for sor in eredmeny:
    adat = eredmeny.split(':')
    eredmenylista.append(int(adat[1]))
    eredmenylista.append(int(adat[0]))

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

seged = 1
print('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:')
for meccs in meccsek:
    print(f'{seged}. {meccs[0]} - {meccs[2]} {meccs[1]}:{meccs[3]} {x12(meccs[1], meccs[3])} ')
    seged += 1
print(f'+1. {csapatnevek} {eredmeny}')

uj_fajl = open('szelveny.txt', mode='w', encoding='utf-8')

seged2 = 1

print('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:', file=uj_fajl)
for meccs in meccsek:
    print(f'{seged2}. {meccs[0]} - {meccs[2]} {meccs[1]}:{meccs[3]} {x12(meccs[1], meccs[3])} ', file=uj_fajl)
    seged2 += 1
print(f'+1. {csapatnevek} {eredmeny}', file=uj_fajl)

golkulonbsegek = []
for meccs in meccsek:
    golkulonbseg = abs(meccs[1] - meccs[3])
    golkulonbsegek.append(golkulonbseg)

seged3 = 1

legn_golk_meccsek = []

for meccs in meccsek:
    if abs(meccs[1] - meccs[3]) == max(golkulonbsegek):
        legn_golk_meccsek.append(seged3)
    seged += 1
    if abs(eredmenylista[0] - eredmenylista[1]) == max(golkulonbsegek):
        legn_golk_meccsek.append('+1')

print(f'Legnagyobb golkünbségű meccsek: {legn_golk_meccsek}')

