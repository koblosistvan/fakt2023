forras = open("utasadat.txt", mode="r", encoding="utf-8")

allomas = []
ido = []
kartya_azonosito = []
berlet_fajta = []
ervenyesseg = []
ervenyesseg_sz = []

for sor in forras:
    adat = sor.strip().split(" ")
    allomas.append(int(adat[0]))
    ido.append(adat[1])
    kartya_azonosito.append(int(adat[2]))
    berlet_fajta.append(adat[3])
    ervenyesseg.append(int(adat[4]))
    ervenyesseg_sz.append(adat[4])

datum = []
ora = []
datum_sz = []
for a in ido:
    item = a.strip().split('-')
    datum.append(int(item[0]))
    ora.append(int(item[1]))
    datum_sz.append(item[0])

forras.close()

print('2. feladat')
print(f'A buszra {len(allomas)} utas akart felszállni.')

print('3. feladat')
lejart = 0
for i in range(len(datum)):
    if (berlet_fajta[i] != 'JGY' and datum[i] > ervenyesseg[i]) or (berlet_fajta[i] == 'JGY' and ervenyesseg[i] == 0):
        lejart += 1
print(f'A buszra {lejart} utas nem szállhatott fel.')

print('4. feladat')
szamlalo = 0
id = 0
allomasok = []
for i in range(len(allomas)-1):
    if allomas[i] == allomas[i+1]:
        szamlalo += 1
        id = allomas[i]
    elif allomas[i] != allomas[i+1]:
        allomasok.append(szamlalo+1)
        szamlalo = 0
allomasok.append(szamlalo+1)

maxi = allomasok[0]
max_id = 0
for i in range(len(allomasok)):
    if allomasok[i] > maxi:
        maxi = allomasok[i]
        max_id = i
print(f'A legtöbb utas ({maxi} fő) a {max_id}. megállóban próbált felszállni.')

allomasok = []
for i in range(max(allomas)+1):
    allomasok.append(allomas.count(i))
print(f'A legtöbb utas ({max(allomasok)} fő) a {allomasok.index(max(allomasok))}. megállóban próbált felszállni.')

print('5.feladat')
kedvezmenyes = ['TAB', 'NYB']
ingyenes = ['NYP', 'RVS', 'GYK']

kedv = 0
for i in range(len(datum)):
    if berlet_fajta[i] in kedvezmenyes and datum[i] <= ervenyesseg[i]:
        kedv += 1
ingy = 0
for i in range(len(datum)):
    if berlet_fajta[i] in ingyenes and datum[i] <= ervenyesseg[i]:
        ingy += 1
print(f'Ingyenesen utazók száma: {ingy} fő.\nKedvezményesen utazók száma: {kedv} fő.')

def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 -1
    h2 = h2 + 9 % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 -1
    return d2 - d1

ev1 = []
ho1 = []
nap1 = []
azonosito = []

ev2 = []
ho2 = []
nap2 = []

for i in range(len(datum_sz)):
    if ervenyesseg[i] > 10:
        ev1.append((int(datum_sz[i][0:4])))
        ho1.append(int(datum_sz[i][5:6]))
        nap1.append(int(datum_sz[i][6:]))
        azonosito.append(kartya_azonosito[i])

for i in range(len(ervenyesseg_sz)):
    if int(ervenyesseg_sz[i]) > 10 :
        ev2.append((int(ervenyesseg_sz[i][0:4])))
        ho2.append(int(ervenyesseg_sz[i][5:6]))
        nap2.append(int(ervenyesseg_sz[i][6:]))

kiiras = open('figyelmeztetes.txt', mode='w', encoding='utf-8')

for i in range(len(ev1)):
    if napokszama(ev1[i], ho1[i], nap1[i], ev2[i], ho2[i], nap2[i]) <= 3:
        print(f'{azonosito[i]} {ev2[i]}-{ho2[i]}-{nap2[i]}', file=kiiras)

kiiras.close()