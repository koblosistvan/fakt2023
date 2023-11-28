írásjelek = '.!?'
kijelentő = '.'
kérdő = '?'
felszólító = '!'

def darab(szöveg):
    felszólító_mondat = 0
    kérdő_mondat = 0
    kijelentő_mondat = 0
    mondatok = 0
    szavak = szöveg.split(' ')
    for i in range(len(szavak)):
        if szavak[i][-1] in írásjelek:
            mondatok += 1
        if szavak[i][-1] == kijelentő:
            kijelentő_mondat += 1
        if szavak[i][-1] == kérdő:
            kérdő_mondat += 1
        if szavak[i][-1] == felszólító:
            felszólító_mondat += 1
    return mondatok, kijelentő_mondat, kérdő_mondat, felszólító_mondat

a, b, c, d = darab("Első mondat. Ez me a második!")
print(f'Összes mondat: {a}, ebből kijelentő: {b}, kérdő: {c}, felszólító: {d}')