class Meres:
    def __init__(self, ora, perc, mp, idotartam, honnan):
    # ora: int, perc: int ~ nem változtat semmin
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.idotartam = 3600/idotartam
        self.honnan = honnan
        self.hova = 'Felső város' if honnan == 'A' else 'Alsó város'

    def ido_mp(self):
        return self.ora*3600 + self.perc*60 + self.mp

forgalom = []
forras = open('forgalom.txt', mode='r', encoding='utf-8')
forras.readline()

# 1. feladat
for i in forras:
    adat = i.strip().split(' ')
    forgalom.append(Meres(ora=int(adat[0]), perc=int(adat[1]), mp=int(adat[2]), idotartam=int(adat[3]), honnan=adat[4]))
    # perc=, ora= stb nem kötelező, nem ad hozzá semmit :3
forras.close()

# 2. feladat
n = int(input('> '))
print(f'Az {n}-edik jármű {forgalom[n].hova} felé haladt.')

# 3. feladat
print(f'Az utolsó két autó között {forgalom[-1].ido_mp()-forgalom[-2].ido_mp()}s telt el.')
# nem ugyanafelől a város felől
