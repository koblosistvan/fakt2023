# 1
fajl_neve = input('1. feladat\nAdja meg a bemeneti fájl nevét! ')
bekertsor = int(input('Adja meg egy sor számát! '))
bekertoszlop = int(input('Adja meg egy oszlop számát! '))

# 2
forras = open(fajl_neve, 'r', encoding='utf-8')
tabla = [[0]*9]*9
for i in range(9):
    sor = forras.readline().strip().split(' ')
    for k in range(len(sor)):
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
adottszam = tabla[bekertoszlop-1][bekertsor-1]
rasztabla = bekertsor % 9 in (1, 2, 3)



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