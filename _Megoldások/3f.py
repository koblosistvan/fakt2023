futás = True
motor_jár = False

while futás:
    parancs = input('> ')
    if parancs == 'indit':
        if motor_jár:
            print('Nem indítok, mert a motor már jár.')
        else:
            print('A motor elindult.')
            motor_jár = True
    elif parancs == 'leáll':
        if motor_jár:
            print('A motor leállt.')
            motor_jár = False
        else:
            print('Nem állíthatom le, mert a motor nem is jár.')
    elif parancs == 'elég':
        print('Viszlát!')
        futás = False
    else:
        print('Nem értem, adj értelmes utasítást!')
