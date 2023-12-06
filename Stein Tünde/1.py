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
        szamok.append(int(bemenet.strip().split(' ')[i]))       #a "bemenet"-et "szamok" listává alakítja
    print(szamok)
szimpatia = 0

def oszthato(x, y):
    oszthatoe = 0
    x = int(x)
    y = int(y)
    if y == 0:       #0-val való osztás elkerülése: sok
        oszthatoe += 0
    elif x == 0:
        oszthatoe += 1
    else:
        if x % y == 0:
            oszthatoe += 1
    return oszthatoe


szamok[0] = str(szamok[0])
szamok[1] = str(szamok[1])
if len(szamok[0]) == 1:     #ha az első szám egyjegyű
    if len(szamok[1]) == 1:
        osztok_szama = oszthato(szamok[0], szamok[1])       #egymással osztva az osztók száma
        szimpatia += osztok_szama

else:
    for i in rage(len(szamok[0])):
        segedvaltozo = int(len(szamok[0]) / (i+1)) #segedvaltozo = hányszor van meg a számjegyek számában a futtatás sorszáma
        for k in rage(segedvaltozo):
            if len(szamok[1]) == 1:
                osztok_szama = oszthato(szamok[0][:segedvaltozo + 1], szamok[1])
                szimpatia += osztok_szama


szamok[0] = str(szamok[0])
szamok[1] = str(szamok[1])
if len(szamok[1]) == 1:     #ha az első szám egyjegyű
    if len(szamok[0]) == 1:
        osztok_szama = oszthato(szamok[0], szamok[1])       #egymással osztva az osztók száma
        szimpatia += osztok_szama

else:
    for i in rage(len(szamok[1])):
        segedvaltozo = int(len(szamok[1]) / (i+1)) #segedvaltozo = hányszor van meg a számjegyek számában a futtatás sorszáma
        for k in rage(segedvaltozo):
            if len(szamok[0]) == 1:
                osztok_szama = oszthato(szamok[1][:segedvaltozo + 1], szamok[0])
                szimpatia += osztok_szama



print(szimpatia)
