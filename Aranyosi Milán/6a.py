import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, 'hu_HU')

forras = open('6a-hallgatok.txt', mode='r', encoding='utf-8')
szuletesnapok = []
kezdesek = []
vegzesek = []

forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    szul_datum = dt.datetime(int(adat[0]), int(adat[1]), int(adat[2]))
    szuletesnapok.append(szul_datum)
    kezdesek.append(int(adat[3]))
    vegzesek.append(int(adat[4]))

def vonal():
    print('-'*100)

#1. feladat
bekert_eletkor = int(input('Adj meg egy életkort:'))
amm = False
for i in range(len(vegzesek)):
    if bekert_eletkor > vegzesek[i] - szuletesnapok[i].year:
        amm = True
if amm == True:
    print('Van olyan hallgató aki ennél fiatalabban szerzett diplomát.')
else:
    print('Nincs olyan hallgató aki ennél fiatalabban szerzett volna diplomát.')
vonal()

#2. feladat
te_szulinapod = str(input('Add meg mikor van a szülinapod: ')).strip().split(' ')
te_szulinapod = dt.datetime(int(te_szulinapod[0]), int(te_szulinapod[1]), int(te_szulinapod[2]))

for i in range(len(szuletesnapok)):
    if te_szulinapod == szuletesnapok[i]:
        print('Van olyan hallgató aki veled egy napon született.')
else:
    print('Nincs olyan hallgató aki veled egy napon született.')
vonal()

#3. feladat
legfiatalabban_szerezte = vegzesek[0] - szuletesnapok[0].year
legfiatalabban_szerezte_bday = szuletesnapok[0]
for i in range(len(szuletesnapok)):
    if vegzesek[i] - szuletesnapok[i].year < legfiatalabban_szerezte:
        legfiatalabban_szerezte = vegzesek[i] - szuletesnapok[i].year
        legfiatalabban_szerezte_bday = szuletesnapok[i]
print(f"Az a hallgató aki a legfiatalabban szerezte meg a diplomáját {legfiatalabban_szerezte_bday.strftime('%Y.%m.%d')} napon született.")
vonal()

#4. feladat
vegzett_2016ban = 0
for i in range(len(vegzesek)):
    if vegzesek[i] == 2016:
        vegzett_2016ban += 1
print(f"{vegzett_2016ban} hallgató végzett 2016-ban.")
vonal()

#5. feladat
eletkorok_osszesen = 0
odajartak2014ben = 0
for i in range(len(vegzesek)):
    if vegzesek[i] >= 2014:
        eletkorok_osszesen += 2014 - szuletesnapok[i].year
        odajartak2014ben += 1
eletkor_2014_atlag = eletkorok_osszesen / odajartak2014ben
print(f'2014-ben {int(eletkor_2014_atlag)} volt az átlag életkor.')
vonal()
