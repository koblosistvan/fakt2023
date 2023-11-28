ékezetes_betűk = "öüóőúéáűíÖÜÓŐÚÉÁŰÍ"


def ékezetes(szó):
    for k in szó:
        if k in ékezetes_betűk:
            return True
            break
    else:
        return False


def szűr(mondat):
    szavak = mondat.split(" ")
    for i in range(len(szavak)):
        if ékezetes(szavak[i]):
            print(len(szavak[i])*"*", end=" ")
        else:
            print(szavak[i], end=" ")

a_mondat = input("Írj egy mondatot! ")
print(szűr(a_mondat))










