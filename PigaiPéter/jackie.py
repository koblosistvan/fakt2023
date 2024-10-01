class Jackie:
    def __init__(self, year: int, races: int, wins: int, podiums:int, poles:int, fastests: int):
        self.year = year
        self.races = races
        self.wins = wins
        self.podiums = podiums
        self.poles = poles
        self.fastests = fastests
    
f = open("PigaiPéter\\jackie.txt", mode='r', encoding='utf-8')
data = []
f.readline()
for i in f:
    sor = i.strip().split('\t')
    data.append(Jackie(year=int(sor[0]), races=int(sor[1]), wins=int(sor[2]), podiums=int(sor[3]), poles=int(sor[4]), fastests=int(sor[5])))
f.close()
#
print(f'3. feladat:{len(data)}')
#
legtobbv = data[0].races
for i in range(len(data)):
    if legtobbv < data[i].races:
        legtobbv = data[i].races
print(f'4. feladat:{legtobbv}')

#
hetven = 0
hatvan = 0
for i in range(len(data)):
    if data[i].year > 1969:
        hetven += data[i].wins
    else:
        hatvan += data[i].wins
print(f'5. feladat:\n\t 60-as évek:{hatvan}\n\t 70-es évek:{hetven}')

#
