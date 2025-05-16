forras = open('ajto-1.txt', mode='r', encoding='utf-8')

ora = []
perc = []
azonosito = []
irany = []

for sor in forras:
    adat = sor.strip().split(' ')
    ora.append(int(adat[0]))
    perc.append(int(adat[1]))
    azonosito.append(int(adat[2]))
    irany.append(adat[3])

bentlevok = []
bentlevok_s = 0
for i in range(len(irany)):
    if irany[i] == 'be':
        bentlevok_s += 1
        bentlevok.append(bentlevok_s)
    elif irany[i] == 'ki':
        bentlevok_s -= 1
        bentlevok.append(bentlevok_s)

forras.close()

print('2. feladat')
print(f'Az első belépő: {azonosito[0]}')
for i in range(len(ora)-1, -1, -1):
    if irany[i] == 'ki':
        print(f'Az utolsó kilépő: {azonosito[i]}')
        break

kiiras = open('athaladas.txt', mode='w', encoding='utf-8')

emberek = sorted(set(azonosito.copy()))

for i in range(len(emberek)):
    atlepes = 0
    for j in range(len(ora)):
        if emberek[i] == azonosito[j]:
            atlepes += 1
    print(f'{emberek[i]} {atlepes}', file=kiiras)

kiiras.close()

print('\n4. feladat')
tarsalgo = []

for i in range(len(ora)):
    if irany[i] == 'be':
        tarsalgo.append(azonosito[i])
    elif irany[i] == 'ki':
        tarsalgo.remove(azonosito[i])

print('A végén a társalgóban voltak:', end=' ')

for i in range(len(tarsalgo)):
    print(sorted(tarsalgo)[i], end=' ')

print('\n\n5. feladat')
for i in range(len(ora)):
    if bentlevok[i] == max(bentlevok):
        print(f'Például {ora[i]}:{perc[i]}-kor voltak a legtöbben a társalgóban.')

print('\n6. feladat')
azon = int(input('Adja meg a személy azonosítóját! '))