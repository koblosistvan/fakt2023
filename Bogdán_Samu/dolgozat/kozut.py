forrás = open('kozut.txt')
össz = int(forrás.readline())
óra = []
perc = []
mp = []
sebesség = []
rendszám = []
for i in forrás:
    x = i.strip().split(' ')
    if int(x[0]) < 10:
        x[0] = '0' + x[0]
    óra.append(x[0])
    if int(x[1]) < 10:
        x[1] = '0' + x[1]
    if int(x[2]) < 10:
        x[2] = '0' + x[2]
    perc.append(x[1])
    mp.append(x[2])
    sebesség.append(int(x[3]))
    rendszám.append(x[4])

print('Adatok beolvasása...' + '\n' + f'A kozut.txt fájlból beolvastam {össz} sort.')

print('\n' + '1. feladat')
x = 0
for i in range(össz):
    if sebesség[i] > 50:
        x += 1
print(f'{x} autó volt gyorsabb a megengedett 50 km/h-nál.')

print('\n' + '2. feladat')
for i in range(össz):
    if sebesség[i] > 55:
        print('Volt 55 km/h-nál gyorsabb autó.')
        break
else:
    print('Nem volt 55 km/h-nál gyorsabb autó.')

print('\n' + '3. feladat')
x = sebesség.index(max(sebesség))
print(f'A leggyorsabb autó rendszáma: {rendszám[x]}, {sebesség[x]} km/h sebességgel ment.')

print('\n' + '4. feladat')
print(f'Az áthaladó autók átlagsebessége {round(sum(sebesség) / len(sebesség), 2)} km/h volt.')

kimenet = open('kozut-kimenet.txt', 'w', encoding='utf-8')
kimenet.write('30 km/h-nál lassabb járművek adatai' + '\n')
for i in range(össz):
    if sebesség[i] < 30:
        kimenet.write(f'{óra[i]}:{perc[i]}:{mp[i]} - {rendszám[i].split("-")[0] + rendszám[i].split("-")[1]} - '
                      f'{sebesség[i]} km/h' + '\n')
