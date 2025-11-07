forras = open('valaszok.txt', mode='r', encoding='utf-8')

megoldas1 = forras.readline()
megoldas = megoldas1[:14]

azonossito = []
valasz = []

for sor in forras:
    adat = sor.strip().split(' ')
    azonossito.append(adat[0])
    valasz.append(adat[1])

forras.close()

def feladat(sorszam):
    return f'\n{sorszam}. feladat'

hossz = len(azonossito)

print(feladat(2))
print(f'A vetéledön {hossz} versenyző indult.')

print(feladat(3))
azonossito_be = input('Egy versenyző azonosítója = ')

valasza = 0
for i in range(hossz):
    if azonossito[i] == azonossito_be:
        print(f'{valasz[i]}\t(a versenyző válasza)')
        valasza = valasz[i]

print(feladat(4))
print(f'{megoldas}\t(a helyes megoldás)')
for i in range(len(valasza)):
    if megoldas[i] == valasza[i]:
        print('+', end='')
    else:
        print(' ', end='')
print('\t(a versenyző helyes válaszai)')

print(feladat(5))
sorszam_be = int(input('A feladat sorszáma = '))
helyes = 0
for i in range(hossz):
    if valasz[i][sorszam_be-1] == megoldas[sorszam_be-1]:
        helyes += 1
print(f'A feladatra {helyes} fő, a versenyzők {helyes/hossz*100:0.2f}%-a adott helyes választ.')

eredmeny = []
for i in range(hossz):
    eredmeny_s = 0
    for j in range(len(valasz[i])):
        if valasz[i][j] == megoldas[j] and j < 5:
            eredmeny_s += 3
        elif valasz[i][j] == megoldas[j] and 4 < j < 10:
            eredmeny_s += 4
        elif valasz[i][j] == megoldas[j] and 9 < j < 13:
            eredmeny_s += 5
        elif valasz[i][j] == megoldas[j] and j == 13:
            eredmeny_s += 6
    eredmeny.append(eredmeny_s)

kiiras = open('pontok.txt', mode='w', encoding='utf-8')

for i in range(hossz):
    print(f'{azonossito[i]} {eredmeny[i]}', file=kiiras)

kiiras.close()

print(feladat(7))
print('A verseny legjobbjai:')
legjobbak = eredmeny.copy()
emberek = azonossito.copy()

print(legjobbak)

legnagyobb = max(legjobbak)
for legjobb in legjobbak:
    if legjobb == legnagyobb:
        i = legjobbak.index(legjobb)
        print(f'1. díj ({legnagyobb}): {emberek[i]}')
        legjobbak.remove(legjobb)
        emberek.remove(emberek[i])

legnagyobb = max(legjobbak)
for legjobb in legjobbak:
    if legjobb == legnagyobb:
        i = legjobbak.index(legjobb)
        print(f'2. díj ({legnagyobb}): {emberek[i]}')
        legjobbak.remove(legjobb)
        emberek.remove(emberek[i])

legnagyobb = max(legjobbak)
for legjobb in legjobbak:
    if legjobb == legnagyobb:
        i = legjobbak.index(legjobb)
        print(f'3. díj ({legnagyobb}): {emberek[i]}')