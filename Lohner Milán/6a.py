import datetime as dt

forras = open('6a-hallgatok.txt', mode='r', encoding='utf-8')

szuletesnapok = []
kezdesek = []
vegzesek = []
eletkorok = []


for sor in forras:
    adat = sor.strip().split(' ')
    if len(adat) == 5:
        szul_datum = dt.datetime(int(adat[0]), int(adat[1]), int(adat[2]))
        kezdes = int(adat[3])
        vegzes = int(adat[4])
        szuletesnapok.append(szul_datum)
        kezdesek.append(kezdes)
        vegzesek.append(vegzes)
        # Az életkor számítása
        eletkor = vegzes - szul_datum.year
        eletkorok.append(eletkor)


eletkor = int(input("Kérem, adja meg az életkorát: "))
fiatalabbak_vannak = any(eletkor > kor for kor in eletkorok)
if fiatalabbak_vannak:
    print("Igen, van olyan hallgató, aki ennél fiatalabban szerzett diplomát.")
else:
    print("Nincs olyan hallgató, aki ennél fiatalabban szerzett diplomát.")


