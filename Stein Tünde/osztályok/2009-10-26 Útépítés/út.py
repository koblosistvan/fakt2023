class Meres:
    def __init__(self, ora, perc, mp, idotartam, honnan):
    # ora: int, perc: int ~ nem változtat semmin
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.idotartam = idotartam
        self.sebesseg = 1000/idotartam
        self.honnan = honnan
        self.honnan_str = 'Felso' if honnan == 'F' else 'Alsó'
        self.hova = 'Felső város' if honnan == 'A' else 'Alsó város'

    def ido_mp(self):
        return self.ora*3600 + self.perc*60 + self.mp

    def __gt__(self, other):
        if self.idotartam > other.idotartam:
            return True
        else:
            return False
    def ido_str(self):
        return f'{self.ora:0>2d}:{self.perc:0>2d}:{self.mp:0>2d}'
    def kilep_mp(self):
        return self.ido_mp() + self.idotartam
    def kilep_str(self):
        ora = self.kilep_mp() // 3600
        perc = self.kilep_mp() % 3600 // 60
        mp = self.kilep_mp() % 60
        return f'{ora}:{perc}:{mp}'


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
felso_fele = [meres for meres in forgalom if meres.honnan == 'A']
print(f'Az utolsó két autó között {felso_fele[-1].ido_mp()-felso_fele[-2].ido_mp()}s telt el.')

# 4. feladat
for i in range(24):
    felso_felol = []
    also_felol = []
    felso_felol = [meres for meres in forgalom if meres.honnan == 'F' and meres.ora == i]
    also_felol = [meres for meres in forgalom if meres.honnan == 'A' and meres.ora == i]
    if len(felso_felol) > 0 or len(also_felol) > 0:
        print(f'{i} {len(also_felol)} {len(felso_felol)}')
    # for k in range(len(forgalom)):
        # i f forgalom[k].honnan == "F" and forgalom[k].ora == i:
            # felso_felol.append(forgalom[k].ora)
        # elif forgalom[k]. honnan == 'A' and forgalom[k].ora == i:
            # also_felol.append(forgalom[k].ora)

# 5. feladat

# leggyorsabb = sorted(forgalom)
# for i in range(10):
    # print(leggyorsabb[-1-i].idotartam)

leggyorsabb = sorted(forgalom, reverse=True)
for i in range(10):
    print(leggyorsabb[i].idotartam)
    print(f'{leggyorsabb[i].ido_str} {leggyorsabb[i].honnan_str} {leggyorsabb[i].sebesseg}')

# 6. feladat

also_fele = [meres for meres in forgalom if meres.honnan == 'F']
idopont_mp = 0
idopont_str = ''
for i in range(len(also_fele)):
    if also_fele[i].kilep_mp() > idopont_mp:
        print(also_fele[i].kilep_str())
        idopont_mp = also_fele[i].kilep_mp()
        idopont_str = also_fele[i].kilep_str()
    else:
        print(idopont_str)

