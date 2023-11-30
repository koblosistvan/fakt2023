ekezetesbetuk = 'óüőúáűéöí'

def ekezetes(szo):
    for k in szo:
        if k in ekezetesbetuk:
            return True
            break
    else:
        return False


print(ekezetes('blablaá'))
print(ekezetes('blablaaa'))


def szur(mondat)
    szavak = mondat.split(' ')
    for i in range(len(szavak)):  #kicsereles otthon + komal feladat dec 10 ig
