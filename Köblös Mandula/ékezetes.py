ékezetes_betűk = 'áéóöőúüűí'

def ékezetes(szó):
    for k in szó:
        if k in ékezetes_betűk:
            return True
            break
    else:
        return False

def szűr(mondat):
    szavak = mondat.split(' ')
    for i in range(len(szavak)):
        if ékezetes(szavak[i]):
            szavak[i] = '*' * len(szavak[i])
    return " ".join(szavak)



print(szűr('ez jó hír lesz'))

