forrás = open('4d-pontok.txt', mode='r', encoding='utf-8')

xk = []
yk = []
for sor in forrás:
    adat = sor.split(' ')
    xk.append(float(adat[0]))
    yk.append(float(adat[1]))
x = float(input('x = '))
y = float(input('y = '))
r = float(input('sugár = '))
while True:
    if r <= 0:
        r = float(input('sugár = '))
    else:
        break

belül = 0
körvonal = 0
kívül = 0

for i in range(len(xk)):
    if (x - xk[i]) ** 2 + (y - yk[i]) **2 < r** 2:
        belül += 1
        a = 'Belülre esik.'
    elif (x - xk[i]) ** 2 + (y - yk[i]) **2 > r** 2:
        kívül += 1
        a = 'Kívülre esik.'
    elif (x - xk[i]) ** 2 + (y - yk[i]) **2 == r** 2:
        körvonal += 1
        a = 'Körvonalra esik.'
    else:
        a = 'hmm'
print(a)