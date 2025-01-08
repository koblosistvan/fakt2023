def kiiras(lista):
    lista2 = lista.copy()
    for index in range(len(lista2)):
        lista2[index] = str(lista2[index])
    return ' '.join(lista2)


# 1
forras = open('dobozok.txt', 'r', encoding='utf-8')
szamok = forras.readline()
dobozok = []
darabszamok = []
for sor in forras:
    i = sor.strip().split(' ')
    doboz = []
    darabszamok.append(int(i[0]))
    for k in range(int(i[0])):
        doboz.append(int(i[k+1]))
    dobozok.append(doboz)
forras.close()

# 2
atlag = int(sum(darabszamok)/len(dobozok))
if sum(darabszamok) % len(dobozok):
   lehete = 'nem lehet egyenletesen elosztani'
else:
    lehete = 'el lehet osztani egyenletesen'
print(f'A játékokat {lehete} a dobozokban.\n'
      f'Játékok dobozonkénti átlagos száma: {atlag}')

# 3
legtobb = max(darabszamok)
print(f'Legtöbb játék egy dobozban {legtobb} a következő dobozokban volt:')
for i in range(len(darabszamok)):
    if darabszamok[i] == legtobb:
        print(kiiras(dobozok[i]))

# 4
jatekdarab = [0] * int(szamok.split(' ')[1])
for i in dobozok:
    for k in i:
        jatekdarab[k-1] += 1
legnepszerubb = max(jatekdarab)
legnepszerubbek = []
for i in range(len(jatekdarab)):
    if jatekdarab[i] == legnepszerubb:
        legnepszerubbek.append(i+1)
print(f'Legnépszerűbb játék(ok): {kiiras(legnepszerubbek)}')

# 5
hianyos6 = []
print('Melyik dobozokból kell elvenni:')
for i in range(len(darabszamok)):
    tobblet = darabszamok[i]-7
    if tobblet > 0:
        print(f'{i+1}. dobozból {tobblet} db játékot')
    else:
        hianyos6.append(i)


# 6
print('A hiányos dobozokba melyik játék rakható:')
for i in range(len(dobozok)):
    if i in hianyos6:
        megnincs = []
        for k in range(int(szamok.split(' ')[1])):
            if (k+1) not in dobozok[i]:
                megnincs.append(k+1)
        print(f'{i+1}. doboz: {kiiras(megnincs)}')
