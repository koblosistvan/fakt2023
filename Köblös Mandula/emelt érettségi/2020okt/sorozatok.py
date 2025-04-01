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

eve = []
honapja = []
napja = []
for a in adasba_kerules:
    if a != 'NI':
        x = a.strip().split('.')
        eve.append(int(x[0]))
        honapja.append(int(x[1]))
        napja.append(int(x[2]))
    else:
        eve.append(a)
        honapja.append(a)
        napja.append(a)

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
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev-1
    hetnapja = napok[(ev + ev//4 - ev//100 + ev//400 + honapok[ho-1] + nap)%7]
    return hetnapja

print('\n7.feladat')
napi_filmek = []
adott_nap = input('Adja meg a hét egy napját (például cs)! Nap=')
for i in range(len(adasba_kerules)):
    if eve[i] != 'NI' and adott_nap == Hetnapja(eve[i], honapja[i], napja[i]):
        napi_filmek.append(cim[i])

if len(napi_filmek) == 0:
    print('Az adott napon nem kerül sor adásba sorozat.')
else:
    print('\n'.join(set(napi_filmek)))

kiiras = open('summ.txt', mode='w', encoding='utf-8')

cim_kiiras = cim[0]
szamlalo_perc = 0
szamlalo_resz = 0
for i in range(len(adasba_kerules)-1):
    if cim[i] == cim[i+1]:
        szamlalo_resz += 1
        szamlalo_perc += hossz[i]
        cim_kiiras = cim[i]
    else:
        print(f'{cim_kiiras} {szamlalo_perc + hossz[i]} {szamlalo_resz + 1}', file=kiiras)
        szamlalo_perc = 0
        szamlalo_resz = 0
if cim[-1] == cim[-2]:
    print(f'{cim_kiiras} {szamlalo_perc + hossz[-1]} {szamlalo_resz + 1}', file=kiiras)
else:
    print(f'{cim[-1]} {hossz[-1]} 1', file=kiiras)

kiiras.close()