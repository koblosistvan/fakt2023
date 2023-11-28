import cuccok
import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, 'hu_HU')

forras = open('6a-hallgatok.txt', mode='r', encoding='utf-8')
szuletesnapok = []
kezdesek = []
vegzesek = []
sorok = 0
forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    szuldatum = dt.datetime(int(adat[0]), int(adat[1]), int(adat[2]))
    szuletesnapok.append(szuldatum)
    kezdesek.append(int(adat[3]))
    vegzesek.append(int(adat[4]))
    sorok += 1

bekert = int(input(':'))
van = False
for i in range(len(kezdesek)):
    if bekert > (vegzesek[i] - szuletesnapok[i].year):
       van = True
if van == True:
    print('van olyan ember aki ennél fiatalabban tette volna le')
else:
    print('nincs olyan ember aki ennél fiatalabban tette volna le')

szülinapom = dt.datetime(2006, 12, 18)
szülinapomlista = []
szülinapomlista.append(szülinapom)
vanszulinap = True
for i in range(sorok):
    if szülinapomlista == szuletesnapok[i]:
        print('van olyan hallgató aki 2006.12.18-an született')
else:
    print('nincs olyan hallgató aki 2006.12.18-an született')
évesenvégzett = 999999
for i in range(sorok):
    if (vegzesek[i] - szuletesnapok[i].year) < évesenvégzett:
        évesenvégzett = vegzesek[i] - szuletesnapok[i].year
        mikorszuletett = szuletesnapok[i]
print(f'A legfiatalabban végzett ember {mikorszuletett.year, mikorszuletett.month, mikorszuletett.day} születet')

tizenhat = 0
for i in range(len(vegzesek)):
    if vegzesek[i] == 2016:
        tizenhat += 1
print(f'{tizenhat} ember végzett 2016ban')

eletkorossz = 0
tizennegybe = 0
for i in range(len(vegzesek)):
    if vegzesek[i] >= 2014:
        eletkorossz += 2014 - szuletesnapok[i].year
        tizennegybe += 1
atlag = eletkorossz / tizennegybe
print(f'2014-ben {int(atlag)} volt az átlag életkor.')