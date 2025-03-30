forras = open('felszin_tpont.txt', encoding='utf-8', mode='r')

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

forras.close()


print('2. feladat')
print(f'A kráterek száma: {len(x_koordinata)}')

print('3. feladat')
krater = input('Kérem egy kráter nevét: ')
van_ilyen = False
for i in range(len(x_koordinata)):
    if nev[i] == krater:
        print(f'A(z) {krater} középpontja X={x_koordinata[i]} Y={y_koordinata[i]} sugara R={sugar[i]}.')
        van_ilyen = True
if van_ilyen == False:
    print('Nincs ilyen nevű kráter.')


print('4. feladat')
legnagyobb = sugar[0]
legnagyobb_id = 0
for i in range(len(x_koordinata)):
    if sugar[i] > legnagyobb:
        legnagyobb = sugar[i]
        legnagyobb_id = i
print(f'A legnagyobb kráter neve és sugara: {nev[legnagyobb_id]} {sugar[legnagyobb_id]}')

def tavolsag(x1, x2, y1, y2):
    return ((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))*0.5


print('6.feladat')
krater_neve = input('Kérem egy kráter nevét: ')

van_e = False
krater_x = 0
krater_y = 0
krater_sugar = 0


for i in range(len(x_koordinata)):
    if nev[i] == krater_neve:
        krater_x = x_koordinata[i]
        krater_y = y_koordinata[i]
        krater_sugar = sugar[i]
        van_e = True
if van_e == True:
    print('Nincs közös része:', end=' ')
    for i in range(len(x_koordinata)):
        if nev[i] != krater_neve and sugar[i] + krater_sugar < tavolsag(x_koordinata[i], krater_x, y_koordinata[i], krater_y):
            print(f'{nev[i]}', end=', ')
    else:
        print('')

print('\n7.feladat')

for i in range(len(x_koordinata)):
    for j in range(len(x_koordinata)):
        if (sugar[i] - sugar[j]) > 0 and tavolsag(x_koordinata[i], x_koordinata[j], y_koordinata[i], y_koordinata[j]) < (sugar[i] - sugar[j]):
            print(f'A(z) {nev[i]} kráter tartalmazza a(z) {nev[j]} krátert.')

kiiras = open('terulet.txt', mode='w', encoding='utf-8')

for i in range(len(x_koordinata)):
    print(f'{sugar[i]*sugar[i]*3.14 :0.2f}\t{nev[i]}', file=kiiras)

kiiras.close()