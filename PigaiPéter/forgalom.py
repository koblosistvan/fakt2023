forras = open("PigaiPéter\\forgalom.txt","r" ,encoding="utf-8")

class Meres:
    def __init__(self, ora, perc, mp, idotartam, honnan):
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.idotartam = idotartam
        self.sebesseg = 3600/idotartam
        self.honnan = honnan
        self.hova = "Felső város" if honnan == "A" else "Alsó város"
    def ido_mp(self):
        return self.ora * 3600 + self.perc * 60 + self.mp

forgalom = []
forras.readline()
for sor in forras:
    adat = sor.strip().split(" ")
    forgalom.append(Meres(int(adat[0]), int(adat[1]), int(adat[2]), int(adat[3]), adat[4]))
forras.close

n = int(input("Melyik jármű adataid kéred?"))
print(f"Az {n}. jármű {forgalom[n-1].hova} felé haladt")

print(f"Az utolsó két autó között {forgalom[-1].ido_mp() - forgalom[-2].ido_mp()}s telt el")