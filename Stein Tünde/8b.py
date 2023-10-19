forras = open('7a-lakas-arak.txt', mode='r', encoding='utf-8')

forras.readline()
lakasok_alapterulet = []
lakasok_ar = []
for sor in forras:
    adat = sor.strip().split('')
    lakasok_alapterulet.append(int(adat[0]))
    lakasok_ar.append(int(adat[1]))
for i in range(0, len(lakasok_alapterulet), - 1):
    print(lakasok_ar)