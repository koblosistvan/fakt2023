class Meres:
    def __init__(self, ora: int, perc: int, mp: int, idotartam: int, honnan: str):
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.idotartam = idotartam
        self.sebesseg = 3600/idotartam
        self.honnan = honnan
        self.hova = 'Felső város' if honnan== 'A' else 'Alsó város'

    def ido_mp(self):
        return self.ora*3600+self.perc*60+self.mp

forgalom = []

forras = open('forgalom.txt', mode='r', encoding='utf-8')

forras.readline()

for sor in forras:
    adat = sor.strip().split(' ')
    forgalom.append(Meres(ora=int(adat[0]), perc=int(adat[1]), mp=int(adat[2]), idotartam=int(adat[3]), honnan=adat[4]))
forras.close()

print(forgalom[0].sebesseg)
#################################################

n = int(input('Add meg a adatát szeretnéd lekérdezni: '))
print(f'Az {n}.jármű {forgalom[n-1].hova} fele halad')

#################################################
print(f'Az utolsó két autó között {forgalom[-1].ido_mp()-forgalom[-2].ido_mp()}mp telt el')


