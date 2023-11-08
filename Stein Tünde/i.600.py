korongok = []
for i in range(1, 26):
    korongok.append(i)
oszlopok_szama = int(input('Oszlopok száma: '))
oszlopok_tartalma = []


for i in range(oszlopok_szama):
    segedvaltozo = input(f'{i + 1}. oszlop elemei növekvő sorrendben: ')
    adat = segedvaltozo.strip().split(', ')
    oszlop = []
    for a in range(len(adat)):
        oszlop.append(int(adat[a]))
        for b in range(len(oszlop)):
            oszlop = sorted(oszlop)

    oszlopok_tartalma.append(oszlop)
print(f'Az oszlopok száma: {oszlopok_szama}')
hasznalt_korongok = []
szabad_korongok = []
for i in range(oszlopok_szama):
    lista = oszlopok_tartalma[i]
    print(f'{i+1}. oszlop: {lista}')
    for mal in range(len(lista)):
        for k in range(len(korongok)):
            if lista[mal] == korongok[k]:
                hasznalt_korongok.append(lista[mal])
for i in range(len(korongok)):
    if korongok[i] not in hasznalt_korongok:
        szabad_korongok.append(korongok[i])
print(f'Szabad korongok: {szabad_korongok}')

hasznalhato_korongok = []
nem_hasznalhato_korongok = []
for i in range(len(oszlopok_tartalma)):
    for k in range(len(oszlopok_tartalma[i])):
        if oszlopok_tartalma[i][k] not in szabad_korongok:
            nem_hasznalhato_korongok = sorted(nem_hasznalhato_korongok.append(oszlopok_tartalma[i][k]))

print(f'Nem hozzátehető korongok: {nem_hasznalhato_korongok}')
