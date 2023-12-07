forras = open('forgalom.txt', mode='r', encoding='utf-8')
forras.readline()

idopont = []
athaladas = []
irany = []

def idomp(o, p, mp):
    return o*3600+p*60+mp

for i in forras:
    adat = i.strip().split(' ')
    idopont.append(idomp(int(adat[0]), int(adat[1]), int(adat[2])))
    athaladas.append(int(adat[3]))
    irany.append(adat[4])
print(idopont)
print(athaladas)
print(irany)
forras.close()

#2.feladat
n = 1 #int(input('Add meg, hogy hányadik jármű iráyára vgagy kiváncsi:'))
if irany[n-1] == 'A':
    print('Felső város irányába halad')
else:
    print('Alsó város irányába halad')


felso_fele = []
i = len(idopont)
while len(felso_fele) < 2:
    i -= -1
    if irany[i] == 'A':
        felso_fele.append(idopont[i])
print(idopont[1] - idopont[0])