forras = open("PigaiPéter\\forgalom.txt","r" ,encoding="utf-8")

class Meres:
    def __init__(self, ora, perc, mp, idotartam, honnan):
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.idotartam = idotartam
        self.sebesseg = 1000/idotartam
        self.honnan = honnan
        self.honnanstr = 'Felső' if honnan == 'F' else 'Alsó'
        self.hova = "Felső város" if honnan == "A" else "Alsó város"
    def ido_mp(self):
        return self.ora * 3600 + self.perc * 60 + self.mp
    def __gt__(self, other):
        if self.sebesseg > other.sebesseg:
            return True
        else:
            return False
    def idostr(self):
        return(f'{self.ora:0>2d}:{self.perc:0>2d}:{self.mp:0>2d}')

forgalom = []
forras.readline()
for sor in forras:
    adat = sor.strip().split(" ")
    forgalom.append(Meres(int(adat[0]), int(adat[1]), int(adat[2]), int(adat[3]), adat[4]))
forras.close

n = int(input("Melyik jármű adataid kéred?"))
print(f"Az {n}. jármű {forgalom[n-1].hova} felé haladt")

felsofele = [meres for meres in forgalom if meres.honnan == 'A']

print(f"Az utolsó két autó között {felsofele[-1].ido_mp() - felsofele[-2].ido_mp()}s telt el")

for i in range(24):
    felsofelol = [meres for meres in forgalom if meres.honnan == 'F' and meres.ora == i]
    alsofelol = [meres for meres in forgalom if meres.honnan == 'A' and meres.ora == i]
    if len(felsofelol) > 0 or len(alsofelol) > 0:
        print(i, len(felsofelol), len(alsofelol))

leggyorsabb = sorted(forgalom)
for i in range(10):
    print(f'{leggyorsabb[i].idostr()} {leggyorsabb[i].honnanstr} {leggyorsabb[i].sebesseg:.1f}')