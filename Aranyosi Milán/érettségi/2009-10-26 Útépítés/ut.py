forras = open('forgalom.txt', mode='r', encoding='utf-8')
forras.readline()

idopont = []
athaladas = []
irany = []
orak = []

def idomp(o, p, mp):
    return o*3600+p*60+mp

for i in forras:
    adat = i.strip().split(' ')
    orak.append(int(adat[0]))
    idopont.append(idomp(int(adat[0]), int(adat[1]), int(adat[2])))
    athaladas.append(int(adat[3]))
    irany.append(adat[4])
forras.close()

#2.feladat
n = int(input('Add meg, hogy hányadik jármű iráyára vgagy kiváncsi:'))
if irany[n-1] == 'A':
    print('Felső város irányába halad')
else:
    print('Alsó város irányába halad')

#3.feladat
ind = []
i = -1
while len(ind) < 2:
    if irany[i] == 'A':
        ind.append(i)
        i -= 1
    else:
        i -= 1
print(idopont[ind[0]] - idopont[ind[1]])

#4.feladat
print(orak)
for i in
for i in range(1,24):
    szamlalo = 0
    alsoszamlalo = 0
    felso_szamlalo = 0
    if i == orak[i]:
        szamlalo += 1
        if irany[i] == 'A':
            alsoszamlalo += 1
        else:
            felso_szamlalo += 1
    print(szamlalo, alsoszamlalo, felso_szamlalo)
