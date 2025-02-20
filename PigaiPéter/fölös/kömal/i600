korong = []
for i in range(1,26):
    korong.append(i)

felnemhasznalhato = [23, 13, 19]
for i in range(len(felnemhasznalhato)):
    korong.remove(felnemhasznalhato[i])

összoszlop = int(input('Hány oszlopő legyen összesen>'))
meglevooszlop = int(input('A meglévő oszlopok száma: '))

felhesznalt = []

x = True
y = True

if meglevooszlop == 0:
    a = 0
    i = 0
    while y:
        if korong[-1] % korong[i] == 0:
            print(f'Az {a + 1}. oszlop elemei: {korong[-1]} {korong[i]}')
            a += 1
            felhesznalt.append(korong[i])
            felhesznalt.append(korong[-1])
            korong.remove(korong[-1])
            korong.remove(korong[i])
            if a == összoszlop:
                break
        i +=1
else:
    for i in range(meglevooszlop):
        a = 1
        hasznalt = input((f'{a}. oszlop: '))
        hasznalt = hasznalt.strip().split(' ')
        for j in range(len(hasznalt)):
            felhesznalt.append(hasznalt[j])
            korong.remove(int(hasznalt[j]))
        a += 1
    b = 0
    i = 0
    while x:
        if korong[-1] % korong[i] == 0:
            print(f'Az {b + 1}. oszlop elemei: {korong[-1]} {korong[i]}')
            b += 1
            felhesznalt.append(korong[i])
            felhesznalt.append(korong[-1])
            korong.remove(korong[-1])
            korong.remove(korong[i])
            if b == összoszlop - meglevooszlop:
                break
        i += 1
print(f'A felhasznált korongok: {felhesznalt}')
print(f'Maradék korongok: {korong}')
print(f'Fel nem hazsnálható korongok: {felnemhasznalhato}')