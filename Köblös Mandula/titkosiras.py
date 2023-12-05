def kodol_dekodol(szó, kódole):
    kódok = 'öüóűqwertzuiopőúasdfghjkléáíyxcvbnm'
    ábécé = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'

    kódolt_szó = ''

    for i in range(len(szó)):
       if kódole:
            kódolt_szó += kódok[ábécé.find(szó[i])]
       else:
           kódolt_szó += ábécé[kódok.find(szó[i])]

    return kódolt_szó

print(kodol_dekodol('alma', True))
print(kodol_dekodol('whwk', False))