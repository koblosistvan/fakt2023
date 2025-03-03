class Pilotak:
    def __init__(self, nev, szuletes, nemzetiseg, rajtszam):
        self.nev=nev
        self.szuletes=szuletes
        self.nemzetiseg=nemzetiseg
        self.rajtszam=rajtszam

osszesadat=[]

forras=open('pilotak.csv', mode='r', encoding='utf-8')

forras.readline()

for sor in forras:
    adat=sor.strip().split(';')
    osszesadat.append(Pilotak(nev=(adat[0]), szuletes=(adat[1]), nemzetiseg=(adat[2]), rajtszam=(adat[3])))

forras.close()

print(f'Az adatsor {len(osszesadat)} adatot tartalmaz')

print(f'{osszesadat[-1].nev} az uccsó név')


szulevek=[]


for i in range(len(osszesadat)):
    ev=osszesadat[i].szuletes.split('.')
    szulevek.append(int(ev[0]))

for i in range(len(szulevek)):
    if szulevek[i]<1900:
        print(f'{osszesadat[i].nev} {osszesadat[i].szuletes}')

for i in range(len(osszesadat)):
    legkisebb=[sorted(osszesadat, reverse=True, key=lambda a: a.rajtszam)]
    if osszesadat[i].rajtszam==None:
        legkisebb