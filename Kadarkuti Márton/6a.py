import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, 'hu_HU')
def vonal():
    print("-"*30)

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
l = len(vegzesek)
vonal()

#+1 feladat
bekertnelFiatalabb = False
bekert = int(input("Adj meg egy életkort: "))

for i in range(l):
    if bekert < vegzesek[i] - szuletes[i].year:
        bekertnelFiatalabb = True
        break
if bekertnelFiatalabb:
    print(f"Van olyan hallgató, aki {bekert} éves.")
else:
    print(f"Nincs olyan hallgató, aki {bekert} éves.")
vonal()

#2+ feladat
szulinap = str(input("Add meg a születésnapod, szóközzel elválasztva: > ")) # formátum: "yyyy mm dd"
#print(szulinap)
szulinap = szulinap.strip().split(" ")
#print(szulinap)
szulinap = dt.datetime(int(szulinap[0]), int(szulinap[1]), int(szulinap[2]))
#print(szulinap)
vanAzonosSzulinap = False

for i in range(l):
    if szulinap == szuletes[i]:
        vanAzonosSzulinap = True
        break
if vanAzonosSzulinap:
    print("<Van> olyan ember a listán, aki ugyanezen a napon született.")
else:
    print("<Nincs> olyan ember a listán, aki ugyanezen a napon született.")
vonal()

#3+ feladat
legfiatalabb = [100, 0]   # életkort és indexet ment el
for i in range(l):
    if vegzesek[i] - szuletes[i].year < legfiatalabb[0]:
        legfiatalabb[0] = vegzesek[i] - szuletes[i].year
        legfiatalabb[1] = i

nyelvhelyesseg = ""   # kijavítani azt a hibát, hogy pl. "16-én" vagy "12-án"
if szuletes[legfiatalabb[1]].day in (1,4,5,7,9,10,11,12,14,15,17,19,21,22,24,25,27,29,31):
    nyelvhelyesseg = "-én"
else:
    nyelvhelyesseg = "-án"
print(f"Az a hallgató, aki a legfiatalabban végzett {szuletes[legfiatalabb[1]].strftime('%Y.%m.%d')}.{nyelvhelyesseg} született.")

vonal()

#+4 feladat
hallgatok_2016 = 0
for i in range(l):
    if vegzesek[i] == 2016:
        hallgatok_2016 += 1
print(f"{hallgatok_2016} hallgató végzett 2016-ban.")
vonal()

#+5 feladat
eletkor_2014_atlag = 0
s = 0  #az átlag kiszámolásához kell osztónak
for i in range(l):
    if vegzesek[i] >= 2014:
        eletkor_2014_atlag += 2014 - szuletes[i].year
        s += 1

eletkor_2014_atlag /= s
print(f"A hallgatók átlagéletkora 2014-ben {int(eletkor_2014_atlag)} év.")

vonal()
