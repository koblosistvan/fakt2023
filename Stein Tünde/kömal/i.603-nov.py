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
    oszthatoe = False
    x = int(x)
    y = int(y)
    if x == 0 and y != 0:       #0-val való osztás elkerülése: sok
        oszthatoe = True
    elif y == 0:
        oszthatoe = True
    elif x and y == 0:
        oszthatoe = False
    elif x % y == 0 or y % x == 0:
        oszthatoe = True
    return oszthatoe

for i in rage(2):       #kétszer futtatja, mert eddigre már csak két megadott érték lehet
    szamok[0] = str(szamok[0])
    if len(szamok[0]) == 1:
        x = oszthato(szamok[0], szamok[1])
        if bool(x):
            szimpatia += 1
    else:
        for k in rage(len(szamok[0])):
            x = oszthato(int(szamok[0][k]), int(szamok[1]))
            if bool(x):
                szimpatia += 1
    szamok[1] = str(szamok[1])
    if len(szamok[1]) == 1:
        x = oszthato(szamok[1], szamok[0])
        if bool(x):
            szimpatia += 1
    else:
        for k in rage(len(szamok[1])):
            x = oszthato(szamok[1][k], szamok[0])
            if bool(x):
                szimpatia += 1

print(szimpatia)
