forras = open('melyseg.txt', mode='r', encoding='utf-8')

melyseg = []

for sor in forras:
    melyseg.append(int(sor))

forras.close()

print('1. feladat')
print(f'A féjl adatainak száma: {len(melyseg)}')

print('\n2. feladat')
tavolsag = int(input('Adjon meg egy távolságértéket! '))-1
print(f'Ezen a helyen a felszín {melyseg[tavolsag]} méter mélyen van.')

print('\n3. feladat')
erintetlen = 0
for i in range(len(melyseg)):
    if melyseg[i] == 0:
        erintetlen += 1
print(f'Az érintetlen terület aránya {erintetlen/len(melyseg):0.2%}')

kiiras = open('godrok.txt', mode='w', encoding='utf-8')



godrok = []
for i in range(len(melyseg)):
    if melyseg[i] != 0:
        godrok.append(melyseg[i])
    elif melyseg[i] == 0 and melyseg[i-1] != 0:
        godrok.append(melyseg[i])


for i in range(len(godrok)):
    if godrok[i] != 0:
        print(godrok[i] ,end=" " ,file=kiiras)
    else:
        print('', file=kiiras)

kiiras.close()

print('\n5.feladat')
godrok_szama = 0
for i in range(len(godrok)):
    if godrok[i] == 0:
        godrok_szama += 1
print(f'A gördök száma: {godrok_szama}')

godrok_index = []
for i in range(len(melyseg)):
    godrok_index_seged = []
    if melyseg[i] > 0:
        godrok_index_seged.append(melyseg[i])
    else:
        godrok_index.append(godrok_index_seged)
print(godrok_index)

print('\n6.feladat')
if melyseg[tavolsag] == 0:
    print('Az adott helyen nincs gödör.')