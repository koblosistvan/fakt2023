ékezetes_betűk = "öüóőúéáűíÖÜÓŐÚÉÁŰÍ"


def ékezetes(szó):
    for k in szó:
        if k in ékezetes_betűk:
            return True
            break
    else:
        return False

print(ékezetes("nkfdkasdfj"))














