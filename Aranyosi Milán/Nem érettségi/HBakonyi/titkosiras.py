def kodol_dekodol(szo,kodole):
    kodok = 'öüóűqwertzuiopőúasdfghjkléáíyxcvbnm'
    abece = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'

    kodolt_szo = ' '

    for i in range(len(szo)):
        if kodole:
            kodolt_szo += kodok[abece.find(szo[i])]
        else:
            kodolt_szo += abece[kodok.find(szo[i])]

    return kodolt_szo

print(kodol_dekodol('alma' , True))
print(kodol_dekodol('whwk' , False))
