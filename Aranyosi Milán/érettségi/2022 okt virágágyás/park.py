forras = open('felajanlas.txt', mode='r', encoding='utf-8')

max_agyas = int(forras.readline())

elso = []
utolso = []
szin = []
for sor in forras:
    adat = sor.strip().split(' ')
    elso.append(int(adat[0]))
    utolso.append(int(adat[1]))
    szin.append(adat[2])

forras.close()

print('2. feladat')
print(f'A felajánlások száma:{len(elso)}')

print('\n3. feladat')
bejaratbeultetes = ''
for i in range(len(elso)):
    if elso[i] > utolso[i]:
        bejaratbeultetes += f' {i+1}'

print(f'A bejárat mindkét oldalán ültetők:{bejaratbeultetes}')


print('\n4.feladat')
adott_agyas = int(input('Adja meg az ágyás sorszámát!'))
szamlalo = 0
szinek_lista = []
szinek = ''
for i in range(len(elso)):
    if adott_agyas in range(elso[i], utolso[i]):
        szamlalo += 1
        if szin[i] not in szinek:
            szinek += f' {szin[i]}'
            szinek_lista.append(szin[i])
if szamlalo == 0:
    print('Ezt az ágyást nem ültetik be.')

print(f'A felajánlók száma: {szamlalo}')
print(f'A virágágyás színe, ha csak az első ültet: {szinek_lista[0]}')
print(f'A virágágyás színei:{szinek}')


print('\n5.feladat')
osszesagyas = []
for i in range(1, max_agyas+1):
    osszesagyas.append(int(i))

def agyasok(elso, utolso):
    lista = []
    if elso > utolso:
        for i in range(elso, max_agyas+1):
            lista.append(i)
        for i in range(1, utolso+1):
            lista.append(i)
    else:
        for i in range(elso, utolso+1):
            lista.append(i)
    return lista

for i in range(len(elso)):
    seged_lista = agyasok(elso[i], utolso[i])
    for j in range(len(seged_lista)):
        if seged_lista[j] in osszesagyas:
            osszesagyas.remove(seged_lista[j])


if len(osszesagyas) == 0:
    print('Minden ágyás beültetésére van jelentkező.')

ossz_felajanlas = 0
for i in range(len(elso)):
    ossz_felajanlas += len(agyasok(elso[i], utolso[i]))

if ossz_felajanlas >= max_agyas:
    print('Átszervezéssel megoldható a beültetés.')

if ossz_felajanlas < max_agyas:
    print('A beültetés nem oldható meg.')


#6. feladat
kimenet = open('szinek.txt', mode='w', encoding='utf-8')

osszesagyas_2 = []
for i in range(1, max_agyas+1):
    osszesagyas_2.append(int(i))

kesz_szinek = []
kesz_agyasok = []
kesz_ajanlszam = []

for i in range(len(elso)):
    seged_lista = agyasok(elso[i], utolso[i])
    for j in range(len(seged_lista)):
        if seged_lista[j] in osszesagyas_2:
            kesz_agyasok.append(seged_lista[j])
            kesz_szinek.append(szin[i])
            kesz_ajanlszam.append(i+1)

for i in range(len(osszesagyas_2)):
    kesz_agyasok.append(osszesagyas_2[i])
    kesz_szinek.append('#')
    kesz_ajanlszam.append(0)


for i in range(len(kesz_agyasok)-1):
    legkisebb = i
    for j in range(i+1, len(kesz_agyasok)):
        if kesz_agyasok[j] < kesz_agyasok[legkisebb]:
            legkiesebb = j
    seged = kesz_agyasok[i]
    kesz_agyasok[i] = kesz_agyasok[legkisebb]
    kesz_agyasok[legkisebb] = seged

    seged_ketto = kesz_szinek[i]
    kesz_szinek[i] = kesz_szinek[legkisebb]
    kesz_szinek[legkisebb] = seged_ketto

    seged_harom = kesz_ajanlszam[i]
    kesz_ajanlszam[i] = kesz_ajanlszam[legkisebb]
    kesz_ajanlszam[legkisebb] = seged_harom



for i in range(len(kesz_szinek)):
    print(f'{kesz_szinek[i]} {kesz_ajanlszam[i]}', file=kimenet)

kimenet.close()
