forras = open('csapatnevek.txt', mode = 'r', encoding='utf-8')

csapatok = []

for sor in forras:
    adat = sor.strip()
    csapatok.append(adat)
forras.close()

csapatnevek = input('Add meg a két csapat nevét! ')
eredmeny = input('Adja meg az eredményt! ')

for i in eredmeny:
    eredmenyek = i.strip().split(':')
    gol1 = eredmenyek[0]
    gol2 = eredmenyek[1]

def x12(gol1, gol2):
    if gol1 > gol2:
        return 1
    elif gol2 > gol1:
        return 2
    else:
        return x

