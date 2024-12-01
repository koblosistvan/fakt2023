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

#2. feladat
szamlalo = 0
for i in range(len(ev)):
    if ev[i] == 2014:
        szamlalo += 1

print(f'2014-ről {szamlalo} sort tartalmaz.')

#3. feladat
print(f'Az adatok {min(ev)}-{max(ev)} közötti évekere vonatkoznak.')

#4. feladat
kapmax = 0
kapmax_index = orszag[0]

for i in range(len(kapacitas)):
    if kapmax < kapacitas[i]:
        kapmax = kapacitas[i]
        kapmax_index = orszag[i]

print(f'A legnagyobb kapacitású ország {kapmax_index}, melynek kapacitása {int(kapmax)} hektár.')

#5. feladat
legkisebb_gdp = None
legkisebb_gdp_ev = ev[0]
legkisebb_gdp_orszag = orszag[0]

for i in range(len(gdp)):
    if (gdp[i] != None and legkisebb_gdp == None) or (gdp[i] != None and gdp[i] < legkisebb_gdp):
        legkisebb_gdp = gdp[i]
        legkisebb_gdp_orszag = orszag[i]
        legkisebb_gdp_ev = ev[i]

print(f'A legkisebb egy főre jutó GDP-je {legkisebb_gdp_orszag}-nak volt {legkisebb_gdp_ev} évben: {round(legkisebb_gdp)} USD/fő.')

#6. feladat
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

#7. feladat
ketezer_arany = ketezer_felhaszn / ketezer_kap
tizennegy_arany = tizennegy_felhaszn / tizennegy_kap

if ketezer_arany > tizennegy_arany:
    print('csökkent')
else:
    print('nőtt')

#8. feladat
ketezer_lakossag = 0
tizennegy_lakossag = 0

for i in range(len(lakossag)):
    if ev[i] == 2000:
        ketezer_lakossag += lakossag[i]
    if ev[i] == 2014:
        tizennegy_lakossag += lakossag[i]

print(f'Az egy főre jutó átlagos felhasználás 2000-ben {ketezer_felhaszn/ketezer_lakossag:0.3f} hektár volt, 2014-re {tizennegy_felhaszn/tizennegy_lakossag:0.3f}-re változott, ami %-os növekedést jelent.')

#9. feladat
print(f'Az egy főre jutó átlagos kapacitás 1980-ben {ketezer_kap/ketezer_lakossag:0.3f} hektár volt, 2014-re {tizennegy_kap/tizennegy_lakossag:0.3f}-re változott, ami 28%-os csökkenést jelent.')

#10. feladat
hatar = int(input('Add meg az alsó határt:'))
print(f'Az alábbi országokban volt az egy főre jutó felhasználás {hatar} hektár fölötti:')
for i in range(len(ev)):
    if felhasznalas[i]/lakossag[i] > hatar:
        print(f'{orszag[i]} - {ev[i]}: {felhasznalas[i]/lakossag[i]:0.3f} hektár')

#11. feladat
szaml = 0
csakorszagok = []
for i in range(len(orszag)):
    if orszag[i] not in csakorszagok:
        csakorszagok.append(orszag[i])
print(f'Az adatok {len(csakorszagok)} ország adatait tartalmazzák.')

 #12. feladat
max_felh_valtozas = felhasznalas[1] - felhasznalas[0]
max_felh_valtozas_orsz = orszag[0]
max_felh_valtozas_ev = ev[0]
max_felh_valtozas_idei = 0
max_felh_valtozas_tavalyi = 0

for i in range(len(felhasznalas)-1):
    if orszag[i] == orszag[i+1]:
        adott_felh = felhasznalas[i+1] - felhasznalas[i]
        if adott_felh > max_felh_valtozas:
            max_felh_valtozas = adott_felh
            max_felh_valtozas_idei = felhasznalas[i]
            max_felh_valtozas_tavalyi = felhasznalas[i+1]
            max_felh_valtozas_orsz = orszag[i]
            max_felh_valtozas_ev = ev[i+1]
print(f'A legnagyobb növekedés a felhasználás értékében {max_felh_valtozas_orsz}-ban {max_felh_valtozas_ev}-ben történt:\n{int(max_felh_valtozas_idei)} => {int(max_felh_valtozas_tavalyi)}.')

#14. feladat
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

#15.feladat
legn_felh_orszagok = []

while len(legn_felh_orszagok) <= 10:
    for i in range(len(felhasznalas)):
        if felhasznalas[i] ==  max(felhasznalas):
            if orszag[i] not in legn_felh_orszagok:
                legn_felh_orszagok.append(orszag[i])
                felhasznalas.remove(felhasznalas[i])
print(legn_felh_orszagok)





#A legnagyobb felhasználók:
#Brazil, China, Germany, India, Indonesia, Japan, Russian Federation, USSR, United
#Kingdom, United States of America
#A legnagyobb kapacitás:
#Argentina, Australia, Brazil, Canada, China, India, Indonesia, Russian Federation,
#USSR, United States of America
#A két csoport úniója:
#Argentina, Australia, Brazil, Canada, China, Germany, India, Indonesia, Japan,
#Russian Federation, USSR, United Kingdom, United States of America
#A két csoport metszete:
#Brazil, China, India, Indonesia, Russian Federation, USSR, United States of America