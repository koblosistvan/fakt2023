futás = True
motorjár = False
sebesség = 0
sebkorlat = 50

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
    elif parancs == 'gyorsít':
        if sebkorlat > sebesség >= 0 and motorjár:
            sebesség = sebesség + 10
            print(f'>A sebességed{sebesség}')
        else:
            if motorjár:
                print('>Elérted a sebességkorlátot')
            else:
                print('>Nem jár a motor')
    elif parancs == 'lassít':
        if sebesség == 0 and motorjár:
            print('Nem tudok 0 km/h-nál kevesebbel menni')
        else:
            if motorjár:
                sebesség = sebesség - 10
                print(f'>A sebességed{sebesség}')
            else:
                print('>A motor nem jár')
    else:
        print('>Nem értem, adj értelmes utasítást')
