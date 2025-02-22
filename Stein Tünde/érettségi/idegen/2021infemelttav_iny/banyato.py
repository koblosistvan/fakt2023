# 1
forras = open('Stein Tünde/érettségi/idegen/2021infemelttav_iny/melyseg.txt', 'r', encoding='utf-8')
sorok = int(forras.readline().strip())
oszlopok = int(forras.readline().strip())
to = [ [ [0] for i in range(oszlopok) ] for k in range(sorok) ]
seged = 0
for i in forras:
    sor = i.strip().split(' ')
    for k in range(oszlopok):
        to[seged][k] = sor[k]
    seged += 1
forras.close()

# 2
sorazon = int(input('2. feladat\nA mérés sorának azonosítója='))
oszlopazon = int(input('A mérés oszlopának azonosítója='))
print(f'A mért mélység az adott helyen {to[sorazon-1][oszlopazon-1]} dm')

# 3
felszincounter = 0
osszmelyseg = 0
for i in range(len(to)):
    for k in range(len(to[i])):
        if to[i][k]:
            felszincounter += 1
            osszmelyseg += to[i][k]
print(f'3. feladat\nA tó felszíne: {felszincounter} m2, átlagos mélysége: {osszmelyseg/felszincounter} m')



"""2. feladat 
A mérés sorának azonosítója=12 
A mérés oszlopának azonosítója=6 
A mért mélység az adott helyen 33 dm 
3. feladat 
A tó felszíne: 646 m2, átlagos mélysége: 4,28 m 
4. feladat 
A tó legnagyobb mélysége: 98 dm 
A legmélyebb helyek sor-oszlop koordinátái: 
(14; 20) (26; 11) (32; 16) 
5. feladat 
A tó partvonala 270 m hosszú 
6. feladat 
A vizsgált szelvény oszlopának azonosítója=6 """