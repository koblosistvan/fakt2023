forras = open('dobozok.txt', mode='r', encoding='utf-8')

dobozok = []
dobozok_ajandekszama = []

forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    dobozok_ajandekszama.append(int(adat[0]))
    dobozok.append(sor.strip().split(' '))

forras.close()
for i in range(len(dobozok)):
    szama = dobozok[i][0]
    dobozok[i].remove(szama)
    for j in range(len(dobozok[i])):
        dobozok[i][j] = int(dobozok[i][j])

# 2. feladat
atlag = sum(dobozok_ajandekszama) // len(dobozok_ajandekszama)

if sum(dobozok_ajandekszama) % atlag == 0:
    print('A játékokat egyenletesen el lehet osztani a dobozokban. ')
else:
    print('A játékokat nem lehet egyenletesen elosztani a dobozokba.')

print(f'Játékok dobozonkénti átlagos száma: {atlag}')

#3. feladat
maxdobozok = []
legnagyobb = max(dobozok_ajandekszama)

for i in range(len(dobozok_ajandekszama)):
    if max(dobozok_ajandekszama) == dobozok_ajandekszama[i]:
        maxdobozok.append(i+1)

print(f'Legtöbb játék egy dobozban ({legnagyobb} db) a következő dobozokban volt:{maxdobozok}')

#4. feladat
osszes = []
adott_ajandek_szaml = 0

for i in range(1, 16):
    for j in range(len(dobozok)):
        for a in range(len(dobozok[j])):
            if dobozok[j][a] == i:
                adott_ajandek_szaml += 1
    osszes.append(adott_ajandek_szaml)
    adott_ajandek_szaml = 0


legtobb = max(osszes)
legtobb_dobozoai = []

for i in range(len(osszes)):
    if osszes[i] == legtobb:
        legtobb_dobozoai.append(i+1)

print(f'Legnépszerűbb játék(ok): {legtobb_dobozoai}')

#5. feladat
melyikbol = []
hanyat = []

for i in range(len(dobozok)):
    if len(dobozok[i]) > atlag:
        melyikbol.append(i+1)
        hanyat.append(len(dobozok[i])-atlag)

print('Melyik dobozokból kell elvenni:')

for i in range(len(melyikbol)):
    print(f'{melyikbol[i]}. dobozból {hanyat[i]} db játékot')

#6.feladat
uj_fajl = open('berakhato.txt', mode='w', encoding='utf-8')

berakhato = []
segedlista = []

hianyosdobozok = []
hianyosdobozok_index = []
for i in range(len(dobozok)):
    if len(dobozok[i]) < atlag:
        hianyosdobozok.append(dobozok[i])
        hianyosdobozok_index.append(i+1)

for j in range(len(hianyosdobozok)):
    for i in range(1, 16):
        if i not in hianyosdobozok[j]:
            segedlista.append(i)
    berakhato.append(segedlista)
    segedlista = []

print('A hiányos dobozokba melyik játék rakható:')
for i in range(len(berakhato)):
    print(f'{hianyosdobozok_index[i]}. doboz:{berakhato[i]}')

print('A hiányos dobozokba melyik játék rakható:', file=uj_fajl)
for i in range(len(berakhato)):
    print(f'{hianyosdobozok_index[i]}. doboz:{berakhato[i]}', file=uj_fajl)

#uj_fajl.close()
#print '' és [] nélkül