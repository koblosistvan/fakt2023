szam = int(input('> '))
oszto = 2
szamig = 56
while oszto <= szam ** (1 / 2):
    if szam % oszto == 0:
        print(f'A {szam} nem prímszám.')
        break
    else:
        oszto += 1
else:
    print(f'A {szam} prímszám.')

szamok = []
oszto = 2
for i in range(2, szamig+1):
    while oszto <= i ** (1 / 2):
        if i % oszto == 0:
            break
        else:
            szamok.append(i)
print(szamok)
