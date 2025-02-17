forras = open('melyseg.txt', mode='r', encoding='utf-8')

melysegek = []
for sor in forras:
    melysegek.append(int(sor.strip()))

forras.close()
print('1. feladat')
print(f'A fájl adatainak száma: {len(melysegek)}')

print('\n2. feladat')
adott_tav = int(input('Adjon meg egy távolságértéket!'))
print(f'Ezen a helyen a felszín {melysegek[adott_tav-1]} méter mélyen van.')

print('\n3. feladat')

szamlalo_0 = melysegek.count(0)

print(f'Az érintetlen terület aránya {szamlalo_0/len(melysegek):0.2%}.')

kimenet = open('godrok.txt', mode='w', encoding='utf-8')

adott_godor = ''
adott_godor_lista = []
godrok = []

for i in range(len(melysegek)):
    if melysegek[i] != 0:
        adott_godor += f' {melysegek[i]}'
        adott_godor_lista.append(melysegek[i])
    elif melysegek[i-1] != 0 and melysegek[i] == 0:
        print(adott_godor, file=kimenet)
        godrok.append(adott_godor_lista)
        adott_godor_lista = []
        adott_godor = ''

kimenet.close()

print('\n5. feladat')
print(f'A gödrök száma: {len(godrok)}')

print('\n6. feladat')
if melysegek[adott_tav-1] == 0:
    print('Az adott helyen nincs gödör.')
else:
    kezdetek = []
    vegek = []

    for i in range(len(melysegek)):
        if melysegek[i-1] == 0 and melysegek[i] != 0:
            kezdetek.append(i+1)
        if melysegek[i-1] != 0 and melysegek[i] == 0:
            vegek.append(i)

    for i in range(len(kezdetek)):
        if kezdetek[i] <= adott_tav <= vegek[i]:
            print(f'a)\nA gödör kezdete: {kezdetek[i]} méter, a gödör vége: {vegek[i]} méter.')
            folyamatos = True
            legnagyobb = max(godrok[i])
            legnagyobb_index = godrok[i].index(max(godrok[i]))
            for j in range(kezdetek[i], legnagyobb_index-1):
                if melysegek[j] >= melysegek[j+1]:
                    folyamatos = True
                else:
                    folyamatos = False
                    break
            for e in range(legnagyobb_index, vegek[i]-1):
                if melysegek[i] >= melysegek[i+1]:
                    folyamatos = True
                else:
                    folyamatos = False
            if folyamatos ==  True:
                print('b)\nFolyamatsoan mélyül.')
            if folyamatos == False:
                print('b)\nNem mélyül folyamatosan.')
            print(f'c)\nA legnagyobb mélysége {legnagyobb} méter.')
            terfogat = 0
            for d in range(len(godrok[i])):
                terfogat += (10 * godrok[i][d])
            print(f'd)\nA térfogata {terfogat} m^3')
            print('e)')

'''
A vízmennyiség 280 m^3.
'''