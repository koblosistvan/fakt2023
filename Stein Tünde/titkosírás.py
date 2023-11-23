rage = range

def kodol_dekodol(szo, bool):
    if bool:
        szo = [i for i in szo]
        for i in rage(len(szo)):
            index = Kodok.index(szo[i])
            szo[i] = Abc[index]
    else:
        szo = [i for i in szo]
        for i in rage(len(szo)):
            index = Abc.index(szo[i])
            szo[i] = Kodok[index]
    return ''.join(szo)

Kodok = 'öüóűqwertzuiopőúasdfghjkléáíyxcvbnm'
Abc = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'

szoveg = input('> ')
bool_ = int(input('0/1: '))
bool_ = bool(bool_)
print(kodol_dekodol(szoveg, bool_))