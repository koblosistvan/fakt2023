#kő papír olló

import random

játékos = input('Ird ide: kő(1), papír(2), olló(3)')

gép = random.randint(1,4)

if gép == 1 and játékos == 3 or gép == 2 and játékos == 1 or gép == 3 and játékos == 2:
    print('A gép nyert')
elif gép == 1 and játékos == 1 or gép == 2 and játékos == 2 or gép == 3 and játékos == 3:
    print('Döntetlen')
else:
    print('Te nyertél!')

