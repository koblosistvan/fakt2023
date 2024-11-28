forras = open('nfa light.txt', mode='r', encoding='utf-8')

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

#1. feladat
print(f'Az adatforrás {len(orszag)} sort tartalmaz.')

#2.
szamlalo = 0
for i in range(len(ev)):
    if ev[i] == 2014:
        szamlalo += 1

print(f'2014-ről {szamlalo} sort tartalmaz.')

#3
print(f'Az adatok {min(ev)}-{max(ev)} közötti évekere vonatkoznak.')

#4
kapmax = 0
kapmax_index = orszag[0]

for i in range(len(kapacitas)):
    if kapmax < kapacitas[i]:
        kapmax = kapacitas[i]
        kapmax_index = orszag[i]

print(f'A legnagyobb kapacitású ország {kapmax_index}, melynek kapacitása {int(kapmax)} hektár.')

#5
legkisebb_gdp = None
legkisebb_gdp_ev = ev[0]
legkisebb_gdp_orszag = orszag[0]

for i in range(len(gdp)):
    if (gdp[i] != None and legkisebb_gdp == None) or (gdp[i] != None and gdp[i] < legkisebb_gdp):
        legkisebb_gdp = gdp[i]
        legkisebb_gdp_orszag = orszag[i]
        legkisebb_gdp_ev = ev[i]

print(f'A legkisebb egy főre jutó GDP-je {legkisebb_gdp_orszag}-nak volt {legkisebb_gdp_ev} évben: {round(legkisebb_gdp)} USD/fő.')

#6
ketezer_kap = 0
tizennegy_kap = 0

ketezer_felhaszn = 0
tizennegy_felhaszn = 0

for i in range(len(kapacitas)):
    if ev[i] == 2000:
        ketezer_kap += kapacitas[i]
        ketezer_felhaszn += felhasznalas[i]
    if ev[i] == 2014:
        tizennegy_kap += kapacitas[i]
        tizennegy_felhaszn += felhasznalas[i]

print(f'A kapacitás 2000-től 2014-ig {round(ketezer_kap)}-ről {round(tizennegy_kap)}-re változott, míg a felhasználás {round(ketezer_felhaszn)}-ről {round(tizennegy_felhaszn)}-re.')

#7
ketezer_arany = ketezer_felhaszn / ketezer_kap
tizennegy_arany = tizennegy_felhaszn / tizennegy_kap

if ketezer_arany > tizennegy_arany:
    print('csökkent')
else:
    print('nőtt')

#8
ketezer_lakossag = 0
tizennegy_lakossag = 0
for i in range(len(lakossag)):
    if ev[i] == 2000:
        ketezer_lakossag += lakossag[i]
    if ev[i] == 2014:
        tizennegy_lakossag += lakossag[i]

print(ketezer_lakossag)



