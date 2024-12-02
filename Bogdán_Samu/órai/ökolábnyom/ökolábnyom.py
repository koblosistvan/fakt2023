def átlag(x, x1, x2):
    if round((x1 / lakosság1), 3) > round((x2 / lakosság2), 3):
        print(f'Az egy főre jutó átlagos {x} {év1}-ban/ben {round((x1 / lakosság1), 3)} hektár volt, {év2}-ra/re {round((x2 / lakosság2), 3)}-ra/re változott, ami {int(round(((round((x1 / lakosság1), 3) / round((x2 / lakosság2), 3)) - 1) * 100))}%-os csökkenést jelent.')
    elif round((x1 / lakosság1), 3) < round((x2 / lakosság2), 3):
        print(f'Az egy főre jutó átlagos {x} {év1}-ban/ben {round((x1 / lakosság1), 3)} hektár volt, {év2}-ra/re {round((x2 / lakosság2), 3)}-ra/re változott, ami {int(round(((round((x2 / lakosság2), 3) / round((x1 / lakosság1), 3)) - 1) * 100))}%-os növekedést jelent.')
    else:
        print(f'Az egy főre jutó átlagos {x} mindkét évben egyaránt {round((x1 / lakosság1), 3)} hektár volt.')


ökolábnyom = open('Bogdán_Samu\\órai\\ökolábnyom\\ökolábnyom.csv', 'r', encoding='utf-8')

ökolábnyom.readline()
kód = []
ország = []
régió = []
év = []
felhasználás = []
felhasználás_alt = []
kapacitás = []
lakosság = []
lakosság_alt = []
gdp = []
gdp_adat = []
for i in ökolábnyom:
    x = i.strip().split(',')
    kód.append(x[0])
    ország.append(x[1])
    régió.append(x[2])
    év.append(int(x[3]))
    felhasználás.append(float(x[4]))
    felhasználás_alt.append(float(x[4]))
    kapacitás.append(float(x[5]))
    lakosság.append(int(x[6]))
    lakosság_alt.append(int(x[6]))
    if x[7] == 'None':
        gdp.append(x[7])
    else:
        gdp.append(float(x[7]))
        gdp_adat.append(float(x[7]))

ökolábnyom.close()

print(f'Az adatforrás {len(kód)} sort tartalmaz.')

print(f'2014-ről {év.count(2014)} sort tartalmaz.')

print(f'Az adatok {min(év)}-{max(év)} közötti évekere vonatkoznak.')

print(f'A legnagyobb kapacitású ország {ország[kapacitás.index(max(kapacitás))]}, melynek kapacitása {int(max(kapacitás)):,} hektár.')

print(f'A legkisebb egy főre jutó GDP-je {ország[gdp.index(min(gdp_adat))]}-nak/nek volt {év[gdp.index(min(gdp_adat))]} évben: {int(round(min(gdp_adat), 0))} USD/fő.')

év1 = int(input('Adja meg az első évet! '))
év2 = int(input('Adja meg a második évet! '))

kap1 = 0
fel1 = 0
lakosság1 = 0

kap2 = 0
fel2 = 0
lakosság2 = 0

for i in range(len(kód)):
    if év[i] == év1:
        kap1 += kapacitás[i]
        fel1 += felhasználás[i]
        lakosság1 += lakosság[i]
    if év[i] == év2:
        kap2 += kapacitás[i]
        fel2 += felhasználás[i]
        lakosság2 += lakosság[i]

kap1 = int(round(kap1))
fel1 = int(round(fel1))

kap2 = int(round(kap2))
fel2 = int(round(fel2))

print(f'A kapacitás {év1}-tól/től {év2}-ig {kap1:,}-ról/ről {kap2:,}-ra/re változott, míg a felhasználás {fel1:,}-ról/ről {fel2:,}-ra/re.')

if (int(round(fel1 / kap1))) > (int(round(fel2 / kap2))):
    print(f'A két érték aránya {int(round(fel1 / kap1 * 100))}%-ról/ről {int(round(fel2 / kap2 * 100))}%-ra/re csökkent.')
elif (int(round(fel1 / kap1))) < (int(round(fel2 / kap2))):
    print(f'A két érték aránya {int(round(fel1 / kap1 * 100))}%-ról/ről {int(round(fel2 / kap2 * 100))}%-ra/re nőtt.')
else:
    print(f'A két érték aránya {int(round(fel1 / kap1 * 100))}% volt mindkét évben.')

átlag('felhasználás', fel1, fel2)
átlag('kapacitás', kap1, kap2)

határ = float(input('Adjon meg egy határértéket! '))

print('Az alábbi országokban volt az egy főre jutó felhasználás 15 hektár fölötti:')

for i in range(len(kód)):
    if round(felhasználás[i] / lakosság[i], 3) > határ:
        print(f'{ország[i]} - {év[i]}: {round(felhasználás[i] / lakosság[i], 3)} hektár')

print(f'Az adatok {len(set(ország))} ország adatait tartalmazzák.')

max_fel = [0]
for i in range(len(kód) - 1):
    if ország[i] == ország[i + 1]:
        max_fel.append(felhasználás[i + 1] - felhasználás[i])
    else:
        max_fel.append(0)
x = max(max_fel)
x_ind = max_fel.index(x)
print(f'A legnagyobb növekedés a felhasználás értékében {ország[x_ind]}-ban/ben {év[x_ind]}-ban/ben történt:')
print(f'{int(round(felhasználás[x_ind - 1])):,} => {int(round(felhasználás[x_ind])):,}.')

for i in range(len(kód) - 1):
    if ország[i] == ország[i + 1]:
        if felhasználás[i] > felhasználás[i + 1]:
            print(f'{ország[i]} felhasználása csökkent {év[i]} évről {év[i + 1]} évre.')
            break
else:
    print('Nincsen olyan ország, akinek csökkent a felhasználása.')

print('A legnagyobb felhasználók:')

fel_átlag = []
országok = list(set(ország))
országok.sort()

for i in range(len(országok)):
    adatsor = []
    for e in range(ország.count(országok[i])):
        adatsor.append(felhasználás_alt[0] / lakosság_alt[0])
        felhasználás_alt.pop(0)
        lakosság_alt.pop(0)
    fel_átlag.append(sum(adatsor) / len(adatsor))

országok_top10 = []

for i in range(10):
    országok_top10.append(országok[fel_átlag.index(max(fel_átlag))])
    fel_átlag.remove(max(fel_átlag))

országok_top10.sort()

print(f'{", ".join(országok_top10)}')