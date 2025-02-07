print('1. feladat')
fajlnev = input('Adja meg a bemeneti fájl nevét!')
adott_sor = int(input('Adja meg egy sor számát!'))
adott_oszlop = int(input('Adja meg egy oszlop számát!'))

forras = open('Aranyosi Milán/érettségi/2021 okt inf/'+fajlnev, mode='r', encoding='utf-8')

sorok = []
valtoztatasok = []

for sor in forras:
    adat = sor.strip().split(' ')
    if len(adat) > 3:
        sorok.append(adat)
    else:
        valtoztatasok.append(adat)

print(sorok)


'''
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
Az adott oszlopban már szerepel a szám. 
'''