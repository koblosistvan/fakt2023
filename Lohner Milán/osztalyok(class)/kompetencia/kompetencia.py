class kompetencia:
    def __init__(self, azonosito, tavalyikepessegpont, tavalyikepessegszint, ideielozetkepessegpont, ideielozetkepessegszint, ideiveglegeskepessegpont, ideiveglegesekepessegszint):
        self.azonosito=azonosito
        self.tavalyikepessegpont=tavalyikepessegpont
        self.tavalyikepessegszint=tavalyikepessegszint
        self.ideielozeteskepessegpont = None if ideielozetkepessegpont == 'Nincs' else int(ideielozetkepessegpont)
        self.ideielozeteskepessegszint = None if ideielozetkepessegszint == 'Nincs' else int(ideielozetkepessegszint)
        self.ideiveglegeskepessegpont = None if ideiveglegeskepessegpont == 'Nincs' else int(ideiveglegeskepessegpont)
        self.ideiveglegesekepessegszint = None if ideiveglegesekepessegszint == 'Nincs' else int(ideiveglegesekepessegszint)



osszesadat=[]
azonositok=[]
szovegertes=[]
matek=[]


forras=open('okm-2023-7.csv')
forras.readline()
forras.readline()
forras.readline()

for sor in forras:
    adat=sor.strip().split(';')
    szovegertes.append(kompetencia(azonosito=(adat[2]), tavalyikepessegpont=(adat[3]), tavalyikepessegszint=(adat[4]), ideielozetkepessegpont=(adat[5]), ideielozetkepessegszint=(adat[6]), ideiveglegeskepessegpont=(adat[7]), ideiveglegesekepessegszint=(adat[8])))
    matek.append(kompetencia(azonosito=(adat[2]), tavalyikepessegpont=(adat[9]), tavalyikepessegszint=(adat[10]), ideielozetkepessegpont=(adat[11]), ideielozetkepessegszint=(adat[12]), ideiveglegeskepessegpont=(adat[13]), ideiveglegesekepessegszint=(adat[14])))
forras.close()

#1. feladat
azon = [meres.azonosito for meres in szovegertes]
print(f'{len(set(azon))} darab meres talalhato')

#2. feladat


legmagasabb=sorted(szovegertes, reverse=True, key=lambda a: a.ideielozeteskepessegpont)

print(legmagasabb[0])