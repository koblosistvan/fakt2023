forras = open('7a-lakas-arak.txt', mode='r', encoding='utf-8')

darab = int(forras.readline())

terulet = []

ar = []


for sor in forras:
    adat = sor.strip().split(' ')
    ar.append(int(adat[1]))
    terulet.append(int(adat[0]))



forras.close()


legdragabb_ar = max(ar)

print(f'A legdragabb haz ara {legdragabb_ar} millio ft', f'es az a haz a {ar.index(max(ar))}')


vanlakas = False

for i in range(len(ar)):
    if ar[i] > 500:
        vanlakas = True
        break



if vanlakas == True:
    print('Van olyan lakas')
else: print('Nincs olyan lakas')


aroszto = []


for i in range(len(darab))


