forrás = open('NFA light.csv', mode='r', encoding='utf-8')

forrás.readline()

kód = []
ország = []
régió = []
év = []
felhasználás = []
kapacitás = []
lakosság = []
gdp = []

for sor in forrás:
    adat = sor.strip().split(',')
    kód.append(adat[0])
    ország.append(adat[1])
    régió.append(adat[2])
    év.append(int(adat[3]))
    felhasználás.append(float(adat[4]))
    kapacitás.append(float(adat[5]))
    lakosság.append(int(adat[6]))
    gdp.append(adat[7])

for i in range(len(gdp)):
    if gdp[i] != 'None':
        gdp[i] = float(gdp[i])

forrás.close()

#1
print(f'Az adatforrás {len(kód)} sort tartalmaz.')

#2
adat_2014 = 0
for i in range(len(év)):
    if év[i] == 2014:
        adat_2014 += 1
print(f'2014-ről {adat_2014} sort tartalmaz.')

#3
min = év[0]
max = év[0]
for i in range(len(év)):
    if min > év[i]:
        min = év[i]
    elif max < év[i]:
        max = év[i]
print(f'Az adatok {min}-{max} közötti évekre vonatkoznak.')

#4
legn_kapacitas = 0
legn_k_orszag = 0
for i in range(len(kapacitás)):
    if kapacitás[i] > legn_kapacitas:
        legn_kapacitas = kapacitás[i]
        legn_k_orszag = i
print(f'A legnagyobb kapacitású ország {ország[legn_k_orszag]}, melynek kapacitása {legn_kapacitas} hektár.')
