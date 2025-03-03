forras = open('NFA light.csv', mode='r', encoding='utf-8')

orszag = []
regio = []
ev = []
felhasznalas = []
kapacitas = []
lakossag = []
gdp = []

forras.readline()

for sor in forras:
    adat = sor.strip().split(',')
    orszag.append(adat[1])
    regio.append(adat[2])
    ev.append(int(adat[3]))
    felhasznalas.append(float(adat[4]))
    kapacitas.append(float(adat[5]))
    lakossag.append(int(adat[6]))
    if adat[7] != 'None':
        gdp.append(float(adat[7]))
    else:
        gdp.append(None)

forras.close()


print(f'A forras {len(orszag)} sort tartalmaz.')


szaml = 0
for i in range(len(ev)):
    if ev[i] == 2014:
        szaml += 1

print(f'2014-ről {szaml} adatot tartalmaz.')


print(f'Az adatok {min(ev)}-{max(ev)} kozotti evekre vonatkoznak')

max1 = 0
max1i = orszag[0]

for i in range(len(kapacitas)):
    if max1 < kapacitas[i]:
        max1 = kapacitas[i]
        max1i = orszag[i]

print(f'A legnagyobb kapacitású ország {max1i}, melynek kapacitása {int(max1)} hektár.')



kisgdp = None
mingpt = ev[0]
mingpto = orszag[0]

for i in range(len(gdp)):
    if (gdp[i] != None and kisgdp == None) or (gdp[i] != None and gdp[i] < kisgdp):
        kisgdp = gdp[i]
        mingpto = orszag[i]
        mingpt = ev[i]

print(f'A legkisebb egy főre jutó GDP-je {mingpto}-nak volt {mingpt} évben: {round(kisgdp)} USD/fő.')




ketezer = 0
tizennegy = 0

ketezer_felhaszn = 0
tizennegy_felhaszn = 0

for i in range(len(kapacitas)):
    if ev[i] == 2000:
        ketezer += kapacitas[i]
        ketezer_felhaszn += felhasznalas[i]
    if ev[i] == 2014:
        tizennegy += kapacitas[i]
        tizennegy_felhaszn += felhasznalas[i]

print(f'A kapacitás 2000-től 2014-ig {round(ketezer)}-ről {round(tizennegy)}-re változott, míg a felhasználás {round(ketezer_felhaszn)}-ről {round(tizennegy_felhaszn)}-re.')


etezer_arany = ketezer_felhaszn / ketezer
tizennegy_arany = tizennegy_felhaszn / tizennegy

if ketezer > tizennegy_arany:
    print('csokken')
else:
    print('no')


ketezer_lakossag = 0
tizennegy_lakossag = 0

for i in range(len(lakossag)):
    if ev[i] == 2000:
        ketezer_lakossag += lakossag[i]
    if ev[i] == 2014:
        tizennegy_lakossag += lakossag[i]

print(f'Az egy főre jutó átlagos felhasználás 2000-ben {ketezer_felhaszn/ketezer_lakossag:0.3f} hektár volt, 2014-re {tizennegy_felhaszn/tizennegy_lakossag:0.3f}-re változott, ami %-os növekedést jelent.')


print(f'Az egy főre jutó átlagos kapacitás 1980-ben {ketezer/ketezer_lakossag:0.3f} hektár volt, 2014-re {tizennegy/tizennegy_lakossag:0.3f}-re változott, ami 28%-os csökkenést jelent.')

hatar = int(input('Add meg az alsó határt:'))
print(f'Az alábbi országokban volt az egy főre jutó felhasználás {hatar} hektár fölötti:')
for i in range(len(ev)):
    if felhasznalas[i]/lakossag[i] > hatar:
        print(f'{orszag[i]} - {ev[i]}: {felhasznalas[i]/lakossag[i]:0.3f} hektár')

szaml = 0

csakorszagok = []
for i in range(len(orszag)):
    if orszag[i] not in csakorszagok:
        csakorszagok.append(orszag[i])
print(f'Az adatok {len(csakorszagok)} ország adatait tartalmazzák.')

maxvalt = felhasznalas[1] - felhasznalas[0]
maxvaltev = ev[0]
maxorszvalt = orszag[0]
maxfelht = 0
maxfelhidei = 0

for i in range(len(felhasznalas)-1):
    if orszag[i] == orszag[i+1]:
        adott_felh = felhasznalas[i+1] - felhasznalas[i]
        if adott_felh > maxvalt:
            maxvalt = adott_felh
            maxfelhidei = felhasznalas[i]
            maxfelht = felhasznalas[i + 1]
            maxorszvalt = orszag[i]
            maxvaltev = ev[i + 1]
print(f'A legnagyobb növekedés a felhasználás értékében {maxorszvalt}-ban {maxvaltev}-ben történt:\n{int(maxfelhidei)} => {int(maxfelht)}.')

csokk_felh_orsz = []
csokk_felh_evn = []
csokk_felh_ev = []

for i in range(len(felhasznalas)-1):
    if orszag[i] == orszag[i+1]:
        if felhasznalas[1] - felhasznalas[i+1] > 0:
            csokk_felh_orsz.append(orszag[i])
            csokk_felh_ev.append(ev[i])
            csokk_felh_evn.append(ev[i+1])

for i in range(len(csokk_felh_orsz)):
    print(f'{csokk_felh_orsz[i]} felhasználása csökkent {csokk_felh_ev[i]} évről {csokk_felh_evn[i]} évre.')