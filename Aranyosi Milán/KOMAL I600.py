korongok = []
for i in range(1, 26):
    korongok.append(i)

oszlopok = []

oszlopszam = int(input('Oszlopok száma: '))
for i in range(1, oszlopszam + 1):
    o = input(str(i) + '. oszlop: ').strip().split(' ')
    oszlopok.append(o)
    for x in o:
        korongok.remove(int(x))
print('Szabad korongok: ' + korongok)

for o in oszlopok:  # oszlopok [6, 12, 24]
    for k in korongok:  # a szabad korongok
        joe = True
        for i in o:  # oszlopon belul a szamok pl. 6 v 12 v 24
            if k % int(i) != 0 and int(i) % k != 0:
                joe = False
        if joe == True:
            korongok.remove(k)

print('Nem hozzátehető korongok:' + korongok)
