pont = input('Add meg a pontot:')
andor = pont.replace('A', '').replace('(', '').replace(')', '')
x, y = andor.split(':')
x, y = int(x), int(y)

if x > 0 and y > 0:
    print(f'{pont} pont az 1. síknegyedbe helyezkedik el')

elif x < 0 and y < 0:
    print(f'{pont} pont a 3. síknegyedbe helyezkedik el')

elif x < 0 < y:
    print(f'{pont} pont a 2. síknegyedbe helyezkedik el')

elif x > 0 > y:
    print(f'{pont} pont az 4. síknegyedbe helyezkedik el')

elif x == 0 and y > 0:
    print(f'{pont} pont illeszkeszkedik az x tengelyre')

elif x > 0 and y == 0:
    print(f'{pont} pont illeszkeszkedik az y tengelyre')

else:
    print(f'{pont} az origóra illeszkedik')