szám = int(input('Szám: '))
osztó = szám
osztóinak_száma = 0
osztok = []

for i in range(szám):
    if szám % osztó == 0:
        osztóinak_száma += 1
        osztok.append(osztó)
    osztó -= 1
    if osztó == 0:
        break
print(osztóinak_száma)
if osztóinak_száma == 2:
    print('Prímszám.')
else:
    print('Nem prímszám.')
    print(osztok)