import random

A = random.randint(0, 10)
print(A)
for i in range(21):
    a = int(input('Az A szám értéke: '))
    if A == a:
        print('Eltaláltad')
        break
    elif A > a:
        print('Az A szám nagyobb ennél.')
    elif A < a:
        print('Az A szám kisebb ennél.')
    if abs(a - A) <= 2:
        print('Közel.')
    elif abs(a - A) < 5:
        print('Lehetne közelebb.')
    else:
        print('Távol.')
    if 10 < i <= 15:
        print('Béna.')
    elif 15 <= i < 20:
        print('Még 5 lehetőséged van.')
    elif i == 20:
        print('Nem találtad el.')