forras = open('rendel.txt', mode='r', encoding='utf-8')

nap = []
varos = []
darab = []

for sor in forras:
    adat = sor.strip().split(' ')
    nap.append(int(adat[0]))
    varos.append(adat[1])
    darab.append(int(adat[2]))

forras.close()

def osszes(varos_betu, nap_szam):
    rendelesek = 0
    for i in range(len(varos)):
        if varos_betu ==  varos[i] and nap_szam == nap[i]:
            rendelesek += darab[i]
    return rendelesek



print('2. feladat')
print(f'A rendelések száma: {len(nap)}')

print('3. feladat')
nap_szama = int(input('Melyik nap adatait szeretnéd?(szám) '))
szamlalo = 0
for i in range(len(nap)):
    if nap[i] == nap_szama:
        szamlalo += darab[i]
print(f'A rendelések száma az adott napon: {szamlalo}')


print('4. feladat')
nem_volt =  []
volt = [nap[i] for i in range(len(nap)) if varos[i] == 'NR']
for dátum in range(1, 31):
    if dátum not in volt:
        nem_volt.append(dátum)
print(f'{len(nem_volt)} nap nem volt rendelés.')

print('5. feladat')
legnagyobb = darab[0]
index_legn = 0
for i in range(len(darab)):
    if darab[i] > legnagyobb:
        legnagyobb = darab[i]
for i in range(len(darab)):
    if darab[i] == legnagyobb:
        index_legn = i
        break
print(f'A legnagyobb darabszám: {legnagyobb}, a rendelés napja: {nap[index_legn]}')

print('7.feladat')
print(f'A rendelt termékek száma a 21. napon: PL: {osszes("PL",21)} TV: {osszes("TV", 21)} NR: {osszes("NR", 21)}')

print('8. feladat')
nap_szam = 1
