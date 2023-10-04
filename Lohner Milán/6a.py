forras = open('6a-hallgatok.txt', mode='r', encoding='utf-8')

import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, 'hu_HU')

szuletesnapok = []
kezdesek = []
vegzesek = []

forras.readline

for sor in forras:
    adat = sor.strip().split(' ')
    szul_datum = dt.datetime(int(adat[0])), (int(adat[1])), (int(adat[2]))
    szuletesnapok.append(szul_datum)


