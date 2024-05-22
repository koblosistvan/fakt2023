forrás = open('Bogdán_Samu\órai\IMDB\imdb.txt')
forrás.readline()
év = []
időtartam = []
értékelés = []
rendező = []
bevétel = []
cím = []
for i in forrás:
    sor = i.strip().split('\t')
    év.append(int(sor[0]))
    időtartam.append(int(sor[1]))
    értékelés.append(float(sor[2]))
    rendező.append(sor[3])
    bevétel.append(int(sor[4]))
    cím.append(sor[5])
forrás.close()

print('\n'+'1. feladat'+'\n'+f'{len(év)} film adatai vannak az állományban.')

print('\n'+'2. feladat'+'\n'+f'Az első film megjelenésének éve {min(év)}.')

print('\n'+'3. feladat')
if max(időtartam) > 120:
    x = 0
    for i in időtartam:
        if időtartam[i] > 120:
            x += 1
    print(f'{x} film van, ami hosszabb két óránál.')
else:
    print('Nincs két óránál hosszabb film.')

print('\n'+'4. feladat')
for i in range(len(értékelés)):
    if értékelés[i] > 9:
        print('Van olyan film, ami 9-es értékelésnél magasabb pontszámot kapott')
        break
else:
    print('Nincs olyan film, ami 9-es értékelésnél magasabb pontszámot kapott')

print('\n'+'5. feladat'+'\n'+f'A legmagasabb értékelés {max(értékelés)} pont.')

print('\n'+'6. feladat')
értékelések = list(set(értékelés))
értékelések.sort()
x = []
for i in range(len(értékelések)):
    x.append(int(értékelés.count(értékelések[i])))
for i in range(len(x)):
    print(f'{értékelések[i]} pont - {x[i]} film')

print('\n'+'7. feladat')
if x[-1] == 1:
    id = értékelés.index(értékelések[-1])
    print(f'A legjobb értékelést kapott filmet {rendező[id]} rendezte.')
else:
    print('A legjobb értékelést kapott filmek rendezői:')
    for i in range(len(értékelés)):
        if értékelés[i] == értékelések[-1]:
            print(f'- {rendező[i]}')

print('\n'+'8. feladat')
r = input('Rendező neve: ')
r1 = (str((r.strip().split(' '))[-1]) + '.txt').lower()
lista = open(f'Bogdán_Samu\órai\IMDB\{r1}', 'w')
for i in range(len(rendező)):
    if rendező[i] == r:
        lista.write(f'{cím[i]} ({év[i]}) - {időtartam[i]} perc'+'\n')
lista.close()

print('\n'+'90. feladat')