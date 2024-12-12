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
print(f'2. feladat:\n'
      f'A rendelések száma: {len(darabszam)}')

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
for i in range(len(varos)):
    if varos[i] == 'NR':
        if not nap[i]:
            nr_rendeles += 1
        elif nap[i] != nap[i-1]:
            nr_rendeles += 1
print(f'4. feladat:\n'
      f'{nr_rendeles} nap nem volt a reklámban nem érintett városból rendelés')

# 5
dbmax = max(darabszam)
print(f'5. feladat:\n'
      f'A legnagyobb darabszám: {dbmax}, a rendelés napja: {nap[darabszam.index(dbmax)]}')

# 6
def osszes(n, v):
    kimenet = 0
    for index in range(len(nap)):
        if nap[index] == n:
            if varos[index] == v:
               kimenet += darabszam[index]
    return kimenet

# 7
print(f'7. feladat:\n'
      f'A rendelt termékek darabszáma a 21. napon'
      f'PL: {osszes(21, "PL")} TV: {osszes(21, "TV")} NR: {osszes(21, "NR")}')

# 8
lista = []
pl_l = [0]*4
pl_l[0] = 'PL'
lista.append(pl_l)
tv_l = [0]*4
tv_l[0] = 'TV'
lista.append(tv_l)
nr_l = [0]*4
nr_l[0] = 'NR'
lista.append(nr_l)
for i in range(len(nap)):
    if nap[i] <= 10:
        for k in lista:
            if varos[i] == k[0]:
                k[1] += 1
    elif 10 < nap[i] <= 20:
        for k in lista:
            if varos[i] == k[0]:
                k[2] += 1
    else:
        for k in lista:
            if varos[i] == k[0]:
                k[3] += 1


print('8. feladat:\n'
      'Napok 1..10 11..20 21..30')
print(*pl_l, sep='\t')
print(*tv_l, sep='\t')
print(*nr_l, sep='\t')
"""
8. feladat:
Napok 1..10 11..20 21..30
PL 98 159 106
TV 97 143 100
NR 91 86 91"""