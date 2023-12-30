forras = open('banki napok bemenet', 'r', encoding='utf-8')
elso_sor = forras.readline().strip().split(' ')
napok_szama = int(elso_sor[0])
belepesek_szama = int(elso_sor[1])
dolgozok = []
napok = []
for i in forras:
    dolgozok_lista = i.strip().split(' ')[0]
    napok_lista = i.strip().split(' ')[1]
    dolgozok.append(int(dolgozok_lista))
    napok.append(int(napok_lista))

print('a feladat')
for i in set(dolgozok):
    if i in dolgozok:
        belepesek = dolgozok.count(i)
        print(f'A(z) {i} azonosítójú dolgozó {belepesek} alkalommal lépett a páncélterembe.\n{i} - > {belepesek}')

print('\nb feladat')
for i in set(napok):
    nap = []
    for k in range(belepesek_szama):
        if napok[k] == i:
            nap.append(dolgozok[k])
    if bool(nap):
        for k in set(dolgozok):
            if bool(nap.count(k)):
                print(f'A(z) {i}. napon a {k} azonosítójú alkalmazott {nap.count(k)} alkalommal lépett be.')

print('\nc feladat')
for i in set(napok):
    nap = []
    volt_e = 0
    for k in range(belepesek_szama):
        if napok[k] == i:
            nap.append(dolgozok[k])
    for k in set(dolgozok):
        if k in dolgozok:
            volt_e += 1
    if volt_e > 1:
        print(f'A(z) {i}. napon több dolgozó is belépett.')

print('\nd feladat')
for i in range(napok_szama):
    nap = []
    for k in range(belepesek_szama):
        if napok[k] == i+1:
            nap.append(dolgozok[k])
    if not bool(nap) or len(nap) == 1:
        print(f'A(z) {i+1}. napon nem lépett be 1-nél több alkalmazott.')
