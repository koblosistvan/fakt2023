bemenet = input(':')
elemek = bemenet.split(' ')
a, b = int(elemek[0]), int(elemek[1])
szimpátia = 0
if a < 10 and b < 10:
    if a % b == 0 and b % a == 0:
        szimpátia += 2
    elif a % b == 0:
        szimpátia += 1
    elif b % a == 0:
        szimpátia += 1
elif a >= 10 > b or b >= 10 > a:
    if a >= 10:
        if a % b == 0 and b % a == 0:
            szimpátia += 2
        elif a % b == 0:
            szimpátia += 1
        elif b % a == 0:
            szimpátia += 1
        a = str(a)
        for i in range(len(a)):
            if int(a[i]) == 0:
                break
            elif int(a[i]) % b == 0 and b % int(a[i]) == 0:
                szimpátia += 2
            elif int(a[i]) % b == 0:
                szimpátia += 1
            elif b % int(a[i]) == 0:
                szimpátia += 1
    elif b >= 10:
        if a % b == 0 and b % a == 0:
            szimpátia += 2
        elif a % b == 0:
            szimpátia += 1
        elif b % a == 0:
            szimpátia += 1
        b = str(b)
        for i in range(len(b)):
            if int(b[i]) == 0:
                break
            elif int(b[i]) % a == 0 and a % int(b[i]) == 0:
                szimpátia += 2
            elif int(b[i]) % a == 0:
                szimpátia += 1
            elif a % int(b[i]) == 0:
                szimpátia += 1
else:
    if a % b == 0 and b % a == 0:
        szimpátia += 2
    elif a % b == 0:
        szimpátia += 1
    elif b % a == 0:
        szimpátia += 1
    a = str(a)
    b = str(b)
    for i in range(len(b)):
        if int(b[i]) == 0:
            break
    for i in range(len(a)):
        if int(a[i]) == 0:
            break
        elif int(a[i]) % int(b[i]) == 0 and int(b[i]) % int(a[i]) == 0:
            szimpátia += 2
        elif int(a[i]) % int(b[i]) == 0:
            szimpátia += 1
        elif int(b[i]) % int(a[i]) == 0:
            szimpátia += 1
print(szimpátia)