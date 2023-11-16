import random

m = 1
d = 0
e = 0
for i in range(3):
    print(f'{m}. kör:')
    a = input('Kő-papír-olló: ')
    b = random.randint(1, 3)
    if b == 1:
        c = 'kő'
    elif b == 2:
        c = 'papír'
    elif b == 3:
        c = 'olló'
    print(f'A te válaszod: {a}\nA program válasza: {c}')
    m = m + 1
    if a == c:
        print('Döntetlen.')
    elif (a == 'papír' and c == 'olló') or (a == 'olló' and c == 'kő') or (a == 'kő' and c == 'papír'):
        print('Vesztettél.')
        e += 1
    elif (a == 'papír' and c == 'kő') or (a == 'kő' and c == 'olló') or (a == 'olló' and c == 'papír'):
        print('Nyertél.')
        d += 1
    else:
        print('Igen :))')
    print(f'{d}:{e}')