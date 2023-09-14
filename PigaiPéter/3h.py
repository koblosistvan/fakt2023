import random
a = 1
b = 999
intervallum = (a, b)
andor = random.randint(a, b)
kitalalva = False
while not kitalalva:
    playerchoice = int(input(f'Add meg a tipped (A {intervallum}-ba)'))
    print(andor)
    if andor - 100 < playerchoice < andor + 100:
        print('langyos')
