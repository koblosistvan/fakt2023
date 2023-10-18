forras = open('7a-lakas-arak.txt', mode='r', encoding='utf-8')

ár = []

terulet = []


for sor in forras:
    adat = sor.strip().split(' ')
    ár.append(int(adat[1]))
    terulet.append(int(adat[0]))



forras.close()


legdragabb_ar = 0
legdragabb_id = 0

for i in range(len(ár)):
    if ár[i] > 500:
        print(f'Ez az ár a legdragabb {legdragabb_ar}')



