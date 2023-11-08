oszlopok_szama = int(input('Add meg hány oszlop van:'))

oszlopok = []
haszn_korongok = []
szabad_korongok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

for i in range(oszlopok_szama):
    sor = input(f'{i+1}. oszlop: ').strip().split(' ')
    for i in range(len(sor)):
        sor[i] = int(sor[i])
    haszn_korongok = haszn_korongok + sor
    oszlopok.append(sor)

for j in range(len(haszn_korongok)):
    if szabad_korongok[j] in haszn_korongok:
        szabad_korongok.remove(int(haszn_korongok[j]))