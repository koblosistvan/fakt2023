forrás = open('banki napok.txt')
x = forrás.readline().strip().split(' ')
össz_nap = int(x[0])
össz_belépés = int(x[1])
azonosító = []
belépés_napja = []
for i in forrás:
    azonosító.append(int(i.strip().split(' ')[0]))
    belépés_napja.append(int(i.strip().split(' ')[1]))

print(f'a. feladat')
print(azonosító.count(1), azonosító.count(2))

napok = list(set(belépés_napja))
belépések = []
x = []
for i in range(len(napok)):
    egyes = 0
    kettes = 0
    for j in range(len(belépés_napja)):
        if belépés_napja[j] == napok[i]:
            if azonosító[j] == 1:
                egyes += 1
            else:
                kettes += 1
    x.append(egyes)
    x.append(kettes)
    belépések.append(x)
    x = []
print('\n' + 'b. feladat')
for i in range(len(belépések)):
    print(f'{napok[i]}. nap: {belépések[i][0]} {belépések[i][1]}')

együtt = []
for i in range(len(belépések)):
    if belépések[i][0] > 0 and belépések[i][1] > 0:
        együtt.append(napok[i])
print('\n' + 'c. feladat')
for i in range(len(együtt)):
    print(f'A(z) {együtt[i]}. napon mindketten beléptek.')

