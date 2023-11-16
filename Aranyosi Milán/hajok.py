import math
forras = open('hajok.txt', mode='r', encoding='utf-8')

elso_sor = forras.readline().strip().split()
hajon_max = int(elso_sor[1])
kontenerek = int(elso_sor[0])
celallomasok = []

for sor in forras:
    celallomasok.append(sor.strip())

forras.close()

varosok = set(celallomasok)

print(varosok)

for varos in varosok:
    kontener_varosba = celallomasok.count

    print(f'{varos} {math.ceil(kontener_varosba/hajon_max)} ')