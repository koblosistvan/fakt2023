forras = open('banki napok bemenet', 'r', encoding='utf-8')
napok_szama = forras.readline().strip().split(' ')[0]
belepesek_szama = forras.readline().strip().split(' ')[1]
dolgozok = []
napok = []
for i in forras:
    dolgozok_lista = i.strip().split(' ')[0]
    napok_lista = i.strip().split(' ')[1]
    dolgozok.append(int(dolgozok_lista))
    napok.append(int(napok_lista))
dolgozok_s = set(dolgozok)

print('a feladat')
for i in dolgozok_s:
    if i in dolgozok:
        belepesek = dolgozok.count(i)
        print(f'A(z) {i} azonosítójú dolgozó {belepesek} alkalommal lépett a páncélterembe.\n{i} - > {belepesek}')

print('\nb feladat')
for i in list(set(napok)):
    szamlalo = 0
    for k in napok.count(i):
        szamlalo +=
        print('1. napon a(z) 1 azonosítójú dolgozó 3 alkalommal lépett be.')

print('\nc feladat')
for i in range(len(napok)-1):
    tobb_belepes = False
    for k in range(len(napok)-1):
        if napok[i] == napok[i+1] and dolgozok[k] == dolgozok[k+1]:
            tobb_belepes = True
    if bool(tobb_belepes):
        print(f'{napok[i]}. napon belépett egynél több alkalmazott.')
    else:
        print(f'{napok[i]}. napon nem lépett be egynél több alkalmazott.')

