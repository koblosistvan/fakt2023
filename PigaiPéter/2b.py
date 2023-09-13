import random

a = random.randint(0,9999)
b = random.randint(0,9999)
print(a , b)

c = input(f'{a} és {b} összege:')
d = a + b
if a + b == d:
    print('ggwp')
else:
    print('gfsf')
