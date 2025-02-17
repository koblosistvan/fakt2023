# 1
forras = open('kep.txt', 'r', encoding='utf-8')
red = []
green = []
blue = []
for sor in forras:
    i = sor.strip().split(' ')
    for k in range(len(i)):
        if (k+1) % 3 == 1:
            red.append(int(i[k]))
        elif (k+1) % 3 == 2:
            green.append(int(i[k]))
        elif (k+1) % 3 == 0:
            blue.append(int(i[k]))
forras.close()

# 2
print('2. feladat:\n'
      'Kérem egy képpont adatait!')
sor = int(input('Sor: '))
oszlop = int(input('Oszlop: '))
keresett_index = (sor-1)*640 + oszlop - 1
print(f'A képpont színe RGB({red[keresett_index]},{green[keresett_index]},{blue[keresett_index]})')

# 3
vilagos = 0
legsotetebb_4 = 600
for i in range(len(red)):
    if (red[i] + green[i] + blue[i]) > 600:
        vilagos += 1
    elif (red[i] + green[i] + blue[i]) < legsotetebb_4:
        legsotetebb_4 = (red[i] + green[i] + blue[i])
print(f'3. feladat:\n'
      f'A világos képpontok száma: {vilagos}')

# 4
legsotetebbindex = []
for i in range(len(red)):
    if (red[i] + green[i] + blue[i]) == legsotetebb_4:
        legsotetebbindex.append(i)
print(f'4. feladat:\n'
      f'A legsötétebb pont RGB összege: {legsotetebb_4}\n'
      f'A legsötétebb pixelek színe:')
for i in legsotetebbindex:
    print(f'RGB ({red[i]}, {green[i]}, {blue[i]})')

def hatar(sor5, elteres):
    van = False
    for index in range((sor5-1)*640, sor5*640-1):
        if abs(blue[index] - blue[index+1]) > elteres:
            van = True
    return van

# 6
elso = 0
utolso = 0
for i in range(359):
    if hatar(i, 10):
        elso = i
        break
for i in range(359):
    if hatar(i, 10):
        if not hatar(i+1, 10):
            utolso = i
            break
print(f'6. feladat:\n'
      f'A felhő legfelső sora: {elso}\n'
      f'A felhő legalsó sora: {utolso}')


"""2. feladat:
Kérem egy képpont adatait!
Sor:180
Oszlop:320
A képpont színe RGB(184,183,181)
3. feladat:
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