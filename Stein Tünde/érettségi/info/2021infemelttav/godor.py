# 1
forras = open('Stein Tünde/érettségi/info/2021infemelttav/melyseg.txt', 'r', encoding='utf-8')
melysegek = []
for i in forras:
    sor = i.strip()
    melysegek.append(int(sor))
forras.close()
l = len(melysegek)
print(f'1. feladat\nA fájl adatainak száma: {l}')

# 2
tavolsagertek = int(input(f'2. feladat\nAdjon meg egy távolságértéket! '))
melysegertek = melysegertek
print(f'Ezen a helyen a felszín {melysegertek} méter mélyen van. ')

# 3
counter = 0
for i in melysegek:
    if not i:
        counter += 1
print(f'3. feladat\nAz érintetlen terület aránya {round(counter/l*100, 2)}%')

# 4
kimenet = open('Stein Tünde/érettségi/info/2021infemelttav/godrok.txt', 'w', encoding='utf-8')
kimenetlista = []
indexlista = []
for i in range(len(melysegek)):
    if i and melysegek[i] and not melysegek[i-1]:
        kimenetlista.append([])
        indexlista.append([])
        kimenetlista[-1].append(str(melysegek[i]))
        indexlista[-1].append(i)
    elif melysegek[i]:
        kimenetlista[-1].append(str(melysegek[i]))
        indexlista[-1].append(i)
for i in kimenetlista:
    print(' '.join(i), file=kimenet)
kimenet.close()

# 5
print(f'5. feladat\nA gödrök száma: {len(kimenetlista)}')

# 6
print('6. feladat')
if not melysegertek:
    print('Az adott helyen nincs gödör.')
else:
    # a
    kezdet = []
    veg = []
    for i in range(tavolsagertek-1):
        if not melysegek[i] and melysegek[i+1]:
            kezdet.append(i+1)
    for i in range(tavolsagertek, len(melysegek)-1):
        if melysegek[i] and not melysegek[i+1]:
            veg = i
            break
    print(f'a)\nA gödör kezdete: {kezdet[-1]+1} méter, a gödör vége: {veg+1} méter.')
    # b
    folyamatosan = True
    for i in range(len(indexlista)):
        if tavolsagertek in indexlista[i]:
            maximum = max(kimenetlista[i])
            for k in range(len(kimenetlista[i])-1):
                segedki = kimenetlista[i][k]
                segedi = indexlista[i][k]
                if segedi < tavolsagertek:
                    if segedki < tavolsagertek:
                        folyamatosan = False
                        break
                    if k and segedki > melysegertek:
                        folyamatosan = False
                if segedi > tavolsagertek:
                    if segedki < tavolsagertek:
                        folyamatosan = False
                    if segedki < melysegertek:
                        folyamatosan = False
    



"""1. feladat 
A fájl adatainak száma: 694 
2. feladat 
Adjon meg egy távolságértéket! 9 
Ezen a helyen a felszín 2 méter mélyen van. 
3. feladat 
Az érintetlen terület aránya 10.09%. 
5. feladat 
A gödrök száma: 22 
6. feladat 
a) 
A gödör kezdete: 7 méter, a gödör vége: 22 méter. 
b) 
Nem mélyül folyamatosan. 
c) 
A legnagyobb mélysége 4 méter. 
d) 
A térfogata 440 m^3. 
e) 
A vízmennyiség 280 m^3. """