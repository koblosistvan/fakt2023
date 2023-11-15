# Döntsük el két számról, hogy osztható-e egyik a másikkal. A felhasználó tetszőleges sorrendben
# adja meg az osztandót és az osztót, tehát arra is figyelnünk kell, hogy melyik szám nagyobb.

a = int(input('Add meg az egyik számot: '))
b = int(input('Add meg a másik számot: '))

# egyik megoldás
if a == b:
    print(f'{a} = {b}')
elif (a > b) and (a % b == 0):
    print(f'{a} osztható {b}.')
elif (b > a) and (b % a == 0):
    print(f'{b} osztható {a}.')
else:
    print(f'{a} és {b} nem osztói egymásnak.')

# másik megoldás
if a < b:
    a, b = b, a

if a == b:
    print(f'{a} = {b}')
elif a % b == 0:
    print(f'{b} osztható {a}.')
else:
    print(f'{a} és {b} nem osztói egymásnak.')

