forras = open('lottosz.dat', mode='r', encoding='utf-8')
nyeroszamok = []
for sor in forras:
    adat = sor.strip().split(' ')
    adat_int = [int(a) for a in adat]
    nyeroszamok.append(adat_int)

forras.close()

# 1-2. feladat
utso_heti = input('Add meg az 52. hét nyerőszámait: ').split(' ') #89 24 34 11 64
utso_heti = sorted([int(a) for a in utso_heti])

print(f'Az 52. heti nyerőszámok: {", ".join(map(str, utso_heti))}')

# 3-4. feladat
bekert_het = int(input('Melyik hét nyerőszámaira vagy kiváncsi: '))
print(f'A(z) {bekert_het}. heti nyerőszámok: {", ".join(map(str, nyeroszamok[bekert_het-1]))}')

# 5. feladat
osszes_nyeroszam = []

osszes_szam = []
for i in range(1, 91):
    osszes_szam.append(i)

for szam in range(len(nyeroszamok)):
    for a in range(szam):
        osszes_nyeroszam.append(a)

for b in range(len(osszes_nyeroszam)):
    if osszes_nyeroszam[b] in osszes_szam:
        osszes_szam.remove(osszes_nyeroszam[b])

if len(osszes_szam) == 0:
    print('Nincs.')
else:
    print('Van.')

#6. feladat
lottoszdat_osszes = []
for c in range(len(nyeroszamok)):
    for d in range(len(nyeroszamok[c])):
        lottoszdat_osszes.append(d)

paratlan_szamlalo = 0

for e in range(len(lottoszdat_osszes)):
    if e % 2 != 0:
        paratlan_szamlalo += 1
print(paratlan_szamlalo)

#7. feladat
kimenet = open('Lotto52.ki', mode='w', encoding='utf-8')
nyeroszamok.append(utso_heti)
for egyhet in range(len(nyeroszamok)):
    print(*egyhet,sep=', ', file=kimenet)

#8.feladat

#9.feladat
primszamok90ig = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
nemhuztakki_prim = []
for g in range(len(osszes_szam)):
    if osszes_szam[g] in primszamok90ig:
        nemhuztakki_prim.append(osszes_szam[g])
print(*nemhuztakki_prim, sep=', ')
