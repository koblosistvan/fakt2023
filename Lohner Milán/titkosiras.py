def kododoldekodol(szó, kódole):

    kodok = "öüóűqwertzuiopőúasdfghjkléáíyxcvbnm"
    abc = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"
    kodoltszo = ''
    for i in range(len(szó)):
        if kódole:
            kodoltszo += kodok[abc.find(szó[i])]

        else:
            kodoltszo += abc[kodok.find(szó[i])]

    return(kodoltszo)

print(kododoldekodol('alma',True))

