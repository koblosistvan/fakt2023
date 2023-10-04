import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, "hu_HU")


forrás = open("6a-hallgatok.txt", mode="r", encoding="utf-8")

szülnapok = []
kezdés = []
bef = []

forrás.readline()
for sor in forrás:
    adat = sor.strip().split(" ")
    szül_dátum = dt.datetime(int(adat[0]), int(adat[1]), int(adat[2]))
    szülnapok.append(szül_dátum)
    kezdés.append(int(adat[3]))
    bef.append(int(adat[4]))














