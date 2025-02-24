forras = open('lista.txt', mode='r', encoding='utf-8')

adasba_kerules = []
cim = []
evad_es_epizod = []
hossz = []
megnezte = []

i = 0
for sor in forras:
    adat = sor.strip()
    if i%5 == 0:
        adasba_kerules.append(adat)
    if i%5 == 1:
        cim.append(adat)
    if i%5 == 2:
        evad_es_epizod.append(adat)
    if i%5 == 3:
        hossz.append(int(adat))
    if i%5 == 4:
        megnezte.append(int(adat))
    i += 1
forras.close()

print('2.feladat')
print(f'A listában {len(adasba_kerules)} db vetítési dátummal rendelkező epizód van.')

print('\n3. feladat')
latott_epizodok = 0
for i in range(len(adasba_kerules)):
    if megnezte[i] == 1:
        latott_epizodok += 1
print(f'A listában lévő epizódok {latott_epizodok/len(evad_es_epizod):0.2%}-át látta.')

print('\n2.feladat')
idotoltes = 0
for i in range(len(adasba_kerules)):
    if megnezte[i] == 1:
        idotoltes += hossz[i]
nap = idotoltes//1440
ora = (idotoltes-(nap*1440))//60
perc = (idotoltes-(nap*1440)-(ora*60))
print(f'Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.')

print('\n5.feladat')
datum = input('Adjon meg egy dátimot! Dátum=')
for i in range(len(adasba_kerules)):
    if adasba_kerules[i] <= datum and megnezte[i] == 0:
        print(f'{evad_es_epizod[i]}\t{cim[i]}')

def Hetnapja(ev, ho, nap):
