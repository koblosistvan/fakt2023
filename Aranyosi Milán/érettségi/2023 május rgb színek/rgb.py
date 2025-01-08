forras = open('kep.txt', mode='r', encoding='utf-8')

kep = []

for sorok in forras:
    adat = sorok.split()
    sor = []
    for i in range(len(adat)):
        if i % 3 == 0:
            R = int(adat[i])
        elif i % 3 == 1:
            G = int(adat[i])
        else:
            B = int(adat[i])
            RGB = [R, G, B]
            sor.append(RGB)
    kep.append(sor)
forras.close()

print('2. feladat:')
print('Kérem egy képpont adatait!')
line = int(input('Sor:'))
oszlop = int(input('Oszlop:'))

print(f'A képpont színe RGB({kep[line-1][oszlop-1][0]},{kep[line-1][oszlop-1][1]},{kep[line-1][oszlop-1][2]})')

print('3. feladat:')
vilagos = 0
for a in range(len(kep)):
    for b in range(a):
        if sum(kep[a][b]) > 600:
            vilagos += 1
print(vilagos)

"""

A világos képpontok száma: 7837
4. feladat:
A legsötétebb pont RGB összege: 197
A legsötétebb pixelek színe:
RGB(0,85,112)
RGB(0,86,111)
RGB(0,86,111)
6. feladat:
A felhő legfelső sora: 103
A felhő legalsó sora: 280 """