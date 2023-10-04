import cuccok
import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, 'hu_HU')

forras = cuccok.megnyit('6a-hallgatok.txt')
szuletesnapok = []
kezdesek = []
vegzesek = []

forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    szuldatum = dt.datatime(int(adat[0]), int(adat[1]), int(adat[2]))
    szuletesnapok.append(szuldatum)
    kezdesek.append(int(adat[3]))
    vegzesek.append(int(adat[4]))

