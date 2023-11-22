forras = open('kerekparverseny.txt', mode='r', encoding='utf-8')

elsosor = forras.readline().strip().split(' ')

varosok = elsosor[0]

versenyhossz = elsosor[1]

varosok_tavolsaga = []

for sor in forras:
    adat = sor.strip().split()
    varosok_tavolsaga.append(int(adat[0]))

otvenkm = 0
utak =

for i in range(len(varosok_tavolsaga)):



