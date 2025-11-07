# 1
forras = open('Stein Tünde/érettségi/proba/felszin_tpont.txt', 'r', encoding='utf-8')
x = []
y = []
sugar = []
nev = []
for i in forras:
    sor =  i.strip().split('\t')
    x.append(float(sor[0]))
    y.append(float(sor[1]))
    sugar.append(float(sor[2]))
    nev.append(sor[3])
forras.close()

# 2
print(f'2. feladat\nA kráterek száma: {len(x)}')

# 3
bekertnev = input(f'3. feladat\nKérem egy kráter nevét: ')
if bekertnev in nev:
    for i in range(len(nev)):
        if nev[i] == bekertnev:
            print(f'A(z) {bekertnev} középpontja X={x[i]} Y={y[i]} sugara R={sugar[i]}.')
else:
    print('Nincs ilyen nevű kráter.')

# 4
maxsugar_i = sugar.index(max(sugar))
print(f'4. feladat\nA legnagyobb kráter neve és sugara: {nev[maxsugar_i]} {sugar[maxsugar_i]}')

# 5
def tavolsag(x1, y1, x2, y2):
    return ( (x2-x1)**2 + (y2-y1)**2 )**(1/2)

# 6
bekertnev = input(f'6. feladat\nKérem egy kráter nevét: ')
if bekertnev in nev:
    bekert_i = nev.index(bekertnev)
    nincskozos = []
    for i in range(len(nev)):
        if tavolsag(x[i], y[i], x[bekert_i], y[bekert_i]) > (sugar[i] + sugar[bekert_i]):
            nincskozos.append(nev[i])
    print(f'Nincs közös része: {", ".join(nincskozos)}.')

# 7
print('7. feladat')
for i in range(len(nev)):
    for k in range(len(nev)):
        if tavolsag(x[i], y[i], x[k], y[k]) < (sugar[i] - sugar[k]):
            print(f'A(z) {nev[i]} kráter tartalmazza a(z) {nev[k]} krátert.')

# 8
kimenet = open('Stein Tünde/érettségi/proba/terulet.txt', 'w', encoding='utf-8')
for i in range(len(nev)):
    print(f'{round(3.14*(sugar[i]**2),2)}\t{nev[i]}', file=kimenet)
kimenet.close()
