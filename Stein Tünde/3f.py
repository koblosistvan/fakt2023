futás = True
motor_jár = False

while futás:
    parancs = input('> ')
    if parancs == 'indít':
        if motor_jár:
            print('A motor már jár.')
        else:
            print('A motor elindult.')
            motor_jár = True
    elif parancs == 'leáll':
        if motor_jár:
            motor_jár = False
            print('A motor leállt.')
        else:
            print('A motor nem jár.')
    elif parancs == 'stop':
        futás = False
    elif parancs == 'gyorsít':
        if motor_jár:
            gyorsít = int(input('> '))
            sebesség = (f'{0 + gyorsít}, km/h')
            print(sebesség)
        else:
            print('A motor nem jár.')
    else:
        print('Nem értem.')