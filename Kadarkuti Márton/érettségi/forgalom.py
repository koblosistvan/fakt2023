from typing import Any

class Meres:
    def __init__(self, ora, perc, mp, sebesseg, honnan):
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.sebesseg = sebesseg
        self.honnan = honnan
        self.honnanf = 'Felső város' if (honnan=='A') else 'Alsó város'

    def ido(self):
        return self.ora*60*60 + self.perc*60 + self.mp
    
    def __gt__(self, other):
        if self.sebesseg >= other.sebesseg:
            return True
        else:
            return False
    def idof(self):
        return f'{self.ora}:{self.perc}:{self.mp}'

forgalom = []
forras = open('Kadarkuti Márton\\érettségi\\forgalom.txt','r',encoding='utf-8')
forras.readline()

for sor in forras:
    adat = sor.strip().split(' ')
    forgalom.append( Meres(int(adat[0]), int(adat[1]), int(adat[2]), int(adat[3]), adat[4]))
forras.close()

n = int(input("Hányadik jármű? > "))
print(f"A {n}. jármű {forgalom[n-1].honnanf3
} felé haladt.")

print(f'Az utolsó két jármű {abs( forgalom[-1].ido() - forgalom[-2].ido() )}s külömbséggel érte el az útszakaszt.')

leggyorsabb = sorted(forgalom, reverse=True)
for i in range(10):
    print(f'{leggyorsabb[i].idof} {leggyorsabb[i].honnanf} {leggyorsabb[i].sebesseg:.1f}')


also_fele = [meres for meres in forgalom if meres.honnan=='F']

