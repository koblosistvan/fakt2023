bemenet = input('> ')
kezdoertek = int(bemenet.strip().split(' ')[0])
zaroertek = int(bemenet.strip().split(' ')[1])
tartomany = []
ertek = kezdoertek
kozepesek = 0
for i in range(zaroertek-kezdoertek+1):
    tartomany.append(ertek)
    ertek += 1


def kozepes_szam(x):
    kozepese = False
    x_osszeg = 0
    if x == 0:
        kozepese = False
    else:
        for mal in (str(x)):
            x_osszeg += int(mal)
            szamtani_kozep = x_osszeg / len(str(x))
        if szamtani_kozep % 1 == 0:
            if x % szamtani_kozep == 0:
                kozepese = True
    return kozepese


for i in range(len(tartomany)):
    segedvaltozo = kozepes_szam(tartomany[i])
    if bool(segedvaltozo):
        kozepesek += 1
print(kozepesek)
