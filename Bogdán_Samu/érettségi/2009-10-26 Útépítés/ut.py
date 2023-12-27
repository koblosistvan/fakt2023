forrás = open('forgalom.txt')
össz = forrás.readline()
idő = []
óra = []
hossz = []
honnan = []
for i in forrás:
    sor = i.strip().split(' ')
    idő.append(int(sor[0]) * 3600 + int(sor[1]) * 60 + int(sor[2]))
    óra.append(int(sor[0]))
    hossz.append(int(sor[3]))
    honnan.append(sor[4])

n = int(input('2. feladat Adja meg a jármű sorszámát! '))
if honnan[n-1] == 'A':
    print('Felsőváros felé halad.')
else:
    print('Alsóváros felé halad.')

x = -1
ind = []
while len(ind) < 2:
    if honnan[x] == 'A':
        ind.append(x)
        x -= 1
    else:
        x -= 1
print(f'3. feladat {idő[ind[0]] - idő[ind[1]]} másodperc különbséggel érték el az útszakasz kezedetét.')

set_óra = list(set(óra))
irányok = []
a = 0
b = 0
x = []
while a <= len(set_óra) and b <= len(óra):
    if set_óra[a] == óra[b]:
        x.append(honnan[b])
        b += 1
    else:
        irányok.append(x)
        x = []
        a += 1
for i in range(len(set_óra)):
    print(óra[i], irányok[i].count('A'), irányok[i].count('B'))
