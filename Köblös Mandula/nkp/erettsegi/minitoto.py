import random

forras = open('csapatnevek.txt', mode='r', encoding='utf-8')

cspatok = []

for sor in forras:
    adat = sor.strip()
    cspatok.append(adat)

forras.close()

merkozesek = input('Melyik 2 csapat játszott?(csapat1-csapat2) ')

eredmenyek = input('Mi lett az eredmény?(golok1:golok2) ')

golok = []
eredmeny = eredmenyek.strip().split(':')
golok.append(eredmeny)

print(golok)
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



kiiras = open('szelveny.txt', mode='w', encoding='utf-8')

print('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:', file=kiiras)
szamlalo = 1
for meccs in meccsek:
    print(f"{szamlalo}. {meccs[0]} - {meccs[2]} {meccs[1]}:{meccs[3]} {x12(meccs[1], meccs[3])}", file=kiiras)
    szamlalo += 1
print(f'+1 {merkozesek} {eredmenyek}', file=kiiras)


golkulonbseg = []
for meccs in meccsek:
    golkulonbseg.append(abs(meccs[1]-meccs[3]))
print(f'Legnagyobb gólkülönbségű mérkőzések: {max(golkulonbseg)}')

dontetlen = 0
for meccs in meccsek:
    if x12(meccs[1], meccs[3]) == 'X':
        dontetlen += 1
        print(f'{meccs[0]} - {meccs[2]}')
if x12(eredmenyek[0], eredmenyek[2]) == 'X':
    dontetlen += 1
    print(merkozesek)
print(f'Döntetlen meccsek száma: {dontetlen}')


print(f'Legalább 2 góllal nyertek: ')
pontos_2 = 0
for meccs in meccsek:
    if abs(meccs[1]-meccs[3]) >= 2:
        if meccs[1] > meccs[3]:
            print(meccs[0])
        elif meccs[3] > meccs[1]:
            print(meccs[2])
        pontos_2 += 1
if pontos_2 == 0:
    print(f'Nem volt legalább két gólos győzelem.')


print('Vége')