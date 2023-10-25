korongok = []
for i in range(1, 26):
    korongok.append(i)
oszlopok_szama = int(input('Oszlopok száma: '))
oszlopok_tartalma = []
for i in range(oszlopok_szama):
    a = input(f'{i+1}. oszlop elemei növekvő sorrendben: ')
    adat = a.strip().split(', ')
    for i in range(len(adat)):
        adat[i] = int(adat[i])
        for i in range(len(adat)):
            for i in range(len(adat)):
                if adat[i] > adat[i+1]:
                    adat[i], adat[i+1] = adat[i+1], adat[i]

    oszlopok_tartalma.append(adat)
print(f'Az oszlopok száma: {oszlopok_szama}')
szabad_korongok =[]
for i in range(oszlopok_szama):
    b = []
    b.append(oszlopok_tartalma[i])
    print(f'{i+1}. oszlop: {b}')
    for i in range(len(b)):
        for k in range(len(korongok)):
            if b[i] == korongok[k]:
                szabad_korongok.append(b[i])
print(f'Szabad korongok: {szabad_korongok}')
