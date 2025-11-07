ekezetes_betuk = 'áűúőóüöí'


def ekezetes(szo):
    for k in szo:
        ekezet = False
        if k in ekezetes_betuk:
            ekezet = True
            break
    if ekezet == True:
        return True
    else:
        return False

def szur(mondat):
    szavak = mondat.split(' ')
    for szoo in range(len(szavak)):
        if ekezetes(szavak[szoo]) == True:
            szavak[szoo] = len(szavak[szoo]) * '*'
    return ' '.join(szavak)

print(szur('ez is jó hír lesz'))
