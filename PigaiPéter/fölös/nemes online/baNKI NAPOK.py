forras = open('banki napok.txt', mode='r', encoding='utf-8')
azonosito = []
nap = []
forras.readline()
for sor in forras:
    azonosito.append(int(sor.strip().split(' ')[0]))
    nap.append(int(sor.strip().split(' ')[1]))
print(f' 1-es dolgozó {azonosito.count(1)}-szor lépett be')
print(f' 2-es dolgozó {azonosito.count(2)}-szor lépett be', '\n𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙')
a = -1
for i in range(len(azonosito)):
    egyes = 0
    kettes = 0
    if i in nap:
        for j in range(nap.count(i)):
            a += 1
            if azonosito[a] == 1:
                egyes += 1
            elif azonosito[a] == 2:
                kettes += 1
        if egyes != 0 and kettes != 0:
            print(f'A {i}. napon mindketten beléptek', '\n𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙')
        elif egyes != 0 and kettes == 0 or egyes == 0 and kettes != 0:
            print(f'A {i}. napon csak az egyik dolgozó lépett be', '\n𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙')
        if egyes == 0:
            print(f'Az egyes dolgozo {egyes}-szor lépett be {i}. napon')
        else:
            print(f'Az egyes dolgozo {egyes}-szer lépett be {i}. napon')
        if kettes == 0:
            print(f'Az kettes dolgozo {kettes}-szor lépett be {i}. napon', '\n𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙')
        else:
            print(f'Az kettes dolgozo {kettes}-szer lépett be {i}. napon', '\n𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙')

