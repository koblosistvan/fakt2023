forras = open('futar.txt', mode='r', encoding='utf-8')
utak_szama = int(forras.readline())
napok = []
utsorszam = []
uthossz = []
for i in forras:
    adat = i.strip().split(' ')
    napok.append(int(adat[0]))
    utsorszam.append(int(adat[1]))
    uthossz.append(int(adat[2]))
forras.close()

print(f'1. feladat:\nA leghosszabb út: {napok[uthossz.index(max(uthossz))]}. nap, {uthossz.index(max(uthossz))}. fuvar - {max(uthossz)} km.\n')

ossz_ut_3 = 0
for i in range(len(napok)):
    if napok[i] == 3:
        ossz_ut_3 += napok[i]
print(f'2. feladat:\nA harmadik napon összesen {ossz_ut_3} km-t tett meg.\n')

print(f'3. feladat:\nA negyedik napon {napok.count(4)} fuvart teljesített.\n')

_20kmnel_hosszabb = 0
for i in range(len(napok)):
    if uthossz[i] > 20:
        _20kmnel_hosszabb += 1
        break
print('4. feladat:')
if bool(_20kmnel_hosszabb):
    volte = ''
else:
    volte = 'nem '
print(f'A futárnak {volte}volt 20 km-nél hosszabb útja.')

kimenet = open('futár-kimenet.txt', mode='w', encoding='utf-8')
print('Napi első fuvarok:', file=kimenet)
for i in range(len(napok)):
    if utsorszam[i] == 1:
        print(f'{napok[i]}. nap: {uthossz[i]} km', file=kimenet)
