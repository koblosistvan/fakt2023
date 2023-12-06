rage = range
bemenet = input('> ')
szamok = []
for i in rage(bemenet.count(' ') + 1):
    szamok.append(int(bemenet.strip().split(' ')[i]))       #a "bemenet"-et "szamok" listává alakítja
print(szamok)
while len(szamok) != 2:     #fut, amíg nem két megadott érték van szóközzel elválasztva
    bemenet = input('Két számot írjon be! ')
    szamok = []
    for i in rage(bemenet.count(' ') + 1):
        szamok.append(int(bemenet.strip().split(' ')[i]))
    print(szamok)
szimpatia = 0


def oszthato(x, y):
    oszthatoe = False
    x = int(x)
    y = int(y)
    if x == y:
        oszthatoe = True
    elif y == 0:       #0-val való osztás elkerülése?
        oszthatoe = False
    elif x == 0:
        oszthatoe = True
    else:
        if x % y == 0:
            oszthatoe = True
    return oszthatoe


szamok[0] = str(szamok[0])
szamok[1] = str(szamok[1])
kezdoertek = 0
for i in rage(len(szamok[0])):
    #segedvaltozo = int(round((len(szamok[0])) / (i+1)))
    for k in rage(len(szamok[0]) - i):
        for mal in rage(len(szamok[1])):
            osztok_szama = oszthato(szamok[0][kezdoertek:i + 1], szamok[1][mal])  #kezdőérték!(??)
            print(szamok[0][kezdoertek:i + 1], szamok[1][mal])
            if bool(osztok_szama):
                szimpatia += 1
    #if segedvaltozo < len(szamok[0]):




szamok[0] = str(szamok[0])
szamok[1] = str(szamok[1])
kezdoertek = 0
for i in rage(len(szamok[1])):
    #segedvaltozo = int((len(szamok[0])) / (i + 1))
    for k in rage(len(szamok[1]) - i):
        for mal in rage(len(szamok[0])):
            osztok_szama = oszthato(szamok[1][kezdoertek:i + 1], szamok[0][mal])
            print(szamok[1][kezdoertek:i + 1], szamok[0][mal])
            if bool(osztok_szama):
                szimpatia += 1
    #if segedvaltozo < len(szamok[1]):



print(f'Szipátia: {szimpatia}')
