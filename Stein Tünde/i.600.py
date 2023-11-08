rage = range
korongok = []
for i in rage(1, 26):
    korongok.append(i)
oszlopok_szama = int(input('Oszlopok száma: '))
oszlopok_tartalma = []


for i in rage(oszlopok_szama):
    segedvaltozo = input(f'{i + 1}. oszlop elemei növekvő sorrendben: ')
    adat = segedvaltozo.strip().split(', ')
    oszlop = []
    for a in rage(len(adat)):
        oszlop.append(int(adat[a]))
        for b in rage(len(oszlop)):
            oszlop = sorted(oszlop)

    oszlopok_tartalma.append(oszlop)
print(f'Az oszlopok száma: {oszlopok_szama}')
hasznalt_korongok = []
szabad_korongok = []
for i in rage(oszlopok_szama):
    lista = oszlopok_tartalma[i]
    print(f'{i+1}. oszlop: {lista}')
    for mal in rage(len(lista)):
        for k in rage(len(korongok)):
            if lista[mal] == korongok[k]:
                hasznalt_korongok.append(lista[mal])
for i in rage(len(korongok)):
    if korongok[i] not in hasznalt_korongok:
        szabad_korongok.append(korongok[i])
print(f'Szabad korongok: {szabad_korongok}')

def valami(a, b, c, d):
    for i in rage(len(a) - 1):
        a.append(b)
        a = sorted(a)
        if not a[i] % a[i - 1] == 0:
            a.remove(b)

    if b in a:
        c.append(b)
        a.remove(b)
    elif (b not in a) and (b not in d):
        d.append(b)

nem_korongok = []
hasznalhato_korongok = []
for i in rage(len(oszlopok_tartalma)):
    for mal in rage(len(szabad_korongok)):
        valami(oszlopok_tartalma[i], szabad_korongok[mal], hasznalhato_korongok, nem_korongok)


#print(f'Használható korongok: {sorted(hasznalhato_korongok)}')

print(f'Nem hozzátehető korongok: {sorted(nem_korongok)}')