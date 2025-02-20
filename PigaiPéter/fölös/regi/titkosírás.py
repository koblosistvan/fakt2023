
def kódol_dekódol(szó,kóde):
    KÓDOK = "öüóűqwertzuiopőúasdfghjkléáíyxcvbnm"
    ABC = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"
    abc = list(x for x in ABC)
    kódok = list(x for x in KÓDOK)
    szó = list(x for x in szó)
    kódolt = []
    dekódolt = []
    if kóde == False:
        for i in range(len(szó)):
            y = szó[i]
            kódolt.append(kódok[abc.index(y)])
        return ''.join(kódolt)
    elif kóde == True:
        for i in range(len(szó)):
            y = szó[i]
            dekódolt.append(abc[kódok.index(y)])
        return ''.join(dekódolt)

print(kódol_dekódol('whwk', True ))