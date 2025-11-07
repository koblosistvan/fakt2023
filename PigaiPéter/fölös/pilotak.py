class Versenyzo:
    def __init__(self, nev: str, szuletes:str, nemzetiseg:str, rajtszam:str):
        self.nev = nev
        self.szuletes = szuletes
        self.nemzetiseg = nemzetiseg
        self.rajtszam = rajtszam

data = []
forras = open('PigaiPéter\\pilotak.csv', mode='r', encoding='utf-8')
forras.readline()
for i in forras:
    sor = i.strip().split(';')
    data.append(Versenyzo(nev=sor[0], szuletes=sor[1], nemzetiseg=sor[2], rajtszam=sor[3]))

#
print(f'3.feladat: {len(data)}')

#
print(f'4.feladat: {data[-1].nev}')

#
ev = []
for i in data:
    datum = i.szuletes.split('.')
    ev.append(datum[0])
print(f'5.feladat:')
for i in range(len(ev)):
    if int(ev[i]) < 1901:
        print(f'\t{data[i].nev} {data[i].szuletes}')

#
counter = -1
rajtszamok = []
id = []
for i in data:
    counter +=1
    if i.rajtszam != '':
        rajtszamok.append(int(i.rajtszam))
        id.append(counter)
print(f'6.feladat: {data[id[rajtszamok.index(min(rajtszamok))]].nemzetiseg}')

#
tobbszor = set()
for i in rajtszamok:
    if rajtszamok.count(i) > 1:
        tobbszor.add(str(i))
print(f'7.feladat: {", ".join(list(tobbszor))}')