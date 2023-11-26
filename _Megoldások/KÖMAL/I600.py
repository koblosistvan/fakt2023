oszlopok_száma = int(input('Hány oszlop van? '))
oszlopok = []
for i in range(oszlopok_száma):
    oszlop = input(f'{i+1}. oszlop korongjai: ').split(' ')
    oszlopok.append([int(a) for a in oszlop])

nem_használt = set(range(1, 26))
for oszlop in oszlopok:
    nem_használt = nem_használt - set(oszlop)
print('Nem használt korongok: ', end='')
print(', '.join(map(str, nem_használt)))

nem_tehető = []
for méret in nem_használt:
    betehető = False
    for oszlop in oszlopok:
        if oszlop[0] % méret == 0 or méret % oszlop[-1] == 0:
            betehető = True
        else:
            for pos in range(len(oszlop)-1):
                if méret % oszlop[pos] == 0 and oszlop[pos+1] % méret == 0:
                    betehető = True
    if not betehető:
        nem_tehető.append(méret)
print('Ne tudjuk betenni: ', end='')
print(', '.join(map(str, nem_tehető)))

'''
Jó megoldás: Samu, Marci, Milo
