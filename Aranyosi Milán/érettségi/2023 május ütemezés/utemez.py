forras = open('taborok.txt', mode='r', encoding='utf-8')

honaptol = []
naptol = []
honapig = []
napig = []
azon = []
tabor = []
for sor in forras:
    adat = sor.strip().split('\t')
    honaptol.append(int(adat[0]))
    naptol.append(int(adat[1]))
    honapig.append(int(adat[2]))
    napig.append(int(adat[3]))
    azon.append(adat[4])
    tabor.append(adat[5])
forras.close()

print('2.feladat')
print(f'Az adatsorok száma: {len(tabor)}')
print(f'Az először rögzített tábor témája: {tabor[0]}')
print(f'Az utoljára rögzített tábor témája: {tabor[-1]}')

print('3. feladat')
szaml = 0
for i in range(len(tabor)):
    if tabor[i] == 'zenei':
        print(f'Zenei tábor kezdődik {honaptol[i]}. hó {naptol[i]}. napján.')
        szaml += 1
if szaml == 0:
    print('Nem volt zenei tabor.')


print('4. feladat')
print('Legnépszerűbbek:')
legnepszerubb = len(azon[0])
for i in range(len(azon)):
    if len(azon[i]) > legnepszerubb:
        legnepszerubb = len(azon[i])
for i in range(len(azon)):
    if len(azon[i]) == legnepszerubb:
        print(f'{honaptol[i]} {naptol[i]} {tabor[i]}')

def sorszam(honap, nap):
    if honap == 6:
        hanyadik = nap-15
    elif honap == 7:
        hanyadik = 30-15+nap
    elif honap == 8:
        hanyadik = 30-15+31+nap
    return hanyadik


print('6. feladat')
adott_honap = int(input('hónap:'))
adott_nap = int(input('nap:'))
tabor_zajlik = []
for i in range(len(tabor)):
    if sorszam(honaptol[i], naptol[i]) <= sorszam(adott_honap, adott_nap) <= sorszam(honapig[i], napig[i]):
        tabor_zajlik.append(i)
print(f'Ekkor éppen {len(tabor_zajlik)} tábor tart.')

print('7. feladat')

betujel = input('Adja meg egy tanuló betűjelét:')
kimenet = open('egytanulo.txt', mode='w', encoding='utf-8')


kimenet.close()
'Nem mehet el mindegyik táborba.'