import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, 'hu_HU')

forras = open('6a-hallgatok.txt', mode='r')
szulnap = []
kezd = []
veg = []
hallgatok = int(forras.readline())
for i in forras:
    sor = i.strip().split(' ')
    szuldatum = dt.date(int(sor[0]), int(sor[1]), int(sor[2]))
    szulnap.append(szuldatum)
    kezd.append(int(sor[3]))
    veg.append(int(sor[4]))
forras.close()

bekert = int(input('Adjon meg egy életkor értéket: '))
for i in range(hallgatok):
    if bekert > veg[i] - szulnap[i].year:
        print('Van olyan hallgató, aki ennél fiatalabban szerzett diplomát.')
        break
else:
    print('Nincs olyan hallgató, aki ennél fiatalabban szerzett diplomát.')

for i in range(hallgatok):
    if szulnap[i].month == 9 and szulnap[i].day == 24:
        print('Van olyan hallgató, akivel egy napon van a születésnapunk.')
        break
else:
    print('Nincs olyan hallgató, akivel egy napon van a születésnapunk.')

ev = szulnap[0].year
for i in range(hallgatok-1):
    if veg[i+1] - szulnap[i+1].year < veg[i] - szulnap[i].year:
        ev = szulnap[i+1].year
print(f'{ev}-ban/ben született a legfiatalabb diplomás.')

print(f'{veg.count(2016)} tanuló végzett 2016-ban.')

kor = 0
z = 0
for i in range(hallgatok):
    if kezd[i] <= 2014 <= veg[i]:
        if szulnap[i].month in (1, 2):
            kor += (2014 - (szulnap[i].year - 1))
            z += 1
        else:
            kor += (2014 - szulnap[i].year)
            z += 1
print(f'2014 tavaszán az egyetem átlagéletkor {int(round((kor / z), 0))} év.')