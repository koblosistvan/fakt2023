pontok = open('4d-pontok.txt', mode='r', encoding='utf-8')
r = float(input('Kör sugarának hossza: '))
x = []
y = []
beleesik = 0
for i in pontok:
    xy = i.split()
    x.append(float(xy[0]))
    y.append(float(xy[1]))
    if x[0] < r and y[0] < r:
        beleesik += 1
pontok.close()
print(f'Körvonalon belülre eső pontok száma: {beleesik}')
