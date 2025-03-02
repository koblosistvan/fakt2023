import math
forras = open('lista.txt', mode='r', encoding='utf-8')

datum = []
cim = []
evaddepizod = []
hossz = []
megneztee= []

szamlalo = 0

for sor in forras:
    if szamlalo % 5 == 0:
        datum.append(sor.strip())
    elif szamlalo % 5 == 1:
        cim.append(sor.strip())
    elif szamlalo % 5 == 2:
        evaddepizod.append(sor.strip())
    elif szamlalo % 5 == 3:
        hossz.append(int(sor.strip()))
    else:
        megneztee.append(int(sor.strip()))
    szamlalo += 1
    segedlista = []

forras.close()

print('2. feladat')
rendesdatum = 0
for i in range(len(datum)):
    if datum[i] != 'NI':
        rendesdatum += 1

print(f'A listában {rendesdatum} db vetítési dátummal rendelkező epizód van.')


print('\n3. feladat')
latta_szamlalo = 0
for i in range(len(megneztee)):
    if megneztee[i] == 1:
        latta_szamlalo += 1

print(f'A listában lévő epizódok {latta_szamlalo/len(megneztee):0.2%}-át látta.')

print('\n4. feladat')
idot_toltott = 0
for i in range(len(megneztee)):
    if megneztee[i] == 1:
        idot_toltott += hossz[i]

idot_toltott_nap = idot_toltott // (24*60)

idot_toltott_ora = (idot_toltott % (24*60)) // 60

idot_toltott_perc = (idot_toltott % (24*60*60)) % (60)

print(f'Sorozatnézéssel {idot_toltott_nap} napot {idot_toltott_ora} órát és {idot_toltott_perc} percet töltött.')

print('\n5. feladat')

adott_datum = input('Adjon meg egy dátumot! Dátum=')

for i in range(len(datum)):
    if datum[i] != 'NI':
        bontott_adott_datum = adott_datum.split('.')
        bontott_rendes_datum = datum[i].split('.')
        if megneztee[i] == 0:
            if int(bontott_adott_datum[0]) >= int(bontott_rendes_datum[0]):
                if int(bontott_adott_datum[1]) >= int(bontott_rendes_datum[1]):
                    if int(bontott_adott_datum[2]) >= int(bontott_rendes_datum[2]):
                        print(f'{evaddepizod[i]}\t{cim[i]}')

def Hetnapja(ev, honap, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if honap < 3:
        ev = ev-1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[honap - 1] + nap) % 7]
    return hetnapja

print('\n7. feladat')

adott_hetnapja = input('Adja meg a hét egy napját (például cs) ! Nap= ')

aznap_vetitik = []

for i in range(len(datum)):
    if datum[i] != 'NI':
        bontott_rendes_datum = datum[i].split('.')
        if adott_hetnapja == Hetnapja(int(bontott_rendes_datum[0]), int(bontott_rendes_datum[1]), int(bontott_rendes_datum[2])):
            if cim[i] not in aznap_vetitik:
                aznap_vetitik.append(cim[i])

if len(aznap_vetitik) == 0:
    print(f'Az adott napon nem kerül adásba sorozat.')
else:
    for i in range(len(aznap_vetitik)):
        print(aznap_vetitik[i])


kimenet = open('summa.txt', mode='w', encoding='utf-8')

cime = []
vetitesi_ido = []
epizodok_szama = []
vetites_ido_szaml = 0
epizodok_szaml = 0
for i in range(len(hossz)-1):
    if cim[i] != cim[i+1]:
        vetites_ido_szaml += hossz[i]
        epizodok_szaml += 1
        cime.append(cim[i])
        vetitesi_ido.append(vetites_ido_szaml)
        epizodok_szama.append(epizodok_szaml)
        epizodok_szaml = 0
        vetites_ido_szaml = 0
    if cim[i] == cim[i+1]:
        epizodok_szaml += 1
        vetites_ido_szaml += hossz[i]

for i in range(len(cime)):
    print(f'{cime[i]} {vetitesi_ido[i]} {epizodok_szama[i]}', file=kimenet)

kimenet.close()