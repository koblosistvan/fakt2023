szamok = []
for i in range(1, 26):
    szamok.append(i)

tiltott_szam = 3

print(f'Bumm({szamok[0]},{szamok[24]},{tiltott_szam})')

oszthatok = []

for i in range(len(szamok)):
    if szamok[i] % 3 == 0:
        oszthatok.append(szamok[i])

for i in range(len(szamok)):
    if szamok[i] in oszthatok or str(tiltott_szam) in str(szamok[i]):
        print('!!', end=' ')
    else:
        print(szamok[i], end=' ')
