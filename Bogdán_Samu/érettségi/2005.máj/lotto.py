forrás = open('lottosz.dat')
húzások = []
for i in forrás:
    húzások.append([int(a) for a in i.strip().split(' ')])
forrás.close()
utolsó = list(input('Az 52. hét lottószámai: ').split(' '))
utolsó = sorted([int(a) for a in utolsó])

print('\n' + '2. feladat')
print(*utolsó, sep=' ')

egész = int(input('Egész szám 1 és 51 között: '))
print('\n' + '4. feladat')
print(*húzások[egész-1], sep=' ')

számok = []
for i in range(1, 91):
    számok.append(int(i))
for i in range(len(húzások)):
    for e in range(len(húzások[i])):
        if húzások[i][e] in számok:
            számok.remove(húzások[i][e])
print('\n' + '5. feladat')
if len(számok) > 0:
    print('Van')
else:
    print('Nincs')

x = 0
for i in range(len(húzások)):
    for e in range(len(húzások[i])):
        if húzások[i][e] % 2 != 0:
            x += 1
print('\n' + '6. feladat')
print(x)

össz = []
húzások.append(utolsó)
adat = open('lotto52.ki', 'w+')
for i in range(len(húzások)):
    adat.write(' '.join(map(str, húzások[i]))+'\n')
    for e in range(len(húzások[i])):
        össz.append(int(húzások[i][e]))
adat.close()

id1 = 1
id2 = 16
print('\n' + '8. feladat')
for i in range(6):
    for e in range(id1, id2):
        print(össz.count(e), end=' ')
    id1 += 15
    id2 += 15
    print('\n')

prímek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
húzott_prím = []
for i in range(len(prímek)):
    if prímek[i] in össz:
        húzott_prím.append(prímek[i])
for i in range(len(húzott_prím)):
    prímek.remove(húzott_prím[i])

print('9. feladat')
print(*prímek, sep=', ')
