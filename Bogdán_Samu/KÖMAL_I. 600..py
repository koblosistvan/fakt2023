n = int(input('Az oszlopok száma: '))

korongok = []
szabad = []
stóc = []

for i in range(n):
    sor = input(f'{i+1}. oszlop: ').strip().split(' ')
    for i in range(len(sor)):
        sor[i] = int(sor[i])
    korongok = korongok + sor
    stóc.append(sor)
for i in range(25):
    szabad.append(i+1)

for i in range(len(korongok)):
    if korongok[i] in szabad:
        szabad.remove(int(korongok[i]))

szabad.sort()
print(f'Szabad korongok: {" ".join(map(str, szabad))}')

nem_korong = szabad
id1 = 0
id2 = 0
for i in range(len(stóc)):
    if len(stóc[i]) == 1:
        while id2 < len(szabad):
            if (stóc[i][0] % szabad[id2] == 0) or (szabad[id2] % int(stóc[i][0]) == 0):
                nem_korong.remove(szabad[id2])
            else:
                id2 += 1
    elif len(stóc[i]) > 1:
        while id2 < len(szabad):
            if (stóc[i][0] % szabad[id2] == 0) or (stóc[i][id1+1] % szabad[id2] == 0 and szabad[id2] % int(stóc[i][id1]) == 0) or (szabad[id2] % int(stóc[i][-1]) == 0):
                nem_korong.remove(szabad[id2])
            else:
                id1 += 1
                if id1 == len(stóc[i])-1:
                    id1 = 0
                    id2 += 1
        id1 = 0
        id2 = 0

print(f'Nem hozzátehető korongok: {" ".join(map(str, nem_korong))}')
