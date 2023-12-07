forras = open('forgalom.txt')

forras.readline()

idopont = []
athaladas = []
irany = []
ora = []

def idoosszead(ó, p, mp):
    return ó*3600+p*60+mp

for sor in forras:
    adat = sor.strip().split(' ')
    idopont.append(idoosszead(int(adat[0]), int(adat[1]), int(adat[2])))
    athaladas.append(int(adat[3]))
    irany.append(adat[4])
    ora.append(adat[0])

forras.close()



n = int(input('Add meg hogy melyik jármű irányát akarod megtudni: '))


if irany[n-1] == 'A':
        print('Felső irányába halad')
else:
    print('Alsó irányába halad')


felso_fele = []

i = len(idopont)

while len(felso_fele) < 2:
    i += 1
    if irany[i] == 'A':
        felso_fele.append(idopont[i])