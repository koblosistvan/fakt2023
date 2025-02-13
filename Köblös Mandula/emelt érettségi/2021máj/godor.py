forras = open('melyseg.txt', mode='r', encoding='utf-8')

melyseg = []

for sor in forras:
    melyseg.append(int(sor))

forras.close()

print('1. feladat')
print(f'A féjl adatainak száma: {len(melyseg)}')

print('2. feladat')
tavolsag = int(input('Adjon meg egy távolságértéket! '))
print(f'Ezen a helyen a felszín {melyseg[tavolsag]} méter mélyen van.')

print('3. feladat')
erintetlen = 0
for i in range(len(melyseg)):
    if melyseg[i] == 0:
        erintetlen += 1
print(f'Az érintetlen terület aránya {erintetlen/len(melyseg):0.2%}')

kiiras = open('godrok.txt', mode='w', encoding='utf-8')

for i in range(len(melyseg)):
    if melyseg[i] != 0:
