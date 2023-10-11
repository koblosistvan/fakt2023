import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, 'hu_HU')

forrás = open('6a-hallgatok.txt', mode='r', encoding='utf-8')
születésnapok = []
kezdések = []
végzések = []

forrás.readline()
for sor in forrás:
    adat = sor.strip().split(' ')
    szül_dátum = dt.datetime(int(adat[0]), int(adat[1]), int(adat[2]))
    születésnapok.append(szül_dátum)
    kezdések.append(int(adat[3]))
    végzések.append(int(adat[4]))

# A diplomaosztó minden évben június 20-án van. Döntsd el, hogy van-e olyan hallgató, aki adott életkor
# előtt szerzett diplomát! (eldöntés)
diplomaosztók = []
kor = int(input('Adj meg egy életkort: '))
for i in range(len(születésnapok)):
    szülinap = dt.datetime(születésnapok[i].year + kor, születésnapok[i].month, születésnapok[i].day)
    diplomaosztó = dt.datetime(végzések[i], 6, 20)
    diplomaosztók.append(diplomaosztó)
    if szülinap > diplomaosztó:
        print(f'Van olyan hallgató, aki {kor} éves kora előtt szerzett diplomát.')
        break
else:
    print(f'Nincs olyan hallgató, aki {kor} éves kora előtt szerzett diplomát.')
