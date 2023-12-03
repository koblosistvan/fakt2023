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

def oszthato(x, y):     #egy bool-t ad vissza, aszerint hogy x és y osztható-e egymással
    oszthatoe = 0
    x = int(x)
    y = int(y)
    if (x == 0 and y != 0) or (x != 0 and y == 0):       #0-val való osztás elkerülése: sok
        oszthatoe += 1
    elif x and y == 0:
        oszthatoe += 0
    else:
        if x % y == 0:
            oszthatoe += 1
        if y % x == 0:
            oszthatoe += 1
    return oszthatoe


szamok[0] = str(szamok[0])
szamok[1] = str(szamok[1])
if len(szamok[0]) == 1:     #ha az első szám egyjegyű
    if len(szamok[1]) != 1:     #csak egyjegyű számokkal szorzok
        for a in rage(len(szamok[1])):
            osztok_szama = oszthato(szamok[0], szamok[1][a])       #egymással osztva az osztók száma
            szimpatia += osztok_szama
    else:
        osztok_szama = oszthato(szamok[0], szamok[1])       #egymással osztva az osztók száma
        szimpatia += osztok_szama

else:
    for i in rage(len(szamok[0])):
        segedvaltozo = int(len(szamok[0]) / (i+1)) #segedvaltozo = hányszor van meg a számjegyek számában a futtatás sorszáma
        for k in rage(segedvaltozo):
            if len(szamok[1]) != 1:
                for a in rage(len(szamok[1])):
                    osztok_szama = oszthato(szamok[0][:segedvaltozo + 1], szamok[1][a])
                    szimpatia += osztok_szama
            else:
                osztok_szama = oszthato(szamok[0][:segedvaltozo + 1], szamok[1])
                szimpatia += osztok_szama


#szamok[0] = str(szamok[0])
#szamok[1] = str(szamok[1])
#if len(szamok[1]) == 1:     #ha a második szám egyjegyű
#    if len(szamok[0]) != 1:
#        for a in rage(len(szamok[0])):
#            osztok_szama = oszthato(szamok[1], szamok[0][a])
#            szimpatia += osztok_szama
#    else:
#        osztok_szama = oszthato(szamok[1], szamok[0])
#        szimpatia += osztok_szama

#else:
#    for i in rage(len(szamok[1])-1):
#        segedvaltozo = int(len(szamok[1]) / (i+1)) #segedvaltozo = hányszor van meg a számjegyek számában a futtatás sorszáma
#        for k in rage(segedvaltozo):
#            if len(szamok[0]) != 1:
#                for a in rage(len(szamok[0])):
#                    osztok_szama = oszthato(szamok[1][:segedvaltozo + 1], szamok[0][a])
#                    szimpatia += osztok_szama
#            else:
#                osztok_szama = oszthato(szamok[0][:segedvaltozo + 1], szamok[0])
#                szimpatia += osztok_szama


print(szimpatia)
