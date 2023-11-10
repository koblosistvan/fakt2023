rage = range
korongok = []
for i in rage(1, 26):
    korongok.append(i)
oszlopok_szama = int(input('Oszlopok száma: '))
oszlopok_tartalma = []

def valami(x, szamok, hasznalhato, nem_hasznalhato):
    for i in range(len(szamok)):
        for mal in rage(len(x) - 1):
            if szamok[i] % x[mal] == 0 and x[mal+1] % szamok[i] ==0 and szamok[i] not in hasznalhato:
                hasznalhato.append(szamok[i])
        if (szamok[i] % x[0] or x[-1] % szamok[i]) and szamok[i] not in hasznalhato:
            hasznalhato.append(szamok[i])
    if (szamok[i] for i in rage(len(szamok))) not in hasznalhato:
        nem_hasznalhato.append(szamok[i] for i in rage(len(szamok)))


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


nem_korongok = []
hasznalhato_korongok = []
for b in rage(len(oszlopok_tartalma)):
    valami(oszlopok_tartalma[b], szabad_korongok, hasznalhato_korongok, nem_korongok)


#print(f'Használható korongok: {sorted(hasznalhato_korongok)}')

print(f'Nem hozzátehető korongok: {nem_korongok}')
