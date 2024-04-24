class Meres:
    def __init__(self, ora, perc, masodperc, idotartam, honnan):
        self.ora = ora
        self.perc = perc
        self.masodperc = masodperc
        self.idotartam = idotartam
        self.sebesseg = 3600/idotartam
        self.honnan = honnan
        self.hova = 'Felső város' if honnan == 'A' else 'Alsóváros'
    def ido_mp(self):
        return self.ora * 3600 + self.perc * 60 + self.masodperc

forgalom = [ ]

forras = open('forgalom.txt', encoding='utf-8', mode='r')
forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    forgalom.append(Meres(ora=int(adat[0]), perc=int(adat[1]), masodperc=int(adat[2]), idotartam=int(adat[3]), honnan=adat[4]))
forras.close()
print(forgalom[0].sebesseg)

#2.feladat
n = int(input('Add meg melyik jármű adataira vagy kíváncsi:'))
print(f' A {n}. jármű {forgalom[n-1].hova} fele halad.')

#3.feladat
print(f'Az utolsó két autó között {forgalom[-1].ido_mp() - forgalom[-2].ido_mp()} s telt el.')
