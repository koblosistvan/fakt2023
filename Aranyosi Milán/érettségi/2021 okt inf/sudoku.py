print('1. feladat')
fajlnev = input('Adja meg a bemeneti fájl nevét!')
adott_sor = int(input('Adja meg egy sor számát!'))
adott_oszlop = int(input('Adja meg egy oszlop számát!'))

forras = open(fajlnev, mode='r', encoding='utf-8')

sorok = []
valtoztatasok = []

for sor in forras:
    adat = sor.strip().split(' ')
    if len(adat) > 3:
        sorok.append(adat)
    else:
        valtoztatasok.append(adat)

print('3. feladat')

adottszam = sorok[adott_sor-1][adott_oszlop-1]
if adottszam == '0':
    adottszam = 'Az adott helyet még nem töltötték ki.'

def resztabla(adott_sor, adott_oszlop):
    resztabla = 0
    if adott_sor <= 3:
        if adott_oszlop <= 3:
            resztabla = 1
        elif 4 <= adott_oszlop <= 6:
            resztabla = 2
        elif 7 <= adott_oszlop <= 9:
            resztabla = 3

    if 4 <= adott_sor <= 6:
        if adott_oszlop >= 3:
            resztabla = 4
        elif 4 <= adott_oszlop <= 6:
            resztabla = 5
        elif 7 <= adott_oszlop <= 9:
            resztabla = 6

    if 7 <= adott_sor <= 9:
        if adott_oszlop <= 3:
            resztabla = 7
        elif 4 <= adott_oszlop <= 6:
            resztabla = 8
        elif 7 <= adott_oszlop <= 9:
            resztabla = 9
    return resztabla


print(f'Az adott helyen szereplő szám: {adottszam}')
print(f'A hely a(z) {resztabla(adott_sor,adott_oszlop)} résztáblázathoz tartozik.')

print('4. feladat')

osszes = len(sorok) * len(sorok[0])

ures_szaml = 0

for i in range(len(sorok)):
    for j in range(len(sorok[i])):
        if sorok[i][j] == '0':
            ures_szaml += 1

print(f'Az üres helyek aránya: {ures_szaml / osszes:0.1%}')

print('5. feladat')

for i in range(len(sorok)):
    valtozas_reszhalmaza = []
    valtozas_oszlopa = []
    valtozas_sora = []
    for j in range(len(valtoztatasok)):
        valtozas_oszlop = valtoztatasok[j][3]
        valtozas_sor = valtoztatasok[j][2]
        valtozas_szam = valtoztatasok[j][1]
        if sorok[i] == valtozas_sor:
            valtozas_sora



'''
A kiválasztott sor: 2 oszlop: 4 a szám: 9
A helyet már kitöltötték.
A kiválasztott sor: 3 oszlop: 6 a szám: 7
A lépés megtehető.
A kiválasztott sor: 6 oszlop: 6 a szám: 3
A résztáblázatban már szerepel a szám.
A kiválasztott sor: 7 oszlop: 9 a szám: 8
Az adott oszlopban már szerepel a szám. 
'''