fajl = open('utonevek.txt', mode='r', encoding='utf-8')

utonevek = []

magas = 'eéiíöőüű'
mely = 'aáoóuú'




def hangrend(vezeteknev):
    szaml_magas = 0
    szaml_mely = 0
    hangrend = ''
    for a in vezeteknev:
        if a in magas:
            szaml_magas += 1
        if a in mely:
            szaml_mely += 1
    if szaml_mely > 0 and szaml_magas > 0:
        hangrend = 'vegyes'
    elif szaml_magas > 0 and szaml_mely == 0:
        hangrend = 'magas'
    elif szaml_mely > 0 and szaml_magas == 0:
        hangrend = 'mely'
    return hangrend

for i in fajl:
    adat = i.strip()
    utonevek.append(adat)

print(utonevek)

vezeteknev = input('add meg a vezeteknevet:')

lehetnek = []

for i in range(len(utonevek)):
    if hangrend(vezeteknev) == hangrend(utonevek[i]):
        lehetnek.append(utonevek[i])

print(lehetnek)








