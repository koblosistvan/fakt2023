forras = open('7a-lakas-arak.txt', mode='r', encoding='utf-8')


a=forras.readline().strip().split()

ár = a[0]

terulet = a[1]


for sor in forras:
    adat = sor.strip().split(' ')
    ár = ár.append(int(adat[1]))
    terulet = terulet.append(int(adat[0]))



forras.close()


legdragabb_ar = 0
legdragabb_id = ár[1] - ár[0]

for i in range(len(ár)):
    if ár[i] > legdragabb_ar:
        print(f'Ez az ár a legdragabb {legdragabb_ar}')

