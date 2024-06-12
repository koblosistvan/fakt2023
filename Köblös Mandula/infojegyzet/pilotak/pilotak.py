class Forma1:
    def __init__(self, nev, szuletesi_datum, nemzetiseg, rajtszam):
        self.nev = nev
        self.szuletesi_datum = szuletesi_datum
        self.nemzetiseg = nemzetiseg
        self.rajtszam = int(rajtszam) if rajtszam.isnumeric() else None

pilotak = []
forras = open('pilotak.txt', mode='r', encoding='utf-8')
forras.readline()
for sor in forras:
    adat = sor.strip().split(';')
    pilotak.append(Forma1(nev=adat[0], szuletesi_datum=adat[1], nemzetiseg=adat[2], rajtszam=adat[3]))
forras.close()

#3. feladat
print(f'3. feladat: {len(pilotak)}')

#4. feladat
print(f'4. feladat: {pilotak[-1].nev}')

#5. feladat
print('5.feladat:')
datumok = []
for i in range(len(pilotak)):
    ev = pilotak[i].szuletesi_datum.split('.')
    datumok.append(int(ev[0]))

for i in range(len(datumok)):
    if datumok[i] < 1901:
        print(f'\t\t{pilotak[i].nev} ({pilotak[i].szuletesi_datum})')

#6. feladat
legkisebb = 1000
legkisebb_id = 0
for i in range(len(pilotak)):
    if pilotak[i].rajtszam and pilotak[i].rajtszam < legkisebb:
        legkisebb = pilotak[i].rajtszam
        legkisebb_id = i
print(f'6.feladat: {pilotak[legkisebb_id].nemzetiseg}')