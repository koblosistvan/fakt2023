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


