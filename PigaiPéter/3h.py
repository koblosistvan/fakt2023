import random
a = 1
b = 999
intervallum = (a, b)  # todo: lista típusok
andor = random.randint(a, b)
kitalalva = False
while not kitalalva:
    playerchoice = int(input(f'Add meg a tipped (A {intervallum} intervallumba)'))
    if playerchoice < andor:
        print('A szám nagyobb mint a tipped')
    elif andor < playerchoice:
        print('A szám kisebb mint a tipped')
    if playerchoice == andor:
        print('A szám kitalálva')
        kitalalva = True
    elif andor - 10 < playerchoice < andor + 10:
        print('forró')
    elif andor - 50 < playerchoice < andor + 50:
        print('meleg')
    elif andor - 100 < playerchoice < andor + 100:
        print('langyos')
    else:
        print('hideg')
