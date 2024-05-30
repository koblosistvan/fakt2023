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

print(f'5. feladat: Napi kölcsönzések száma: {len(név)}')

nev = input('6. feladat: Kérek egy nevet: ')
if név.count(nev) == 0:
    print('Nem volt ilyen nevű kölcsönző!')
else:
    print(f'\t{nev} kölcsönzései:')
    for i in range(len(név)):
        if név[i] == nev:
            print(f'\t{eó[i]:02d}:{ep[i]:02d}-{vó[i]:02d}:{vp[i]:02d}')

idő = input('7. feladat: Adjon meg egy időpontot óra:perc alakban: ')
óra = idő.strip().split(':')[0]
perc = idő.strip().split(':')[1]
idő = int(str(óra) + str(perc))
for i in range(len(név)):
    if int(str(eó[i]) + str(ep[i])) <= idő and int(str(vó[i]) + str(vp[i])) >= idő:
        print(f'\t{eó[i]:02d}:{ep[i]:02d}-{vó[i]:02d}:{vp[i]:02d} : {név[i]}')
