import math
forras = open('felszin_tpont.txt', mode='r', encoding='utf-8')

x_koordinata = []
y_koordinata = []
sugar = []
nev = []

for sor in forras:
    adat = sor.strip().split('\t')
    x_koordinata.append(float(adat[0]))
    y_koordinata.append(float(adat[1]))
    sugar.append(float(adat[2]))
    nev.append(adat[3])

print(x_koordinata)
print(y_koordinata)
print(sugar)
print(nev)

forras.close()

print('2.feladat')
print(f'A kráterek száma: {len(sugar)}')

print('3.feladat')
bekert_nev = input('Kérem egy kráter nevét: ')

if bekert_nev in nev:
    for i in range(len(nev)):
        if bekert_nev == nev[i]:
            print(f'A(z) {bekert_nev} középpontja X={x_koordinata[i]} Y={y_koordinata[i]} sugara R={sugar[i]}.')
            break
else:
    print('Nincs ilyen nevű kráter.')


print('4.feladat')

legnagyobb_sugar = max(sugar)
legnagyobb_sugar_index = sugar.index(legnagyobb_sugar)

print(f'A legnagyobb kráter neve és sugara: {nev[legnagyobb_sugar_index]} {sugar[legnagyobb_sugar_index]}')

def tavolsag(x1, y1, x2, y2):
    tavolsag = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) ** 1/2
    return tavolsag

print('6.feladat')

bekert_krater = input('Kérem egy kráter nevét: ')
bekert_krater_index = nev.index(bekert_krater)

nincs_kozos_resze = []

for i in range(len(sugar)):
    if i != bekert_krater_index:
        sugarak_osszege = sugar[i] + sugar[bekert_krater_index]
        tavolsag = (x_koordinata[bekert_krater_index] - x_koordinata[i]) * (x_koordinata[bekert_krater_index] - x_koordinata[i]) + (y_koordinata[bekert_krater_index] - y_koordinata[i]) * (y_koordinata[bekert_krater_index] - y_koordinata[i]) ** 1/2
        if tavolsag > sugarak_osszege:
            nincs_kozos_resze.append(nev[i])

if len(nincs_kozos_resze) > 0:
    print(f'Nincs közös része: {nincs_kozos_resze}.')

masik_sugar = sugar

kisebbnagyobb_lista = []

for i in range(len(sugar)):
    for j in range(len(masik_sugar)):
        tavolsag = (x_koordinata[j] - x_koordinata[i]) * (x_koordinata[j] - x_koordinata[i]) + (y_koordinata[j] - y_koordinata[i]) * (y_koordinata[j] - y_koordinata[i]) ** 1 / 2
        if sugar[i] > masik_sugar[j]:
            sugarak_kulonbsege = sugar[i] - masik_sugar[j]
        else:
            sugarak_kulonbsege = masik_sugar[j] - sugar[i]
        if tavolsag < sugarak_kulonbsege:
            if sugar[i] > masik_sugar[j]:
                eredmeny = f'A(z) {nev[i]} kráter tartalmazza a(z) {nev[j]} krátert'
                if eredmeny not in kisebbnagyobb_lista:
                    kisebbnagyobb_lista.append(f'A(z) {nev[i]} kráter tartalmazza a(z) {nev[j]} krátert')
            else:
                eredmeny = f'A(z) {nev[j]} kráter tartalmazza a(z) {nev[i]} krátert'
                kisebbnagyobb_lista.append(f'A(z) {nev[j]} kráter tartalmazza a(z) {nev[i]} krátert')

for i in range(len(kisebbnagyobb_lista)):
    print(kisebbnagyobb_lista[i])
kimenet = open('terulet.txt', mode='w', encoding='utf-8')

for i in range(len(sugar)):
    terulet = 3.14 * sugar[i] ** 2
    print(f'{terulet:0.2f}\t{nev[i]}', file=kimenet)

kimenet.close()