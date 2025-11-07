# 1. feladat
forras = open('tomeg.txt', mode='r', encoding='utf-8')
lista = []
for i in forras:
    sor = i.strip(', ').split(', ')
    for k in sor:
        lista.append(int(k))
forras.close()

print(f'2. feladat\nA tárgyak tömegének összege: {sum(lista)}')

print('3. feladat')
lista1 = lista
tomegek = []
while lista1 != []:
    tomeg = 0
    while lista != [] and tomeg + lista1[0] <= 20:
        tomeg += lista1[0]
        lista1.remove(lista1[0])
        """ -= lista1[i]"""
    tomegek.append(tomeg)
print(tomegek)
print()
print(f'A dobozok tartalmának tömege (kg): ', end='')
for t in tomegek:
    print(t, end=' ')

print(f'\nA szükséges dobozok száma: {len(tomegek)}')
