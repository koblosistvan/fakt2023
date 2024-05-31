forras = open('kolcsonzesek.txt', 'r', encoding='utf-8')

nev = []
jazon = []
eora = []
eperc = []
vora = []
vperc = []

forras.readline()
for i in forras:
    k = i.strip().split(';')
    nev.append(k[0])
    jazon.append(k[1])
    eora.append(int(k[2]))
    eperc.append(int(k[3]))
    vora.append(int(k[4]))
    vperc.append(int(k[5]))
forras.close()

# task 5 (???)
print(f'Napi kölcsönzések száma: {len(nev)}')

# task 6
nev_input = input('Kérek egy nevet: ')
print(f'{nev_input} kölcsönzései: ')
for i in range(len(nev)):
    if nev[i] == nev_input:
        print(f'{eora[i]}:{eperc[i]}-{vora[i]}:{vperc[i]}')
else:
    print('Nem volt ilyen nevű kölcsönző!')

# task 7

# nullák!!
idopont = input('Adjon meg egy időpontot óra:perc alakban: ')
ido = idopont.strip().split(':')
print('A vízen lévő járművek:')
for i in range(len(nev)):
    if eora[i] < int(ido[0]):
        if vora[i] > int(ido[0]):
            print(f'{eora[i]}:{eperc[i]}-{vora[i]}:{vperc[i]} : {nev[i]}')

        elif vora[i] == int(ido[0]):
            if vperc[i] >= int(ido[1]):
                print(f'{eora[i]}:{eperc[i]}-{vora[i]}:{vperc[i]} : {nev[i]}')

    elif eora[i] == int(ido[0]):
        if eperc[i] <= int(ido[1]):
            print(f'{eora[i]}:{eperc[i]}-{vora[i]}:{vperc[i]} : {nev[i]}')

# task 8
bevetel = 0
for i in range(len(nev)):
    felorak = (60 * vora[i] + vperc[i]) - (60 * eora[i] + eperc[i])
    if felorak % 3 != 0:
        felorak = int(felorak) + 1
    bevetel += 2400 * felorak
print(f'A napi bevétel: {bevetel}')


