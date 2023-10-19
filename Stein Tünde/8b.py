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


lista = [1, 2, 3, 4, 67, 0]
lista2 = []
for i in range(len(lista) - 1):
    if lista[i] > lista[i+1]:
        lista2.append(lista[i])
        i_erteke = i
