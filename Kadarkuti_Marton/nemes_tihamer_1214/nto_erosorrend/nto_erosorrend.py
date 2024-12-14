# Nemes Tihamér Online 2. forduló - 5. feladat - Erősorrend
# Kadarkuti Márton

DEBUG_ELSO = "3 3"
DEBUG_MASODIK = "Albert Bence Cecil"
DEBUG_SOROK = [
    "Albert > Bence",
    "Bence < Cecil",
    "Cecil < Albert",
]

tmp = "" # seged
nevek = []
nevek_szama:int = 0
sorok_szama:int = 0
relaciok:list[tuple] = []
rendezett:list[float] = []

tmp = DEBUG_ELSO#input() # elso sor
tmp = tmp.strip().split(' ')
nevek_szama:int = int(tmp[0])
sorok_szama:int = int(tmp[1])
rendezett:list[float] = [0]*nevek_szama

nevek = DEBUG_MASODIK#input() # masodik sor, nevek
nevek = nevek.strip().split(' ')

for sor in range(sorok_szama):
    tmp = DEBUG_SOROK[sor]#input()
    tmp = tmp.strip().split(' ')
    if tmp[1] == '<': # a bemenet rendezese A<B alakba
        relaciok.append( (tmp[0],tmp[2]) )
    else:
        relaciok.append( (tmp[2],tmp[0]) )

