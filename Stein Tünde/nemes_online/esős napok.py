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
elso_nap = 0
utolso_nap = 0
for k in range(len(eso)-1):
    if bool(eso[k]):
        elso_index = k
        utolso_index = 0
        d_feladat_lista = []
        for i in range(elso_index + 1, len(eso)):
            if bool(eso[i]):
                utolso_index = i + 1
                d_feladat_lista = eso[elso_index:utolso_index]
                d_esos = 0
                for mal in d_feladat_lista:
                    if bool(mal):
                        d_esos += 1
                if d_esos >= len(d_feladat_lista)/2 and len(d_lista) < len(d_feladat_lista):
                    d_lista = d_feladat_lista
                    elso_nap = elso_index + 1
                    utolso_nap = utolso_index + 1
if bool(d_lista):
    print(f'd feladat\n{elso_nap}. és {utolso_nap}. nap közti intervallum, ami {len(d_lista)} nap.')
