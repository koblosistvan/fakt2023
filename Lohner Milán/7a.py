forras = open('7a-lakas-arak.txt', mode='r', encoding='utf-8')

terulet = []

ar = []

forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    ar.append(int(adat[0]))
    terulet.append(int(adat[1]))



forras.close()


legdragabb_ar = max(ar)
legdragabb_id =

for i in range(len(ar)):





