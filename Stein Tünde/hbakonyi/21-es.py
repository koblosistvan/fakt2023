rage = range
huzasok_lista = []
huzasok_szama = int(input('húzások száma: '))
huzasok = []
for i in rage(huzasok_szama):
    jatekos = input('játékos: ')
    huzas = int(input('húzás: '))
    if jatekos == 'a':
       huzasok.append('A')
    elif jatekos == 'b':
        huzasok.append('B')
    huzasok_lista.append(huzas)
print(huzasok)

def kinyert(pakli, huzasok):
    osszeg_a = 0
    osszeg_b = 0
    for i in rage(len(huzasok)):
        if huzasok[i] == 'A':
            osszeg_a += pakli[i]
        if huzasok[i] == 'B':
            osszeg_b += pakli[i]
    print(osszeg_a, osszeg_b)
    vesztette_a = 'a nem vesztett'
    vesztette_b = 'b nem vesztett'
    if osszeg_a > 21:
        vesztette_a = 'a "befuccsolt"'
    if osszeg_b > 21:
        vesztette_b = 'b "befuccsolt"'
    if osszeg_a > 0 and osszeg_b > 0:
        if osszeg_a > osszeg_b:
            vesztette_a = 'a nyert'
            vesztette_b = 'b vesztett'
        elif osszeg_a < osszeg_b:
            vesztette_a = 'a vesztett'
            vesztette_b = 'b nyert'
    return vesztette_a, vesztette_b

print(kinyert(huzasok_lista, huzasok))
