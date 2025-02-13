# 1
fajl_neve = input('1. feladat\nAdja meg a bemeneti fájl nevét! ')
bekertsor = int(input('Adja meg egy sor számát! '))
bekertoszlop = int(input('Adja meg egy oszlop számát! '))

# 2
forras = open(fajl_neve, 'r', encoding='utf-8')
tabla = [[0]*9 for _ in range(9)]

for i in range(9):
    sor = forras.readline().strip().split(' ')
    for k in range(9):
        a = tabla[i]
        b = tabla[i][k]
        tabla[i][k] = int(sor[k])
lepes = []
tsor = []
oszlop = []
for i in forras:
    sor = i.strip().split(' ')
    lepes.append(int(sor[0]))
    tsor.append(int(sor[1]))
    oszlop.append(int(sor[2]))
forras.close()

# 3

def resztabla(s, o):
    if s < 4:
        resz = 1
        if o > 3:
            resz += 3
        if o > 6:
            resz += 3
    elif s <= 6:
        resz = 2
        if o > 3:
            resz += 3
        if o > 6:
            resz += 3
    else:
        resz = 3
        if o > 3:
            resz += 3
        if o > 6:
            resz += 3
    return resz


adottszam = tabla[bekertsor-1][bekertoszlop-1]
print('3. feladat')
if adottszam:
    print(f'Az adott helyen szereplő szám: {adottszam}')
else:
    print('Az adott helyet még nem töltötték ki.')
print(f'A hely a(z) {resztabla(bekertsor, bekertoszlop)} résztáblázathoz tartozik. ')

# 4
ures = 0
for i in tabla:
    for k in i:
        if not k:
            ures += 1
print(f'4. feladat\n'
      f'Az üres helyek aránya: {round(ures/81*100, 1)}%')

# 5
print('5. feladat')
for i in range(len(lepes)):
    oszloplista = []
    reszlista = []
    for k in range(9):
        oszloplista.append(tabla[k][oszlop[i]-1])
    for k in range(9):
        for j in range(9):
            if resztabla(k+1, j+1) == resztabla(tsor[i], oszlop[i]):
                reszlista.append(tabla[i][k])
    print(f'A kiválasztott sor: {tsor[i]} oszlop: {oszlop[i]} a szám: {lepes[i]}')
    if tabla[tsor[i]-1][oszlop[i]-1]:
        print('A helyet már kitöltötték. ')
    elif lepes[i] in tabla[tsor[i]-1]:
        print('Az adott sorban már szerepel a szám.')
    elif lepes[i] in oszloplista:
        print('Az adott oszlopban már szerepel a szám.')
    elif lepes[i] in reszlista:
        print('A résztáblázatban már szerepel a szám.')
    else:
        print('A lépés megtehető. ')

"""1. feladat 
Adja meg a bemeneti fájl nevét! konnyu.txt 
Adja meg egy sor számát! 1 
Adja meg egy oszlop számát! 1 
3. feladat 
Az adott helyen szereplő szám: 5 
A hely a(z) 1 résztáblázathoz tartozik. 
4. feladat 
Az üres helyek aránya: 17.3% 
5. feladat 
A kiválasztott sor: 2 oszlop: 4 a szám: 9 
A helyet már kitöltötték. 
A kiválasztott sor: 3 oszlop: 6 a szám: 7 
A lépés megtehető. 
A kiválasztott sor: 6 oszlop: 6 a szám: 3 
A résztáblázatban már szerepel a szám. 
A kiválasztott sor: 7 oszlop: 9 a szám: 8 
Az adott oszlopban már szerepel a szám. """