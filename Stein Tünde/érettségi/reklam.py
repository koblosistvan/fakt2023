# 1
forras = open('rendel.txt', 'r', encoding='utf-8')
nap = []
varos = []
darabszam = []
for sor in forras:
    i = sor.strip().split(' ')
    nap.append(int(i[0]))
    varos.append(i[1])
    darabszam.append(int(i[2]))
forras.close()

# 2
print(f'2. feladat:'
      f'A rendelések száma: {sum(darabszam)}')

# 3
print('3. feladat:')
melyiknap = int(input('Kérem, adjon meg egy napot: '))
rendelesek_3 = 0
for i in range(len(darabszam)):
    if nap[i] == melyiknap:
        rendelesek_3 += darabszam[i]
print(f'A rendelések száma az adott napon: {rendelesek_3}')

# 4
nr_rendeles = 0
for i in varos:
    if i == 'NR':
        nr_rendeles += 1
print(f'4. feladat:'
      f'{nr_rendeles} nap nem volt a reklámban nem érintett városból rendelés')

# 5
dbmax = max(darabszam)
print(f'5. feladat:'
      f'A legnagyobb darabszám: {dbmax}, a rendelés napja: {nap[darabszam.index(dbmax)]}')

# 6

# 7
pl_7 = 0
tv_7 = 0
nr_7 = 0
for i in range(len(nap)):
    if nap[i] == 21:
        if varos[i] == 'PL':
            pl_7 += darabszam[i]
        elif varos[i] == 'TV':
            tv_7 += darabszam[i]
        elif varos[i] == 'NR':
            tv_7 += darabszam[i]
print(f'7. feladat:'
      f'A rendelt termékek darabszáma a 21. napon PL: {pl_7} TV: {tv_7} NR: {nr_7}')

# 8
osszlista = []
pl_l = []*4
pl_l[0] = 'PL'
osszlista.append(pl_l)
tv_l = []*4
tv_l[0] = 'TV'
osszlista.append(tv_l)
nr_l = []*4
nr_l[0] = 'NR'
osszlista.append(nr_l)
for i in range(len(nap)):
    for k in range(len(osszlista)):
        if varos == osszlista[k][0]:
            if nap[i] >= 10:
                pl_l[1] += darabszam[i]
            elif 10 > nap[i] >= 20:
                pl_l[2] += darabszam[i]
            else:
                pl_l[3] += darabszam[i]
print(f'8. feladat:'
      f'Napok 1..10 11..20 21..30'
      f'{osszlista[0]}'
      f'{osszlista[1]}'
      f'{osszlista[2]}')

"""
8. feladat:
Napok 1..10 11..20 21..30
PL 98 159 106
TV 97 143 100
NR 91 86 91"""