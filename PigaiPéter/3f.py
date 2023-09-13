futás = True
motorjár = False
sebesség = 0

while True:
    parancs = input('>')
    if parancs == 'indít':
        if motorjár:
            print('>A motor már jár')
        else:
            print('>Motor elindult')
            motorjár = True
    elif parancs == 'leáll':
        if sebesség == 0:
            if motorjár:
                print('>A motor leállt')
                motorjár = False
            else:
                print('>A motort nem lehet leállítani mert már áll')
        else:
            print(f'{sebesség}km/h-val nem érdemes leállítani a motort')
    elif parancs == 'elég':
        futás = False
        print('>viszlát')
    if parancs == 'gyorsít':
        if sebesség > 0:
            sebesség = sebesség + 1
            print(f'>A sebességed{sebesség}')
    if parancs == 'lassít':
        if sebesség == 0:
            print('Nem tudok 0 km/h-nál kevesebbel menni')
        else:
            sebesség = sebesség - 1
            print(f'>A sebességed{sebesség}')
        sebesség = sebesség-1


    else:
        print('>Nem értem, adj értelmes utasítást')
