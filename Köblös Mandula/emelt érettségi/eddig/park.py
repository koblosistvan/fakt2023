forras = open('felajanlas.txt', mode='r', encoding='utf-8')

agyasok = int(forras.readline())

mettol = []
meddig = []
szin = []

for sor in forras:
    adat = sor.strip().split(' ')
    mettol.append(int(adat[0]))
    meddig.append(int(adat[1]))
    szin.append(adat[2])

forras.close()

print('2. feladat')
print(f'A felajánlások száma: {len(mettol)}')

print('3. feladat')
print('A bejárat mindkét oldalán ültetők:', end=' ')
for i in range(len(mettol)):
    if mettol[i] > meddig[i]:
        print(i+1, end=' ')

print(f'\n4. feladat')
agyas_sorszama = int(input("Adja meg az ágyás sorszámát! "))
agyasok_szine = []
felajanlasok = 0
for i in range(len(mettol)):
    if mettol[i] < meddig[i] and mettol[i] <= agyas_sorszama <= meddig[i]:
        felajanlasok += 1
        agyasok_szine.append(szin[i])
    elif mettol[i] >= meddig[i] and (mettol[i] <= agyas_sorszama or agyas_sorszama <= meddig[i]):
            felajanlasok += 1
            agyasok_szine.append(szin[i])
print(f'Felajánlók száma: {felajanlasok}')
if len(agyasok_szine) > 0:
    print(f'A virágágyás színe, ha csak az első ültet: {agyasok_szine[0]}')
else:
    print('Nem érkezett felajánlás.')
print(f'A virágágyás színei: {" ".join(set(agyasok_szine))}')

beultetett_agyasok = []
for i in range(len(mettol)):
    if mettol[i] < meddig[i]:
        beultetett_agyasok.append(meddig[i]-mettol[i])
    elif mettol[i] > meddig[i]:
        beultetett_agyasok.append((agyasok-mettol[i])+meddig[i])
# print(beultetett_agyasok)

print('5.feladat')
agyas_szamlalo = [0] * agyasok
for i in range(len(mettol)):
    if mettol[i] < meddig[i]:
        a = range(mettol[i], meddig[i] + 1)
    else:
        a = list(range(mettol[i], agyasok + 1)) + list(range(1, meddig[i] + 1))

    for j in a:
        agyas_szamlalo[j-1] += 1
if min(agyas_szamlalo) > 0:
    print('Minden ágyás beültetésére van jelentkező.')
elif sum(beultetett_agyasok) >= agyasok:
    print('Átszervezéssel megoldható a beültetés.')
elif sum(beultetett_agyasok) < agyasok:
    print('A beültetés nem oldható meg.')

