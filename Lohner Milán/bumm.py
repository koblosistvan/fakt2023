import math
szamok = []

for i in range(1,26):
    szamok.append(i)

tiltott=int(input('Add meg a tiltottat: '))
oszthatok = []
for i in range(len(szamok)):
    if szamok[i] % tiltott == 0:
        oszthatok.append(szamok[i])


for i in range(len(szamok)):
    if szamok[i] in oszthatok or str(tiltott) in str(szamok[i]):
    else: print(szamok[i])








