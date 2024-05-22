import math
forrás = open('Bogdán_Samu\starcraft\starcraft.txt', 'r', encoding='UTF-8')
forrás.readline()
egység = []
faj = []
pajzs = []
hp = []
földi = []
légi = []
for i in forrás:
    sor = i.strip().split('\t')
    egység.append(sor[0])
    faj.append(sor[1])
    pajzs.append(int(sor[2]))
    hp.append(int(sor[3]))
    földi.append(int(sor[4]))
    légi.append(int(sor[5]))
forrás.close()

print('\n'+'1. feladat')
print(f'Az állomány {len(egység)} egység adatait tartalmazza.')

print('\n'+'2. feladat')
id = hp.index(max(hp))
print(f'A legerősebb egységnek {hp[id]} HP-ja van. Ez a {faj[id]} faj {egység[id]} egysége.')

print('\n'+'3. feladat')
x = 0
for i in range(len(egység)):
    if faj[i] == 'Protoss' and földi[i] > 0:
        x += 1
print(f'{x} Protoss egység tud földi célpontot támadni.')

print('\n'+'4. feladat')
támadók = open('Bogdán_Samu\starcraft\starcraft-támadók.txt', 'w', encoding='UTF-8')
for i in range(len(egység)):
    if földi[i] > 0 and légi[i] > 0:
        támadók.write(f'Egység: {egység[i]}, faj: {faj[i]}, pajzs: {pajzs[i]}, hp: {hp[i]}, föld ellen: {földi[i]}, levegő ellen: {légi[i]}.'+'\n')
támadók.close()
print('Nyissa meg a "starcraft-támadók.txt" nevű fájlt!')

print('\n'+'5. feladat')
for i in range(len(egység)):
    if faj[i] == 'Zerg' and (földi[i] > 100 or légi[i] > 100):
        print('Van 100-nál többet sebző Zerg egység.')
        break
else:
    print('Nincs 100-nál többet sebző Zerg egység.')

print('\n'+'6. feladat')
terran = []
for i in range(len(egység)):
    if faj[i] == 'Terran':
        terran.append(hp[i])
átlag = sum(terran) / len(terran)
print(f'A Terran egységek átlagos HP-ja {round(átlag)}.')

print('\n'+'7. feladat')
id1 = egység.index('Goliath')
id2 = egység.index('Hydralisk')
gh = math.ceil(hp[id2]/földi[id1])
hg = math.ceil(hp[id1]/földi[id2])
if gh < hg:
    print('A Goliath nyerne.')
elif hg < gh:
    print('A Hydralisk nyerne.')
else:
    print('Döntetlen lenne.')
print('\n')
