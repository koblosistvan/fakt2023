elso = input().split(' ')
n = int(elso[0])
l = int(elso[1])
s = []
f = []
for i in range(n):
    masodik = input().split(' ')
    s.append(int(masodik[0]))
    f.append(int(masodik[1]))
sorok = s.copy()
fontossag = f.copy()
vegsosorok = 0
fontossaguk = 0
sorszamlista = []
for i in range(len(sorok)-1):
    for k in range(len(sorok)-1):
        if fontossag[k] < fontossag[k+1]:
            fontossag[k], fontossag[k+1] = fontossag[k+1], fontossag[k]
            sorok[k], sorok[k + 1] = sorok[k + 1], sorok[k]
sorok_szama = l
for i in range(len(sorok)):
    if sorok_szama - sorok[i] >= 0:
        sorok_szama -= sorok[i]
        vegsosorok += sorok[i]
        fontossaguk += fontossag[i]
        c = f.index(fontossag[i])
        sorszamlista.append(c + 1)
        f.remove(f[f.index(fontossag[i])])
print(f'{vegsosorok} {fontossaguk}')
print(*sorszamlista)

