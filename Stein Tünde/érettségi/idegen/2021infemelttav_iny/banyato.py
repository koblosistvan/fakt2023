# 1
forras = open('Stein Tünde/érettségi/idegen/2021infemelttav_iny/melyseg.txt', 'r', encoding='utf-8')
sorok = int(forras.readline().strip())
oszlopok = int(forras.readline().strip())
to = [ [ [0] for i in range(oszlopok) ] for k in range(sorok) ]
seged = 0
for i in forras:
    sor = i.strip().split(' ')
    for k in range(oszlopok):
        to[seged][k] = int(sor[k])
    seged += 1
forras.close()

# 2
sorazon = int(input('2. feladat\nA mérés sorának azonosítója='))
oszlopazon = int(input('A mérés oszlopának azonosítója='))
print(f'A mért mélység az adott helyen {to[sorazon-1][oszlopazon-1]} dm')

# 3
felszincounter = 0
osszmelyseg = 0
maxim = to[0][0]
for i in range(len(to)):
    for k in range(len(to[i])):
        if to[i][k]:
            felszincounter += 1
            osszmelyseg += to[i][k]
        if to[i][k] > maxim:
            maxim = to[i][k]
atlag = osszmelyseg/felszincounter/10
print(f'3. feladat\nA tó felszíne: {felszincounter} m2, átlagos mélysége: {str(round(atlag, 2)).replace(".", ",")} m')

# 4
koordinatak = []
for i in range(sorok):
    for k in range(oszlopok):
        if to[i][k] == maxim:
            koordinatak.append(f'({i+1}; {k+1})')
print(f'4. feladat\nA tó legnagyobb mélysége: {maxim} dm\nA legmélyebb helyek sor-oszlop koordinátái:\n{" ".join(koordinatak)}')

# 5

def keruletbe(a, b):
    kim = 0
    if b and to[a][b] and not to[a][b-1]:
            kim += 1
    if a and to[a][b] and not to[a-1][b]:
            kim += 1
    if to[a][b] != to[a][-1] and to[a][b] and not to[a][b+1]:
            kim += 1
    if to[a] != to[-1] and to[a][b] and not to[a+1][b]:
            kim += 1
    return kim

partvonalak = 0
for i in range(sorok):
     for k in range(oszlopok):
        partvonalak += keruletbe(i, k)
print(f'5. feladat\nA tó partvonala {partvonalak} m hosszú')

# 6
oszlopazon = int(input('6. feladatA vizsgált szelvény oszlopának azonosítója='))
kimenet = open('Stein Tünde/érettségi/idegen/2021infemelttav_iny/diagram.txt', 'w', encoding='utf-8')
for i in range(sorok):
    #print(to[i][oszlopazon-1] , int(to[i][oszlopazon-1]/10))
    kimenetvaltozo = f'{(i+1):02d} {"*"*int(round((to[i][oszlopazon-1]/10), 0))}'
    print(kimenetvaltozo, file=kimenet)


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