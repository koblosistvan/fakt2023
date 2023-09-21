futás = True
motor_jar = False
sebesség =
while True:
    parancs = input('> ')
    if parancs == 'indít':
        if motor_jar:
            print('Nem inditok, mert a motor jár.')
        print('A motor elindult')
        motor_jar = True
    elif parancs == 'leállít':
        if motor_jar:
            print('A motor ')
            motor_jar = False
        else:
            print('A motor eddig sem járt.')
        print('A motor leállt')
    elif parancs == 'elég':
        print('viszlát')
        futás = False
    elif parancs == 'gyorsít':

    else:
        print('Ezt a parancsot nem értem , adj értelmes utasítást')
