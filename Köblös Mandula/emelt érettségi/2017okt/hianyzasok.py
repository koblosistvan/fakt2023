IGAZOLT = 'X'
IGAZOLATLAN = 'I'
JELEN = '0'
NINCS_ORAJA = 'N'

forras = open('naplo-2.txt', mode='r', encoding='utf-8')

honap = []
nap = []
nev = []
hianyzas = []

ho_s = 0
nap_s = 0
for sor in forras:
    adat = sor.strip().split(' ')
    if adat[0] == '#':
        ho_s = int(adat[1])
        nap_s = int(adat[2])
    else:
        honap.append(ho_s)
        nap.append(nap_s)
        nev.append(f'{adat[0]} {adat[1]}')
        hianyzas.append(adat[2])

forras.close()

print(honap)
print(nap)
print(nev)
print(hianyzas)

hossz = len(honap)

print('2. feladat')
print(f'A naplóban {hossz} bejegyzés van.')

print('\n3. feladat')
igazolt = 0
igazolatlan = 0

for i in range(hossz):
    for j in range(len(hianyzas[i])):
        if hianyzas[i][j] == IGAZOLT:
            igazolt += 1
        elif hianyzas[i][j] == IGAZOLATLAN:
            igazolatlan += 1

print(f'Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.')

def hetnapja(honap, nap):
    napnev = ['vasárnap', 'hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1]+nap) % 7
    return napnev[napsorszam]

print('\n5. feladat')
honap_be = int(input('A hónap sorszáma='))
nap_be = int(input('A nap sorszáma='))
print(f'Azon a napon {hetnapja(honap_be, nap_be)} volt.')

print('\n6.feladat')
nap_be2 = input('A nap neve=')
ora_be = int(input('Az óra sorszáma='))
hiany = ['X', 'I']
hianyzas_szamlalo = 0

for i in range(hossz):
    if hetnapja(honap[i], nap[i]) == nap_be2 and hianyzas[i][ora_be-1] in hiany:
        hianyzas_szamlalo += 1

print(f'Ekkor összesen {hianyzas_szamlalo} óra hiányzás történt.')

print('\n7. feladat')
nevek_abc = sorted(set(nev.copy()))
osszes_hianyzas = []

for i in range(len(nevek_abc)):
    osszes_hiany = 0
    for j in range(hossz):
        if nevek_abc[i] == nev[j]:
            osszes_hiany += hianyzas[j].count('I')
            osszes_hiany += hianyzas[j].count('X')
    osszes_hianyzas.append(osszes_hiany)

print('A legtöbbet hiányzó tanulók:', end=' ')
for i in range(len(nevek_abc)):
    if osszes_hianyzas[i] == max(osszes_hianyzas):
        print(f'{nevek_abc[i]}', end=' ')