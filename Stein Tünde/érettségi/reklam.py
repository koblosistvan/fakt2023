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
melyiknap =

"""
3. feladat:
Kérem, adjon meg egy napot: 9
A rendelések száma az adott napon: 27
4. feladat:
3 nap nem volt a reklámban nem érintett városból rendelés
5. feladat:
A legnagyobb darabszám: 9, a rendelés napja: 22
7. feladat:
A rendelt termékek darabszáma a 21. napon PL: 43 TV: 36 NR: 18
8. feladat:
Napok 1..10 11..20 21..30
PL 98 159 106
TV 97 143 100
NR 91 86 91"""