import math

forras = open('hajok.txt', mode='r', encoding='utf-8')

elsosor = forras.readline().strip().split(' ')

osszeskont = int(elsosor[0])

kontenerperhajo = int(elsosor[1])

celallomasok = []


for sor in forras:
    adat = sor.strip().split(' ')
    celallomasok.append(sor.strip())


városok = set(celallomasok)


for város in városok:
    konténer_varosba = celallomasok.count(város)
    ureshelyek =

    print(f'{város} {math.ceil(konténer_varosba/kontenerperhajo)}, ureshelyek')






