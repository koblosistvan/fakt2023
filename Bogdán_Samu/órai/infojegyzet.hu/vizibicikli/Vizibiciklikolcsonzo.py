from math import ceil
forrás = open('Bogdán_Samu\órai\infojegyzet.hu\\vizibicikli\kolcsonzesek.txt', 'r', encoding='utf-8')
forrás.readline()
név = []
azon = []
eó = []
ep = []
vó = []
vp = []
for i in forrás:
    sor = i.strip().split(';')
    név.append(sor[0])
    azon.append(sor[1])
    eó.append(int(sor[2]))
    ep.append(int(sor[3]))
    vó.append(int(sor[4]))
    vp.append(int(sor[5]))
forrás.close()

print(f'5. feladat: Napi kölcsönzések száma: {len(név)}')

nev = input('6. feladat: Kérek egy nevet: ')
if név.count(nev) == 0:
    print(f'\t{nev} kölcsönzései:')
    print('\tNem volt ilyen nevű kölcsönző!')
else:
    print(f'\t{nev} kölcsönzései:')
    for i in range(len(név)):
        if név[i] == nev:
            print(f'\t{eó[i]:02d}:{ep[i]:02d}-{vó[i]:02d}:{vp[i]:02d}')

idő = input('7. feladat: Adjon meg egy időpontot óra:perc alakban: ')
if idő != 'x':
    óra = idő.strip().split(':')[0]
    perc = '{:02d}'.format(int(idő.strip().split(':')[1]))
    idő = int(str(óra) + str(perc))
    for i in range(len(név)):
        if int(str(eó[i]) + str('{:02d}'.format(int(ep[i])))) <= idő and int(str(vó[i]) + str('{:02d}'.format(int(vp[i])))) >= idő:
            print(f'\t{eó[i]:02d}:{ep[i]:02d}-{vó[i]:02d}:{vp[i]:02d} : {név[i]}')
else:
    print('\tFeladat átlépve')

x = 0
for i in range(len(név)):
    x += (ceil(((((vó[i] * 60) + vp[i]) - ((eó[i] * 60) + ep[i]))) / 30) * 2400)
print(f'8. feladat: A napi bevétel: {x} Ft')

f = open('Bogdán_Samu\\órai\\infojegyzet.hu\\vizibicikli\\F.txt', 'w', encoding='utf-8')
for i in range(len(név)):
    if azon[i] == 'F':
        f.write(f'{eó[i]:02d}:{ep[i]:02d}-{vó[i]:02d}:{vp[i]:02d} : {név[i]}\n')
f.close()

print('10. feladat: Statisztika')
abc = list(set(azon))
abc.sort()
for i in range(len(abc)):
    print(f'\t{abc[i]} - {azon.count(abc[i])}')
