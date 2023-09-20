#rockpaperscissors
import random

print('Klasszikus ko papír olló')

print('Kő=1 papír=2 olló=3')

gep=random.randint(1,3)

b=int(input('Kő papír olló:'))

if b == gep:
        print('Hát ez döntetlen')

elif b == 1 and gep == 2:
        print('vesztettél ellenfélnek papírja volt')

elif b == 1 and gep == 3:
        print('Nyertél ellenfélnek ollója volt')

elif b == 2 and gep == 1:
        print('Nyertél ellenfélnek kője volt')

elif b == 2 and gep == 3:
        print('Vesztettél ellenfélnek ollója volt')

elif b == 3 and gep == 1:
        print('Vesztettél ellenfélnek kője volt')

elif b == 3 and gep == 2:
        print('Nyertél ellenfélnek papírja volt')








