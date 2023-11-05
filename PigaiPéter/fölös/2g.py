a = int(input('Add meg az egyik számot:'))
b = int(input('Add meg a második számot:'))

if a > b:
    c = a/b
    if c.is_integer():
        print(f'{a} és {b} osztható egymással')
    else:
        print(f'{a} és {b} nem osztható egymással')

elif b > a:
    c = b/a
    if c.is_integer():
        print(f'{b} és {a} osztható egymással')
    else:
        print(f'{b} és {a} nem osztható egymással')

elif b == a:
    print(f'{a} és {b} oszthatóak egymással')
