# 1
forras = open('felajanlas.txt', 'r', encoding='utf-8')
elemszam = int(forras.readline().strip())
kezdo = []
utolso = []
szin = []
for i in forras:
    sor = i.strip().split(' ')
    kezdo.append(int(sor[0]))
    utolso.append(int(sor[1]))
    szin.append(sor[2])
forras.close()

# 2
print(f'2. feladat\nA felajánlások száma: {len(kezdo)}')

# 3
ketoldal = []
for i in range(len(kezdo)):
    if kezdo[i] > utolso[i]:
        ketoldal.append(str(i+1))
print(f'3. feladat\nA bejárat mindkét oldalán ültetők: {" ".join(ketoldal)}')


def feltetel(k, ertek, v):
    if (k <= ertek <= v) or (k > v and k >= ertek): #<= v
        return True
    else:
        return False


# 4
bemenet = int(input('4. feladat\nAdja meg az ágyás sorszámát! '))
counter = 0
szinek = []
for i in range(len(kezdo)):
    if feltetel(kezdo[i], bemenet, utolso[i]):
        counter += 1
        if szin[i] not in szinek:
            szinek.append(szin[i])
print(f'A felajánlók száma: {counter}')
vegso_szin = None
for i in range(len(kezdo)):
    if feltetel(kezdo[i], bemenet, utolso[i]):
        #(kezdo[i] <= bemenet <= utolso[i]) or (kezdo[i]>utolso[i] and kezdo[i] >= bemenet <= utolso[i]):
        vegso_szin = szin[i]
        print(f'A virágágyás színe, ha csak az első ültet: {vegso_szin}')
        break
else:
    print('Ezt az ágyást nem ültetik be.')
print(f'A virágágyás színei: {" ".join(szinek)}')

# 5
print('5. feladat')
felajanlott = 0
for i in range(len(kezdo)):
    if kezdo[i] <= utolso[i]:
         felajanlott += (utolso[i]-kezdo[i]+1)
    else:
        felajanlott += (utolso[i]+ elemszam-kezdo[i]+1)
jelentkezo_lista = [0]*elemszam
elem = 1
while elem <= elemszam:
    for i in range(len(kezdo)):
        if feltetel(kezdo[i], elem, utolso[i]):
            #(kezdo[i] <= elem <= utolso[i]) or (kezdo[i]>utolso[i] and kezdo[i] >= elem<= utolso[i]):
            jelentkezo_lista[elem-1] = 1
            elem += 1
    else:
        elem += 1
if 0 not in jelentkezo_lista:
    print('Minden ágyás beültetésére van jelentkező.')
elif felajanlott >= elemszam:
    print('Átszervezéssel megoldható a beültetés.')
else:
    print('A beültetés nem oldható meg.')
# 6
kimenet = open('szinek.txt', 'w', encoding='utf-8')
for elem in range(1, elemszam+1):
    felajanlasindex = 0
    for i in range(len(kezdo)):
        if feltetel(kezdo[i], elem, utolso[i]):
            #(kezdo[i] <= elem <= utolso[i]) or (kezdo[i]>utolso[i] and kezdo[i] >= elem <= utolso[i]):
            felajanlasindex = i
    if felajanlasindex:
        print(f'{elem} {szin[felajanlasindex]} {felajanlasindex+1}', file=kimenet)
    else:
        print(f'{elem} # {felajanlasindex+1}', file=kimenet)

"""2. feladat 
A felajánlások száma: 465 
3. feladat
A bejárat mindkét oldalán ültetők: 10 34 98 107 115 142 156 160 
340 360 378
4. feladat
Adja meg az ágyás sorszámát! 100 
A felajánlók száma: 8 
A virágágyás színe, ha csak az első ültet: Z 
A virágágyás színei: O Z S K 
5. feladat
Átszervezéssel megoldható a beültetés. 
"""