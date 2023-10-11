def vonal():
    print('> ' * 15, '.', '< '*15)

def prime(szam):
    a = True
    for i in range(2, szam):
        if (szam % i == 0):
            a = False
    return a

def andor(x):
    a = '' + 'I'
    for i in range(1, x + 1):
        a += 'I'
        print(f'{a} + 1')
def soos(b):
    a = '' + 'I'
    for i in range(1, b + 1):
        print(f'elif {a} == i:\n\t\t {a} += 1')
        a += 'I'