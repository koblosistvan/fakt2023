forras = open('utonevek.txt', mode='r', encoding='utf-8')

keresztnevek = []

for sor in forras:
    adat = sor.strip()
    keresztnevek.append(adat)

hangrend = ''

magas = 'eéiíöőüű'
mely = 'aáuúoó'

magas_e = False
mely_e = False

def hangrend(nev):
    for c in nev:
        if c in magas:
            magas_e = True
        if c in mely:
            mely_e = True

    if magas_e == True and mely_e == False:
            hangrend = 'magas'
    elif magas_e == False and mely_e == True:
            hangrend = 'mely'
    else:
        hangrend = 'vegyes'

    return hangrend

vezeteknev = input('Add meg a vezetékneved! ')

lehetseges = []

for i in range(len(keresztnevek)):
    if len(vezeteknev) + len(keresztnevek[i]) >= 15:
        lehetseges.append(keresztnevek[i])

print(lehetseges)


lehet = []

for i in range(len(keresztnevek)):
    if hangrend(vezeteknev[i]) == hangrend(keresztnevek[i]):
        lehet.append(keresztnevek[i])

print(lehet)