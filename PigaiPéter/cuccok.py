def vonal():
    print('> ' * 15, '.', '< '*15)

def prime(szam):
    a = True
    for i in range(2, szam):
        if (szam % i == 0):
            a = False
    return a

