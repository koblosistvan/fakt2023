# 1
forras = open('Stein Tünde/érettségi/info/2020infemeltokt/lista.txt', 'r', encoding='utf-8')
datum = []
cim = []
epizod = []
ido = []
latta = []
sorszam = 0
for i in forras:
    sor = i.strip().split('\n')
    if (sorszam+1) % 5 == 1:
        datum.append(sor[0])
    elif (sorszam+1) % 5 == 2:
        cim.append(sor[0])
    elif (sorszam+1) % 5 == 3:
        epizod.append(sor[0])
    elif (sorszam+1) % 5 == 4:
        ido.append(int(sor[0]))
    else:
        latta.append(int(sor[0]))
    sorszam += 1
forras.close()

# 2
counter = 0
for i in datum:
    if i != 'NI':
        counter += 1
print(f'2. feladat\nA listában {counter} db vetítési dátummal rendelkező epizód van. ')

# 3
hanyatlatott = 0
perc = 0
for i in range(len(latta)):
    if latta[i]:
        hanyatlatott += 1
        perc += ido[i]
print(f'3. feladat\nA listában lévő epizódok {round(hanyatlatott/len(latta)*100, 2)}%-át látta.')

# 4
napokszama = int(perc/60/24)
perc -= napokszama*60*24
ora = int(perc/60)
perc -= ora*60
print(f'4. feladat\nSozatnézéssel {napokszama} napot {ora} órát és {perc} percet töltött. ')

# 5
bekert_datum = input(f'5. feladat\nAdjon meg egy dátumot! Dátum= ')
for i in range(len(datum)):
    if datum[i] != 'NI' and datum[i] <= bekert_datum and not latta[i]:
        print(f'{epizod[i]} {cim[i]}')

# 6
def Hetnapja(ev, ho, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo'] 
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4] 
    if ho < 3:
        ev -= 1
    hetnapja = napok[int(ev + ev/4 - ev/100 + ev/400 + honapok[ho-1] + nap) % 7]
    return hetnapja

#7
hetnapja = input(f'7. feladat\nAdja meg a hét egy napját (például cs)! Nap= ')
aznapvetitik = []
kerultadasba = False
for i in range(len(datum)):
    if datum[i] != 'NI':
        seged = datum[i].split('.')
        if Hetnapja(int(seged[0]), int(seged[1]), int(seged[2])) == hetnapja and cim[i] not in aznapvetitik:
            print(cim[i])
            aznapvetitik.append(cim[i])
            kerultadasba = True
if not kerultadasba:
    print('Az adott napon nem kerül adásba sorozat.')

sorozatok = list(set(cim))
kimenetlista = [[ [] for k in range(3) ] for i in range(len(sorozatok))]
kimenet = open('Stein Tünde/érettségi/info/2020infemeltokt/summa.txt', 'w', encoding='utf-8')
for i in range(len(sorozatok)):
    kimenetlista[i][0] = sorozatok[i]
    kimenetlista[i][1] = 0
    kimenetlista[i][2] = 0
for i in range(len(cim)):
    for k in range(len(kimenetlista)):
        if cim[i] == kimenetlista[k][0]:
            kimenetlista[k][1] += ido[i]
            kimenetlista[k][2] += 1
for i in range(len(kimenetlista)):
    print(' '.join(str(a) for a in kimenetlista[i]), file=kimenet)




"""2. feladat 
A listában 202 db vetítési dátummal rendelkező epizód van. 
3. feladat 
A listában lévő epizódok 45,66%-át látta. 
4. feladat 
Sorozatnézéssel 2 napot 15 órát és 32 percet töltött. 
5. feladat 
Adjon meg egy dátumot! Dátum= 2017.10.18 
7x01 The Fable 
7x02 The Fable 
15x04 Military Police 
5x03 Spy School 
5x04 Spy School 
4x04 The Elite Minds 
7. feladat 
Adja meg a hét egy napját (például cs)! Nap= cs 
The Hospital 
Spectacular Power 
Upper Story 
Chicago Flame 
Shrinktime"""
