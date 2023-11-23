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


print(ékezetes('blabla'))
print(ékezetes('blábléá'))
