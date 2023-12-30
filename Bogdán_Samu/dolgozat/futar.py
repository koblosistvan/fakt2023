forrás = open('futar.txt')
utak = int(forrás.readline())
nap = []
fuvar = []
út = []
for i in forrás:
    x = i.strip().split(' ')
    nap.append(int(x[0]))
    fuvar.append(int(x[1]))
    út.append(int(x[2]))
forrás.close()

print('Adatok beolbasása...' + '\n' + f'A futar.txt fájlból beolvastam {utak} sort.')

print('\n' + '1. feladat')
x = út.index(max(út))
print(f'A leghosszabb út: {nap[x]}. nap, {fuvar[x]}. fuvar - {út[x]} km.')

print('\n' + '2. feladat')
x = 0
for i in range(utak):
    if nap[i] == 3:
        x += út[i]
print(f'A harmadik napon összesen {x} km-t tett meg.')

print('\n' + '3. feladat')
x = 0
for i in range(utak):
    if nap[i] == 4:
        x += fuvar[i]
print(f'A negyedik napon {x} fuvart teljesített.')

print('\n' + '4. feladat')
if max(út) > 20:
    x = 'volt'
else:
    x = 'nem volt'
print(f'A futárnak {x} 20 km-nél hosszabb útja.')

kimenet = open('futar-kimenet.txt', 'w', encoding='utf-8')
kimenet.write('Napi első fuvarok:' + '\n')
fuvarok = [0, 0, 0, 0, 0, 0, 0]
napok = [1, 2, 3, 4, 5, 6, 7]
for i in range(utak):
    if fuvar[i] == 1:
        fuvarok[nap[i]-1] = út[i]
for i in range(len(fuvarok)):
    if fuvarok[i] == 0:
        pass
    else:
        kimenet.write(f'{napok[i]}. nap: {fuvarok[i]} km' + '\n')
kimenet.close()
