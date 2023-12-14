forrás = open('banki napok.txt', mode='r', encoding='utf-8')

forrás.readline()

dolgozók = []
napok = []
for sor in forrás:
    adat = sor.strip().split(' ')
    dolgozók.append(int(adat[0]))
    napok.append(int(adat[1]))

print('a. feladat')
dologozó_kódok = set(dolgozók)
for d_id in dologozó_kódok:
    print(f'Az {d_id}. dolgozó {dolgozók.count(d_id)} alkalommal lépett be.')

mindketten = []
print('\nb. feladat')
for nap in set(napok):
    print(f'{nap}. nap:', end=' ')
    belépők = 0
    for d_id in dologozó_kódok:
        belépések_száma = 0
        for i in range(len(dolgozók)):
            if dolgozók[i] == d_id and napok[i] == nap:
                belépések_száma += 1
        print(f'{belépések_száma}', end=' ')
        if belépések_száma > 0:
            belépők += 1
    print()
    if belépők == len(set(dolgozók)):
        mindketten.append(str(nap))

print('\nc. feladat')
print(f'A {", ".join(mindketten)} napokon mindenki belépett.')
