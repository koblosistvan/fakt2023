class Meres:
    def __init__(self, ora, perc, masodperc, idotartam, honnan):
        self.ora = ora
        self.perc = perc
        self.masodperc = masodperc
        self.idotartam = idotartam
        self.sebesseg = 1000/idotartam
        self.sebesseg2 = 3600/idotartam
        self.honnan = honnan
        self.honnan_str = 'Felső' if honnan == 'F' else 'Alsó'
        self.hova = 'Felső város' if honnan == 'A' else 'Alsóváros'
    def ido_mp(self):
        return self.ora * 3600 + self.perc * 60 + self.masodperc
    def __gt__(self, other):
        if self.sebesseg > other.sebesseg:
            return True
        else:
            return False

    def ido_str(self):
        return f'{self.ora:0>2d}:{self.perc:0>2d}:{self.masodperc:0>2d}'

forgalom = [ ]

forras = open('forgalom.txt', encoding='utf-8', mode='r')
forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    forgalom.append(Meres(ora=int(adat[0]), perc=int(adat[1]), masodperc=int(adat[2]), idotartam=int(adat[3]), honnan=adat[4]))
forras.close()
#1.feladat
print(forgalom[0].sebesseg2)

#2.feladat
n = int(input('Add meg melyik jármű adataira vagy kíváncsi:'))
print(f'A {n}. jármű {forgalom[n-1].hova} fele halad.')

#3.feladat
felso_fele = [meres for meres in forgalom if meres.honnan == 'A']
print(f'Az utolsó két autó között {felso_fele[-1].ido_mp() - felso_fele[-2].ido_mp()} s telt el.')

#4.feladat
for i in range(24):
    felso_felol = [meres for meres in forgalom if meres.honnan == 'F' and meres.ora == i]
    also_felol = [meres for meres in forgalom if meres.honnan == 'A'and meres.ora == i]
    if len(felso_felol) > 0 and len(also_felol) > 0:
        print(f'{i} {len(also_felol)} {len(felso_felol)}')

#5.feladat
leggyorsabb = sorted(forgalom, reverse=True)
for i in range(10):
    print(f'{leggyorsabb[i].ido_str()} {leggyorsabb[i].honnan_str} {leggyorsabb[i].sebesseg:.1f}')
