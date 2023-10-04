import datetime
import locale

forras = open('6a-hallgatok.txt', mode='r', encoding='utf-8')

forras.readline()
for i in forras:
    adat = i.strip().split(' ')
    szuldatum = dt.datetime(int(adat[0]), int(adat[1]), int(adat[2]))
