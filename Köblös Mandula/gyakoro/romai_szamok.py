romai_szam = input("Adj meg egy római számot! ")

'''
M = 1000
D = 500
C = 100
L = 50
X = 10
V = 5
I = 1
'''

kod = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

szamok = []

for betu in romai_szam:
    if betu in kod:
        szamok.append(kod[betu])
    else:
        print('Nincs ilyen római szám')

print(szamok)

for i in range(len(szamok)-1):
    if szamok[i] < szamok[i+1]:
        szamok[i] *= -1

print(szamok)

arab_szam = 0
for i in range(len(szamok)):
    arab_szam += szamok[i]

print(sum(szamok))