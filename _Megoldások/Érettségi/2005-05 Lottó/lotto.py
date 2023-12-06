forrás = open('lottosz.dat', mode='r', encoding='utf-8')
számok = []
for sor in forrás:
    adat = sor.strip().split(' ')
    adat_int = [int(a) for a in adat]
    számok.append(adat_int)
    # vagy egy paranccsal:
    # számok.append([int(a) for a in sor.strip().split(' ')])
forrás.close()

# 1-2. feladat
utolsó_heti = input('Add meg az 52. heti nyerőszámokat: ').split(' ')
utolsó_heti = sorted([int(a) for a in utolsó_heti])

print(f'Az 52. heti nyerőszámok: {", ".join(map(str, utolsó_heti))}')
#print(*utolsó_heti, sep=', ')

# 3-4. feladat
hét_száma = int(input('Melyik hét nyerőszámaira vagy kiváncsi: '))
print(f'A(z) {hét_száma}. heti nyerőszámok: {", ".join(map(str, számok[hét_száma-1]))}')

# 5. feladat