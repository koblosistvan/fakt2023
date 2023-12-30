forras = open('kozut.txt')

elsosor = forras.readline().strip().split(' ')

ido = []

sebesseg = []

rendszam = []

adatdarab = int(elsosor[0])

osszesido = []
def mpbe(ora, perc, mp):
    print(ora * 3600 + perc * 60 + mp)





for sor in forras:
    adat = sor.strip().split(' ')
    sebesseg.append(int(adat[3]))
    rendszam.append(adat[4])




forras.close()

tobbmintotven = 0

for i in range(len(sebesseg)):
    if sebesseg[i] > 50:
        tobbmintotven += 1


print(f'{tobbmintotven}db olyan autó volt amely 50 nél gyorsabban ment')

voltotvenotnelgyorsabb = False

for i in range(len(sebesseg)):
    if sebesseg[i] >= 55:
        voltotvenotnelgyorsabb = True
        print('Volt olyan auto amely 55 nél gyorsabban ment')
        break
    else:
        print('Nem volt olyan auto amely 55 nel gyorsabban ment')

for i in range(len(rendszam)):
    legyorsabb = max([a for a in sebesseg])
    legyorsabb_id = rendszam[i]
    print(f'A leggyorsabb auto {legyorsabb} sebességgel ment {legyorsabb_id}-es rendszámmal')
    break

for i in range(len(sebesseg)):
    print(sum(sebesseg) / adatdarab,'volt az átlagsebesség')
    break


