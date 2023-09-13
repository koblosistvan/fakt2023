import cmath
import math

a = int(input('Add meg az "a" értéket:'))
b = int(input('Add meg a "b" értéket:'))
c = int(input('Add meg a "c" értéket:'))

disk = (b**2)-(4*a*c)

megold1 = (-b + math.sqrt(abs(disk)))/(2*a)
megold2 = (-b - math.sqrt(abs(disk)))/(2*a)

megold1komp = (-b + cmath.sqrt(abs(disk)))/(2*a)
megold2komp = (-b - cmath.sqrt(abs(disk)))/(2*a)

if disk == 0:
    print(f'A megoldás {megold1}')

elif disk > 0:
    print(f'Az első megoldá {megold1} \n A második megoldás {megold2}')


else:
    print(f'Az első megoldás: {megold1komp} \n A második megoldás: {megold2komp} ')