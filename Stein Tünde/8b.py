forras = open('7a-lakas-arak.txt', mode='r', encoding='utf-8')

forras.readline()
lakasok_alapterulet = []
lakasok_ar = []
for sor in forras:
    adat = sor.strip().split(' ')
    lakasok_alapterulet.append(int(adat[0]))
    lakasok_ar.append(int(adat[1]))
for i in range(len(lakasok_alapterulet)):
    for i in range(len(lakasok_alapterulet)-1):
        if lakasok_alapterulet[i] < lakasok_alapterulet[i+1]:
            lakasok_alapterulet[i], lakasok_alapterulet[i+1] = lakasok_alapterulet[i+1], lakasok_alapterulet[i]
            lakasok_ar[i], lakasok_ar[i+1] = lakasok_ar[i+1], lakasok_ar[i]
for i in range(len(lakasok_alapterulet)):
    print(f'1. alapterület: {lakasok_alapterulet[i]} m², ár: {lakasok_ar[i]} MFt')
