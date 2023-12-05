szám = int(input('Szám: '))
osztóinak_száma = 0
osztok = []
if szám % 2 == 0:
    osztó = szám / 2
    osztóinak_száma += 2
    osztok.append(2)
    osztok.append((szám/2))
else:
    osztó = int((szám / 2) -0.5) - 1

while osztó > 2:
    if szám % osztó == 0:
        osztóinak_száma += 1
        osztok.append(osztó)
    osztó -= 2
    print(osztó)
print(osztóinak_száma)
if osztóinak_száma == 0:
    print('Prímszám.')
else:
    print('Nem prímszám.')
    print(osztok)
