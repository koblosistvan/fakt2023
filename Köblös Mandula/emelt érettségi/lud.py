forrás = open('dobasok.txt', mode='r', encoding='utf-8')
dobasok = []
for sor in forrás:
    adat = sor.strip().split(' ')
    dobasok.append(adat)


forrás.close()

forrás2 = open('osvenyek.txt', mode='r', encoding='utf-8')
osveny = []
for sor in forrás2:
    osveny.append(sor)

forrás2.close()

print('2. feladat')
szamlalo = 0
for i in dobasok:
    szamlalo += 1
print(f'A dobások száma: {szamlalo}')
print(f'Az ösvények száma: {len(osveny)}')