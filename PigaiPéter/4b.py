import random
pontok = []
ponthatár = 96
jeles = 0
majdnemjeles = 0
maxim = 0
tizsz = 0
huszsz = 0
harmsz = 0
negyvsz = 0
otvsz = 0
hatvsz = 0
hetvsz = 0
nyolcsz = 0
kilencsz = 0
szazsz = 0
atlag = 0
for i in range(100):
    b = random.randint(0, 120)
    pontok[:0] = [b]
    if pontok[0] >= ponthatár:
        jeles += 1
    if pontok[0] + 3 >= ponthatár:
        majdnemjeles += 1
    if pontok[0] == 120:
        maxim += 1
    if pontok[0] <= (120 / 100) * 10:
        tizsz += 0
    elif (120 / 100) * 10 < pontok[0] <= (120 / 100) * 20:
        huszsz += 1
    elif (120 / 100) * 20 < pontok[0] <= (120 / 100) * 30:
        harmsz += 1
    elif (120 / 100) * 30 < pontok[0] <= (120 / 100) * 40:
        negyvsz += 1
    elif (120 / 100) * 40 < pontok[0] <= (120 / 100) * 50:
        otvsz += 1
    elif (120 / 100) * 50 < pontok[0] <= (120 / 100) * 60:
        hatvsz += 1
    elif (120 / 100) * 60 < pontok[0] <= (120 / 100) * 70:
        hetvsz += 1
    elif (120 / 100) * 70 < pontok[0] <= (120 / 100) * 80:
        nyolcsz += 1
    elif (120 / 100) * 80 < pontok[0] <= (120 / 100) * 90:
        kilencsz += 1
    elif (120 / 100) * 90 < pontok[0]:
        szazsz += 1
    atlag += pontok[0]
print(f'{jeles} jeles lett')
print(f'{majdnemjeles} majdnem jeles lett')
print(f'{maxim} max pontos lett')
print(f'10%os határokba {tizsz} {huszsz} {harmsz} {negyvsz} {otvsz} {hatvsz} {hetvsz} {nyolcsz} {kilencsz} {szazsz}')
print(f'Az átlag pontszám: {atlag/100}')
