forras = open('jackie.txt', 'r', encoding='utf-8')

year = []
races = []
wins = []
podiums = []
poles = []
fastests = []

forras.readline()
for i in forras:
    k = i.strip().split('\t')
    year.append(int(k[0]))
    races.append(int(k[1]))
    wins.append(int(k[2]))
    podiums.append(int(k[3]))
    poles.append(int(k[4]))
    fastests.append(int(k[5]))
forras.close()

# task 3
print(f'3. feladat: {len(year)}')

# task 4
print(f'4. feladat: {year[races.index(max(races))]}')

# task 5
print('5. feladat:')
minimum = 1910
maximum = 1919
evek = 10
for k in range(9):
    megnyert = 0
    for i in range(len(year)):
        if minimum <= year[i] <= maximum:
            megnyert += races[i]
            minimum += 10
            maximum += 10
    if megnyert:
        print(f'{evek}-es évek: {megnyert} megnyert verseny')

# task 6


