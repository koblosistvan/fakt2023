import random
'''csapatok = input('Adja meg a két csapat nevét! Egyik-Másik ')
csapatok = csapatok.strip().split('-')
pontok = input('Adja meg az eredményt! 0:0 ')
pontok = pontok.strip().split(':')
for i in pontok:
    i = int(i)
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


def kimenet(lista1, lista2):
    seged = fv(lista2[0], lista2[1])
    return f'{lista1[0]} - {lista1[1]} {lista2[0]}:{lista2[1]} {seged}'


print(f'Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:')
for i in range(len(meccsek)):
    print(kimenet(meccsek[i], eredmenyek[i]))
'''print(kimenet(csapatok, pontok))'''

szelvenyek = open('szelvenyek.txt', 'w', encoding='utf-8')
print(f'Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:', file=szelvenyek)
for i in range(len(meccsek)):
    print(kimenet(meccsek[i], eredmenyek[i]), file=szelvenyek)
'''print(kimenet(csapatok, pontok), file=szelvenyek)'''
szelvenyek.close()

legnagyobb = abs(eredmenyek[0][0]-eredmenyek[0][1])
dontetlen = []
legalabb2 = []


def legalabb2gollal(lista1, lista2, ki):
    if lista1[0]-lista1[1] > 2:
        ki.append(lista2[0])
    elif lista1[0]-lista1[1] < 2:
        ki.append(lista2[1])
    return ki
def legnagyobb_kulonbseg(lista, x):
    if abs(lista[0]-lista[1]) > x:
        x = abs(lista[0]-lista[1])
        return x
def dontetlen_meccsek(lista, ki):
    if lista[0] == lista[1]:
        ki.append(i+1)
        return ki


for i in range(len(eredmenyek)):
    legnagyobb = legnagyobb_kulonbseg(eredmenyek[i], legnagyobb)
    dontetlen = dontetlen_meccsek(eredmenyek[i], dontetlen)
    legalabb2 = legalabb2gollal(eredmenyek[i], meccsek[i], legalabb2)
'''if legnagyobb_kulonbseg(pontok, legnagyobb) > legnagyobb:
    legnagyobb = '+1'
if pontok[0] == pontok[1]:
    dontetlen.append('+1')
legalabb2 = legalabb2gollal(pontok, csapatok, legalabb2)'''

print(f'Legnagyobb gólkülönbségű mérkőzések: {legnagyobb}'
      f'0:0-ás mérkőzések: {dontetlen}')

print(f'Legalább két góllal nyertek:'
      f'{", ".join(legalabb2)}')