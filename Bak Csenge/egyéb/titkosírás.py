
def kódol_dekódol(szó, kódole):
    kódok = "öüóűqwertzuiopőúasdfghjkléáűíyxcvbnm"
    abc = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"

    kódolt_szó = ""
    if kódole:
        for i in range(len(szó)):
            poz = abc.find(szó[i])
            kód = kódok[poz]
            kódolt_szó += kód
    else:
        for i in range(len(szó)):
            kód = abc.find(szó[i])
            poz = kódok[kód]
            kódolt_szó += poz
    return kódolt_szó


logikai = input("True/False: ")
szó = input("A szó: ")
print(kódol_dekódol(szó, logikai))





