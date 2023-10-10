import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, 'hu_HU')

forras = open('6a-hallgatok.txt', mode='r', encoding='utf-8')
szuletes = []
kezdesek = []
vegzesek = []

forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    szuletesi_datum = dt.datetime(int(adat[0]), int(adat[1]), int(adat[2]))
    szuletes.append(szuletesi_datum)
    kezdesek.append(int(adat[3]))
    vegzesek.append(int(adat[4]))
forras.close()

# 1. feladat
bekert_eletkor = int(input('Adj meg egy életkort: '))
_1 = 'Van'
for i in range(len(vegzesek)):
    if bekert_eletkor > vegzesek[i] - szuletes[i].year:
        _1 = 'Van'
        break
print(f'{_1} olyan hallgató, aki ennél fiatalabban szerzett diplomát.')

#2. feladat
bekert_datum = input('Add meg a születési dátumodat: ')
bekert_datum = bekert_datum.strip().split(' ')
bekert_datum = dt.datetime(int(bekert_datum[0]), int(bekert_datum[1]), int(bekert_datum[2]))
_2 = 'Nincs'
for i in range(len(szuletes)):
    if szuletes[i].month == bekert_datum.month and szuletes[i].day == bekert_datum.day:
        _2 = 'Van'
print(f'{_2} olyan hallgató, akinek ugyanazon a napon van a születésnapja mint neked.')

#3. feladat
legfiatalabb = 100
for i in range(len(szuletes)):
    if vegzesek[i] - szuletes[i].year < legfiatalabb:
        legfiatalabb = vegzesek[i] - szuletes[i].year
        i_ertek = i
print(f'A legfiatalabb diplomázó {szuletes[i_ertek].year}-ban született, és {vegzesek[i_ertek]}-ben diplomázott.')

#4. feladat
vegzett_16ban = 0
for i in range(len(vegzesek)):
    if vegzesek[i] == 2016:
        vegzett_16ban += 1
print(f'{vegzett_16ban} hallgató végzett 2016-ban.')

#5. feladat
eletkorok_osszege_2014 = 0
nevezo = 0
for i in range(len(szuletes)):
    if vegzesek[i] > 2014 >= kezdesek[i]:
        if szuletes[i].month in (1, 2):
            eletkorok_osszege_2014 += (2014 - (szuletes[i].year - 1))
            nevezo += 1
        elif szuletes[i].month > 2:
            eletkorok_osszege_2014 += (2014 - szuletes[i].year)
            nevezo += 1
print(f'Az hallgatók átlagéletkora 2014 tavaszán {eletkorok_osszege_2014 / nevezo}.')
