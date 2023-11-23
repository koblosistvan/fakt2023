def kódol_dekódol(szó,kódole):
    KÓDOK = 'öüóűqwertzuiopőúasdfghjkléáíyxcvbnm'
    ÁBÉCÉ = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'
    lista = list(szó)
    if kódole == 'kódol':
        for i in range(len(szó)):
            lista[i] = KÓDOK[ÁBÉCÉ.index(lista[i])]
        return ''.join(lista)
    elif kódole == 'dekódol':
        for i in range(len(szó)):
            lista[i] = ÁBÉCÉ[KÓDOK.index(lista[i])]
        return ''.join(lista)
    else:
        return 'Nem értelmezhető parancs.'

forrás = input('Szó (kódolni vagy dekódolni kívánt szó vagy kód), kódolja vagy dekódolja-e (kódol vagy dekódol): ')
szó = forrás.split(',')[0]
kódole = forrás.split(',')[1]
print(kódol_dekódol(szó, kódole))
