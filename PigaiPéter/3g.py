import random

playerstatus = 0
computerstatus = 0


for i in range(3):
    playerchoice = input('>')
    computerchoice = random.randint(1, 3)    # 1 = kő 2 = papír 3 = olló
    if computerchoice == 1 and playerchoice == 'kő':
        print('A gép követ választott, a játékos követ választott: döntetlen')
        playerstatus = playerstatus + 0
        computerstatus = computerstatus + 0
        print(f'Az állás {playerstatus}:{computerstatus}') # todo: amit minden esetben megteszünk, azt if-en kívülre
    elif computerchoice == 2 and playerchoice == 'papír':
        print('A gép papírt választott, a játékos papírt választott: döntetlen')
        playerstatus = playerstatus + 0
        computerstatus = computerstatus + 0
        print(f'Az állás {playerstatus}:{computerstatus}')
    elif computerchoice == 3 and playerchoice == 'olló':
        print('A gép ollót választott, a játékos ollót választott: döntetlen')
        playerstatus = playerstatus + 0
        computerstatus = computerstatus + 0
        print(f'Az állás {playerstatus}:{computerstatus}')
    elif computerchoice == 1 and playerchoice == 'papír':
        print('A gép követ választott, a játékos papírt')
        playerstatus = playerstatus + 1
        computerstatus = computerstatus + 0
        print(f'Az állás {playerstatus}:{computerstatus}')
    elif computerchoice == 1 and playerchoice == 'olló':
        print('A gép követ választott, a játékos ollót')
        playerstatus = playerstatus + 0
        computerstatus = computerstatus + 1
        print(f'Az állás {playerstatus}:{computerstatus}')
    elif computerchoice == 2 and playerchoice == 'kő':
        print('A gép papírt választott, a játékos követ')
        playerstatus = playerstatus + 0
        computerstatus = computerstatus + 1
        print(f'Az állás {playerstatus}:{computerstatus}')
    elif computerchoice == 2 and playerchoice == 'olló':
        print('A gép papírt választott, a játékos ollót')
        playerstatus = playerstatus + 1
        computerstatus = computerstatus + 0
        print(f'Az állás {playerstatus}:{computerstatus}')
    elif computerchoice == 3 and playerchoice == 'kő':
        print('A gép ollót választott, a játékos követ')
        playerstatus = playerstatus + 1
        computerstatus = computerstatus + 0
        print(f'Az állás {playerstatus}:{computerstatus}')
    elif computerchoice == 3 and playerchoice == 'papír':
        print('A gép ollót választott, a játékos papírt')
        playerstatus = playerstatus + 0
        computerstatus = computerstatus + 1
        print(f'Az állás {playerstatus}:{computerstatus}')
    if i == 2:
        if playerstatus > computerstatus:
            print('Vége a játéknak, a játékos győzött')
        elif playerstatus < computerstatus:
            print('Vége a játéknak, a gép győzött')
