# Nemes Tihamér Online 2. forduló - 4. feladat - Puska
# Kadarkuti Márton

# ROSSZ

DEBUG_ELSO = "4 7"
DEBUG_SOROK = [
    "5 2",
    "4 2",
    "2 2",
    "1 2",
]

tmp = "" # seged
tmp = DEBUG_ELSO#input()
tmp = tmp.strip().split(' ')

kepletek_szama:int = int(tmp[0])
sorok_szama:int = int(tmp[1])

kepletek:list[list[int]] = [[i] for i in range(kepletek_szama)]

for sor in range(kepletek_szama):
    tmp = DEBUG_SOROK[sor]#input()
    kepletek[sor] += [int(i) for i in tmp.strip().split(' ') ]

#print(kepletek)
kepletek = sorted(kepletek, key=lambda i: i[2])
kepletek = sorted(kepletek, key=lambda i: i[1])
#print(kepletek)

kimenet = []
kimenet_fontos_osszeg:int = 0
i:int = 0
for keplet in reversed(kepletek):
    i += keplet[1]
    if i <= sorok_szama:
        kimenet.append(keplet)
        kimenet_fontos_osszeg += keplet[2]

# kimenet
print(len(kimenet), kimenet_fontos_osszeg)
print(' '.join([str(1+i[0]) for i in kimenet]))