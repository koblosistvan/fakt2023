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

összes_szám = []
for i in range(len(számok)):
    összes_szám += számok[i]

# 5. feladat
for i in range(1, 91):
    if i not in összes_szám:
        print("Van olyan szám amit nem húztak ki.")
        break
else:
    print("Nem volt olyan szám amit nem húztak ki.")

# 6. feladat
páratlan = 0
for i in range(len(összes_szám)):
    if összes_szám[i] % 2 != 0:
        páratlan += 1
print(f'{páratlan} db páratlan számot húztak ki.')

# 7. feladat
számok.append(utolsó_hét)

kimenet = open("lotto52.ki", mode="w", encoding="utf-8")

for i in range(len(számok)):
    print(", ".join(map(str, számok[i])), file=kimenet)

kimenet.close()

