def vonal():
    print('-' * 30)

def prime(szam):
    a = True
    for i in range(2, szam):
        if (szam % i == 0):
            a = False
    return a

def megnyit(a):
    open(a, mode= 'r', encoding= 'utf8')
