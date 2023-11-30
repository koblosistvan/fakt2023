forrás = open('lottosz.dat', mode='r', encoding='utf-8')
számok = []
for sor in forrás:
    adat = sor.strip().split(' ')
    int_adat = [int(a) for a in adat]
    számok.append(int_adat)

forrás.close()

# 1-2. feladat, nyerőszámok:  89 24 34 11 64
utolsó_hét = input('Add meg az 52. heti számokat. ').split(' ')
utolsó_hét = sorted([int(a) for a in utolsó_hét])

print(f'{utolsó_hét}')

# 3-4.feladat

hét = int(input('Adj meg egy számot 1 és 51 között. '))
lotto_számok = számok[hét-1]
print(f'A {hét}. heti nyerőszámok: {lotto_számok}')




