class Meres:
    def __init__(self, ora: int, perc: int, mp: int, idotartam:int, honnan: str):
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.idotartam = idotartam
        self.sebesseg = 1000/idotartam
        self.sebesseg2 = 3600/idotartam
        self.honnan = honnan
        self.honnan_str = 'Felső' if honnan == 'F' else 'Alsó'
        self.hova = 'Felső város' if honnan == 'A' else 'Alsó város'

    def ido_mp(self):
        return self.ora*3600 + self.perc*60 + self.mp

    def __gt__(self, other):
        if self.sebesseg > other.sebesseg:
            return True
        else:
            return False

    def ido_str(self):
        return f'{self.ora:0>2d}:{self.perc:0>2d}:{self.mp:>2d}'
    
    def kilepmp(self):
        return self.ido_mp() + self.idotartam
    
    def kilepstr(self):
        ora = self.kilepmp() // 3600
        perc = self.kilepmp() // 3600 // 60
        mp = self.kilepmp() % 60
        return f'{ora:0>2d} {perc:0>2d} {mp:0>2d}'

forgalom = []
forras = open('forgalom.txt', mode='r', encoding='utf-8')
forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    forgalom.append(Meres(ora=int(adat[0]), perc=int(adat[1]), mp=int(adat[2]), idotartam=int(adat[3]), honnan=adat[4]))
forras.close()

print(forgalom[0].sebesseg2)

# 2. feladat
n = int(input("Melyik jármű adatait kéred? "))
print(f'Az {n}. jármű {forgalom[n-1].hova} felé haladt.')

# 3. feladat
felso_fele = [meres for meres in forgalom if meres.honnan == 'A']
print(f'Az utolsó két autó között {felso_fele[-1].ido_mp() - felso_fele[-2].ido_mp()}s telt el')

# 4.feladat
for i in range(24):
    felso_felol = [meres for meres in forgalom if meres.honnan == 'F' and meres.ora == i]
    also_felol = [meres for meres in forgalom if meres.honnan == 'A' and meres.ora == i]
    if len(felso_felol) > 0 or len(also_felol) > 0:
        print(f'{i} {len(also_felol)} {len(felso_felol)}')

# 5. feladat
leggyorsabb = sorted(forgalom, reverse=True)
for i in range(10):
    print(f'{leggyorsabb[i].ido_str()} {leggyorsabb[i].honnan_str} {leggyorsabb[i].sebesseg:.1f}')
#
alsofele = [Meres for meres in forgalom if meres.honnan == 'F']
idopontmp = 0
idopontstr = ''
for i in range(len(alsofele)):
    if alsofele[i].kilepmp() > idopontmp:
        print(alsofele[i].kilepstr())
        idopontmp = alsofele[i].kilepmp()
        idopontstr = alsofele[i].kilepstr()
    else:
        print(idopontstr)
