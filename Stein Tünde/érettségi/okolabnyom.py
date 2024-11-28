forras = open('okolabnyom.txt', 'r', encoding='utf-8')
lnevek = forras.readline()
kod = []
orszag = []
regio = []
ev = []
felhasznalas = []
kapacitas = []
lakossag = []
gdp = []
for sor in forras:
    i = sor.strip().split(',')
    kod.append(i[0])
    orszag.append(i[1])
    regio.append(i[2])
    ev.append(int(i[3]))
    felhasznalas.append(float(i[4]))
    kapacitas.append(float(i[5]))
    lakossag.append(int(i[6]))
    gdp.append(i[7])
for i in range(len(gdp)):
    if gdp[i]:
        gdp[i] = float(gdp[i])
forras.close()

# 1
print(f'Az adatforrás {len(kod)} sort tartalmaz.')

# 2
counter = 0
for i in ev:
    if i == 2014:
        counter += 1
print(f'2014-ről {counter} sort tartalmaz.')

# 3
print(f'Az adatok {min(ev)}-{max(ev)} közötti évekere vonatkoznak.')

# 4
legn_k = kapacitas[0]
legn_k_orszag = ''
for i in range(len(kapacitas)):
    if kapacitas[i] > legn_k:
        legn_k = kapacitas[i]
        legn_k_orszag = orszag[i]
print(f'A legnagyobb kapacitású ország {legn_k_orszag}, melynek kapacitása {legn_k} hektár.')

# 5
legk_gdp = -1
legk_gdp_orszag = ''
legk_ev = 0
for i in range(len(gdp)):
    if gdp and gdp[i] > legk_gdp:
        legk_gdp = gdp[i]
        legk_gdp_orszag = orszag[i]
        legk_ev = ev[i]
print(f'A legkisebb egy főre jutó GDP-je {legk_gdp_orszag}-nak volt {legk_ev} évben: {legk_gdp} USD/fő.')

# 6
teljes_k_00 = 0
teljes_k_14 = 0
teljes_felh_00 = 0
teljes_felh_14 = 0
lak8_00 = 0
lak8_14 = 0
for i in range(len(kapacitas)):
    if ev[i] == 2000:
        teljes_k_00 += kapacitas[i]
        teljes_felh_00 += felhasznalas[i]
        lak8_00 = lakossag[i]
    elif ev[i] == 2014:
        teljes_k_14 += kapacitas[i]
        teljes_felh_14 += felhasznalas[i]
        lak8_14 = lakossag[i]
print(f'A kapacitás 2000-től 2014-ig {teljes_k_00}-ről {teljes_k_14}-re változott, míg a '
      f'felhasználás {teljes_felh_00}-ről {teljes_felh_14}-re.')

# 7
print(f'A két érték aránya {teljes_felh_00/teljes_k_00}%-ról {teljes_felh_14/teljes_k_14}%-ra nőtt.')

# 8
atl_felh_volt = teljes_felh_00/lak8_00
atl_felh_lesz = teljes_felh_14/lak8_14
valtozas_felh = (atl_felh_lesz*100)/atl_felh_volt - 100
if valtozas_felh > 0:
    n_cs_f = 'növekedés'
elif valtozas_felh < 0:
    n_cs_f = 'csökkenés'
print(f'Az egy főre jutó átlagos felhasználás 2000-ben {atl_felh_volt} hektár volt,'
      f'2014-re {atl_felh_lesz}-re változott, ami {abs(valtozas_felh)}-os {n_cs_f}t jelent.')

# 9
atl_k_volt = teljes_k_00/lak8_00
atl_k_lesz = teljes_k_14/lak8_14
valtozas_k = (atl_k_lesz*100)/atl_k_volt - 100
if valtozas_k > 0:
    n_cs_k = 'növekedés'
elif valtozas_k < 0:
    n_cs_k = 'csökkenés'
print(f'Az egy főre jutó átlagos felhasználás 2000-ben {atl_k_volt} hektár volt,'
      f'2014-re {atl_k_lesz}-re változott, ami {abs(valtozas_k)}-os {n_cs_f}t jelent.')

# 10
alsoh = float(input('> '))
print(f'Az alábbi országokban volt az egy főre jutó felhasználás {alsoh} hektár fölötti:')
for i in range(len(felhasznalas)):
    if felhasznalas[i] > alsoh:
        print(f'{orszag[i]} - {ev[i]}: {felhasznalas[i]} hektár')
# 11
counter = 0
for i in range(len(orszag)):
    if i and orszag[i] != orszag[i-1]:
        counter += 1
print(f'Az adatok {counter} ország adatait tartalmazzák.')

# 12
legn_nov = felhasznalas[1]-felhasznalas[0]
legn_nov_orszag = ''
legn_nov_ev = 0
csokkent_13_ev = []
csokkent_13_orszag = []
for i in range(len(felhasznalas)-1):
    if orszag[i+1] == orszag[i]:
        seged = felhasznalas[i+1] - felhasznalas[i]
        if seged > legn_nov:
            elozo = legn_nov
            legn_nov = felhasznalas[i+1] - felhasznalas[i]
            legn_nov_orszag = orszag[i+1]
            legn_nov_ev = ev[i+1]
        if seged < 0:
            csokkent_13_ev.append(ev[i+1])
            csokkent_13_orszag.append(orszag[i+1])
print(f'A legnagyobb növekedés a felhasználás értékében {legn_nov_orszag}-ban {legn_nov_ev}-ben történt:\n'
      f'{elozo} => {legn_nov}.')

# 13

print(f'Aruba felhasználása csökkent 1991 évről 1992 évre.')
'''

A legnagyobb felhasználók:
Brazil, China, Germany, India, Indonesia, Japan, Russian Federation, USSR, United 
Kingdom, United States of America
A legnagyobb kapacitás:
Argentina, Australia, Brazil, Canada, China, India, Indonesia, Russian Federation, 
USSR, United States of America
A két csoport úniója:
Argentina, Australia, Brazil, Canada, China, Germany, India, Indonesia, Japan, 
Russian Federation, USSR, United Kingdom, United States of America
A két csoport metszete:
Brazil, China, India, Indonesia, Russian Federation, USSR, United States of America
A 2014-es adatok statisztikai mutatói:
átlag: 3.349 hektár
mimimum: 0.503 hektár
maximum: 15.654 hektár
terjedelem: 15.152 hektár
medián: 2.872 hektár
szórás: 2.29'''