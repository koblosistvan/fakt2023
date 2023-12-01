forrás = open('lottosz.dat')
húzások = []
for i in forrás:
    húzások.append([int(a) for a in i.strip().split(' ')])
utolsó = list(input('Az 52. hét lottószámai: ').split(' '))
utolsó = sorted([int(a) for a in utolsó])
print('2. feladat')
print(*utolsó, sep=' ')
egész = int(input('Egész szám 1 és 51 között: '))
print('4. feladat')
print(*húzások[egész-1], sep=' ')
számok = []
for i in range(1, 91):
    számok.append(int(i))
for i in range(len(húzások)):
    for e in range(len(húzások[i])):
        if húzások[i][e] in számok:
            számok.remove(húzások[i][e])
print('5. feladat')
if len(számok) > 0:
    print('Van')
else:
    print('Nincs')
x = 0
for i in range(len(húzások)):
    for e in range(len(húzások[i])):
        pass
