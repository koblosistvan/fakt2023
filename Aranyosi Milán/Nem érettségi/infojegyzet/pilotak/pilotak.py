class Forma1:
    def __init__(self, versenyzok, szuletesi_datum, nemzetiseg, rajtszam):
        self.versenyzok = versenyzok
        self.szuletesi_datum = szuletesi_datum
        self.nemzetiseg = nemzetiseg
        self.rajtszam = rajtszam



pilotak = []
forras = open('pilotak.txt', mode='r', encoding='utf-8')
forras.readline()
for sor in forras:
    adat = sor.strip().split(';')
    pilotak.append(Forma1(versenyzok=adat[0], szuletesi_datum=adat[1], nemzetiseg=adat[2], rajtszam=adat[3]))

forras.close()

#3. feladat:
print(f'3. feladat: {len(pilotak)}')

#4.feladat:
print(f'4. feladat: {pilotak[-1].versenyzok}')

#5. feladta
print(f'5. feladat:')
szulevek = []
for i in range(len(pilotak)):
    ev = pilotak[i].szuletesi_datum.split('.')
    szulevek.append(int(ev[0]))

for i in range(len(szulevek)):
    if szulevek[i] < 1901:
        print(f'\t\t{pilotak[i].versenyzok} ({pilotak[i].szuletesi_datum})')

#6. feladat
legkisebb = int(pilotak[0].rajtszam)
legkisebb_id = 0
for i in range(len(pilotak)):
    if  int(pilotak[i].rajtszam) < legkisebb:
        legkisebb = int(pilotak[i].rajtszam)
        legkisebb_id = i
print(f'{}')
