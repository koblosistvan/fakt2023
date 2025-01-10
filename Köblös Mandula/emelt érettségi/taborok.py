forras = open('taborok.txt', mode='r', encoding='utf-8')

honap_kezdes = []
nap_kezdes = []
honap_vege = []
nap_vege = []
diakok = []
tema = []

for sor in forras:
    adat = sor.strip().split('\t')
    honap_kezdes.append(int(adat[0]))
    nap_kezdes.append(adat[1])
    honap_vege.append(adat[2])
    nap_vege.append(adat[3])
    diakok.append(adat[4])
    tema.append(adat[5])

forras.close()

def sorszam(honap, nap):
    if honap == 6:
        hanyadik = nap-15
    elif honap == 7:
        hanyadik = 30-15+nap
    else:
        hanyadik = 30-15+31+nap
    return hanyadik

print('2.feladat')
print(len(tema))
print(f'első tábor témája: {tema[0]} \nutolsó tábor témája: {tema[-1]}')

print('3.feladat')
zenei = 0
for i in range(len(tema)):
    if tema[i] == 'zenei':
        print(f'Zenei tábor kezdődik {honap_kezdes[i]}. hónap {nap_kezdes[i]}. napján')
        zenei += 1
if zenei == 0:
    print('Nem volt zenei tábor')

print('4. feladat')
legnepszerubb = len(diakok[0])
legnepszerubb_id = 0
for i in range(len(diakok)):
    if len(diakok[i]) > legnepszerubb:
        legnepszerubb = len(diakok[i])
        legnepszerubb_id = i
print(honap_kezdes[legnepszerubb_id], nap_kezdes[legnepszerubb_id], legnepszerubb)

ho = int(input('hónap: '))
nap = int(input('nap: '))

taborok = 0
for i in range(len(honap_kezdes)):
    if sorszam(honap_kezdes[i], nap_kezdes[i]) <= sorszam(ho, nap) <= sorszam(honap_vege[i], nap_vege[i]):
        taborok += 1
print(f'{taborok} tábor volt ekkor')