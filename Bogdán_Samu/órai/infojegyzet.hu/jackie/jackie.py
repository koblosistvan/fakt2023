jackie = open('Bogdán_Samu\\órai\\infojegyzet.hu\\jackie\\jackie.txt', 'r', encoding='utf-8')
jackie.readline()
year = []
races = []
wins = []
podiums = []
poles = []
fastests = []
for i in jackie:
    sor = i.strip().split('\t')
    year.append(int(sor[0]))
    races.append(int(sor[1]))
    wins.append(int(sor[2]))
    podiums.append(int(sor[3]))
    poles.append(int(sor[4]))
    fastests.append(int(sor[5]))
jackie.close()

print(f'3. feladat: {len(year)}')

print(f'4. feladat: {year[races.index(max(races))]}')

print('5. feladat:')
hetven = 0
hatvan = 0
for i in range(len(year)):
    if year[i] >= 1970:
        hetven += wins[i]
    else:
        hatvan += wins[i]
print(f'\t70-es évek: {hetven} megnyert verseny')
print(f'\t60-as évek: {hatvan} megnyert verseny')

print('6. feladat: jackie.html')
