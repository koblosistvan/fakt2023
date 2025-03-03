q = int(input())
osszpercek = 0
zenek = []
zenepercek = []
for _ in range(q):
    bemenet = input().strip().split(' ')
    if bemenet[0] == 'P':
        osszpercek += int(bemenet[1])
    elif bemenet[0] == 'L':
        if bemenet[1] not in zenek:
            zenek.append(bemenet[1])
            zenepercek.append(int(bemenet[2]))
        else:
            zenepercek.remove(zenepercek[zenek.index(bemenet[1])])
            zenek.remove(bemenet[1])
    if bemenet[0] == 'Q':
        counter = 0
        osszszamok = 0
        z = 0
        i = 0
        a = osszpercek
        while a >= 0:
            if i > len(zenek)-1+z:
                z -= len(zenek)
            b = zenepercek[-1-i-z]
            a -= zenepercek[-1-i-z]
            if a < 0:
                break
            osszszamok += 1
            i += 1
        for i in range(osszszamok):     # annyiszor ahány számot lejátszott
            if i > len(zenek)-1:
                z -= len(zenek)
            if zenek[-1-i-z] == bemenet[1]:
                counter += 1

print(counter)
