import random
'''csapatok = input('Adja meg a két csapat nevét! Egyik-Másik ')
csapat1 = csapatok.strip().split('-')[0]
csapat2 = csapatok.strip().split('-')[1]
eredmeny = input('Adja meg az eredményt! 0:0 ')
pont1 = int(eredmeny.strip().split(':')[0])
pont2 = int(eredmeny.strip().split(':')[1])
'''


def fv(gol1, gol2):
    if gol1 > gol2:
        return 1
    elif gol1 < gol2:
        return 2
    else:
        return 'X'


forras = open('csapatnevek.txt', 'r', encoding='utf-8')
csapatnevek = []
for sor in forras:
    i = sor.strip()
    csapatnevek.append(i)
forras.close()
meccsek = []
eredmenyek = []
for i in range(7):
    csapatnevek_2 = csapatnevek.copy()
    meccs = []
    golok = []
    for k in range(2):
        golok.append(random.randint(0, 5))
        seged = random.choice(csapatnevek_2)
        meccs.append(seged)
        csapatnevek_2.remove(seged)
    meccsek.append(meccs)
    eredmenyek.append(golok)

