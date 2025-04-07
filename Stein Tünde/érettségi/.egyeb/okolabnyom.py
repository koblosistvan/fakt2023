forras = open('okolabnyom.txt', 'r', encoding='utf-8')
forras.readline()
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
    if gdp[i] != 'None':
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
    if gdp[i] != 'None':
        if gdp[i] > legk_gdp:
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
    if i:
        if orszag[i] != orszag[i-1]:
            counter += 1
    else:
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
        elif seged < 0:
            csokkent_13_ev.append(ev[i+1])
            csokkent_13_orszag.append(orszag[i+1])
print(f'A legnagyobb növekedés a felhasználás értékében {legn_nov_orszag}-ban {legn_nov_ev}-ben történt:\n'
      f'{elozo} => {legn_nov}.')

# 14
for i in range(len(csokkent_13_ev)):
    print(f'{csokkent_13_orszag[i]} felhasználása csökkent {csokkent_13_ev[i]-1} évről {csokkent_13_ev[i]} évre.')

# 15
top10felh_orszag = []
felhasznalas_15 = felhasznalas.copy()
orszag_15 = orszag.copy()
while len(top10felh_orszag) != 10:
    seged = max(felhasznalas_15)
    segedindex = felhasznalas_15.index(seged)
    segedorszag = orszag_15[segedindex]
    if orszag_15[segedindex] not in top10felh_orszag:
        top10felh_orszag.append(segedorszag)
        felhasznalas_15.remove(seged)
        orszag_15.remove(segedorszag)
        while segedorszag in orszag_15:
            if segedorszag in orszag_15:
                felhasznalas_15.remove(felhasznalas_15[orszag_15.index(segedorszag)])
                orszag_15.remove(segedorszag)
print(f'A legnagyobb felhasználók:\n{", ".join(sorted(top10felh_orszag))}')

# 16
top10k_orszag = []
kapacitas_16 = kapacitas.copy()
orszag_16 = orszag.copy()
while len(top10k_orszag) != 10:
    seged = max(kapacitas_16)
    segedindex = kapacitas_16.index(seged)
    segedorszag = orszag_16[segedindex]
    if orszag_16[segedindex] not in top10k_orszag:
        top10k_orszag.append(segedorszag)
        kapacitas_16.remove(seged)
        orszag_16.remove(segedorszag)
        while segedorszag in orszag_16:
            if segedorszag in orszag_16:
                kapacitas_16.remove(kapacitas_16[orszag_16.index(segedorszag)])
                orszag_16.remove(segedorszag)
print(f'A legnagyobb kapacitás:\n{", ".join(sorted(top10k_orszag))}')

# 17
metszet = []
unio = []
for i in top10felh_orszag:
    if i in top10k_orszag:
        metszet.append(i)
    if i not in unio:
        unio.append(i)
print(f'A két csoport úniója:\n{", ".join(sorted(unio))}\n'
      f'A két csoport metszete:\n{", ".join(sorted(metszet))}')

# 18
egyfore2014 = []
for i in range(len(felhasznalas)):
    if ev[i] == 2014:
        egyfore2014.append(felhasznalas[i]/lakossag[i])
segedlen = len(egyfore2014)
segedatl = sum(egyfore2014)/segedlen
segedmin = min(egyfore2014)
segedmax = max(egyfore2014)
egyfore2014.sort()
if segedlen % 2:
    med = egyfore2014[ int(segedlen/2) +1]
else:
    med = (egyfore2014[int(segedlen/2)] + egyfore2014[int((segedlen/2) + 1)]) / 2
szoras = 0
for i in egyfore2014:
    szoras += (i-segedatl) ** 2
szoras /= segedlen
szoras = szoras ** (1/2)
print(f'A 2014-es adatok statisztikai mutatói:\n'
      f'átlag: {segedatl} hektár\n'
      f'mimimum: {segedmin} hektár\n'
      f'maximum: {segedmax} hektár\n'
      f'terjedelem: {segedmax-segedmin} hektár\n'
      f'medián: {med} hektár\n'
      f'szórás: {szoras}')

