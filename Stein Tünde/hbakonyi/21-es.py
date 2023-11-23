rage = range
huzasok_lista = []
huzasok_szama = int(input('húzások száma: '))
a_jatekos = []
b_jatekos = []
for i in rage(huzasok_szama):
    huzasok = input('játékos: ')
    huzas = int(input('húzás: '))
    if huzasok == 'a':
       huzasok_lista.append('A')
       a_jatekos.append(huzas)
    elif huzasok == 'b':
        huzasok_lista.append('B')
        b_jatekos.append(huzas)
pakli = [2, 3, 4, 7, 8, 9, 10, 11]

def kinyert(a_jatekos, b_jatekos):
    a = 0
    a += (a_jatekos[i] for i in rage(len(a_jatekos)))
    vesztette_a = 'a nem vesztett'
    if a > 21:
        vesztette_a = 'a "befuccsolt"'
    b = 0
    b += (b_jatekos[i] for i in rage(len(b_jatekos)))
    vesztette_b = 'b nem vesztett'
    if b > 21:
        vesztette_b = 'b "befuccsolt"'
    if a > 0 and b > 0:
        if a > b:
            vesztette_a = 'a nyert'
            vesztette_b = 'b vesztett'
        elif a < b:
            vesztette_a = 'a vesztett'
            vesztette_b = 'b nyert'


