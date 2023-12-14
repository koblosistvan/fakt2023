napok = int(input('Napok száma: '))
bemenet_eso = input('Csapadék mennyisége: ')
eso = []
#11
#5 0 0 0 0 5 0 3 3 0 0

for i in bemenet_eso.strip().split(' '):
    eso.append(int(i))
csapadekos_nap = 0
for i in eso:
    if i > 0:
        csapadekos_nap += 1
print(f'a feladat\n{csapadekos_nap} napon esett az eső.\n')

legh_idotartam = 0
idotartam = 0
for i in range(len(eso)):
    if eso[i] == 0:
        idotartam += 1
        if idotartam > legh_idotartam:
            legh_idotartam = idotartam
    else:
        idotartam = 0
print(f'b feladat\n{legh_idotartam} nap volt a leghosszabb csapadékmentes időszak.\n')

legtobb_cs = 0
csapadek = 0
for i in range(len(eso)-1):
    if eso[i] + eso[i+1] > legtobb_cs:
        legtobb_cs = eso[i] + eso[i+1]
print(f'c feladat\nKét nap alatt {legtobb_cs} mm volt a legtöbb leesett csapadék.\n')

d_lista = []
for k in range(len(eso)):
    elso_index = 0
    utolso_index = 0
    d_feladat_lista = []
    for i in range(len(eso)):
        if bool(eso[i]):
            elso_index = eso[i]
        if bool(eso[i]) and eso[i] == elso_index:
            utolso_index = eso[i]
    d_feladat_lista.append(eso[elso_index:utolso_index])
    d_esos = 0
    for i in d_feladat_lista:
        if bool(i):
            d_esos += 1
    if d_esos >= len(d_feladat_lista):
        d_lista = d_feladat_lista
print(d_lista)
print(f'd feladat\n{d_lista[0]}. és {d_lista[-1]}. nap közti intervallum.')
