class jack:
    def __init__(self, year, races, win, podiums, fastests):
        self.year=year
        self.races=races
        self.win=win
        self.podiums=podiums
        self.fastests=fastests

infok=[]

forras=open('jack.txt', mode='r', encoding='utf-8')

forras.readline()

for sor in forras:
    adat=sor.strip().split('\t')
    infok.append(jack(year=int(adat[0]), races=int(adat[1]), win=int(adat[2]), podiums=int(adat[3]), fastests=int(adat[4])))

forras.close()

#1.feladat

print(f'Az állomány {len(infok)} adatot tartalmaz')

#2.feladat



legtobb=sorted(infok, reverse=True, key=lambda a: a.races)


for i in range(len(infok)):
    print(legtobb[0].races)
    break