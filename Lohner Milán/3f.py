
run=True
motor_jár=False

while run:
    parancs = input('> ')
    if parancs == 'start':
        if motor_jár:
            print('Nem indítok mert a motor már jár')
        print('A motor elindult')
        motor_jár=True
    elif parancs == 'stop':
        if motor_jár:

        print('A motor leállt')
    elif parancs== 'off':
        print('viszlát')
        run=False

    elif parancs == gyorsít:


    else:
        print('Nem értem a parancsot!')