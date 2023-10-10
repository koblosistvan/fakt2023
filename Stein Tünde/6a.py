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
bekert_evszam = int(input('Adj meg egy évszám: '))
bekert_datum = input('Add meg a születési dátumodat: ')
bekert_datum.strip().split('. ')
int(bekert_datum)
print(bekert_datum)
for i in range(len(vegzesek)):
    if bekert_evszam < vegzesek[i]:
        print('Van olyan hallgató, aki ennél fiatalabban szerzett diplomát.')
    else:
        print('Nincs olyan hallgató, aki ennél fiatalabban szerzett diplomát.')