forras = open('kerekparverseny.txt', mode='r', encoding='utf-8')

elso_sor = forras.readline().strip().split()

varosok_szama = int(elso_sor[0])

verseny_hossz = int(elso_sor[1])

varosok_tavolsaga = []

for sor in forras:
    adat = sor.strip().split()
    varosok_tavolsaga.append(int(adat[0]))

otvenkm = 0
utak = []

for i in range(len(varosok_tavolsaga)):
    