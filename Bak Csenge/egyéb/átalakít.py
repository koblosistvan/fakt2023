
def betűvé(szám, kisebnagyob):
    if kisebnagyob == "kisebb":
        szótár = {0: "nulla", 1: "egy", 2: "kettő", 3: "három", 4: "négy", 5: "öt", 6: "hat", 7: "hét", 8: "nyolc", 9: "kilenc"}
    elif kisebnagyob == "nagyobb" and szám not in [10, 20]:
        szótár = {1: "tizen", 2: "huszon", 3: "harminc", 4: "negyven", 5: "ötven", 6: "hatvan", 7: "hetven", 8: "nyolcvan",
                  9: "kilencven"}
    else:
        szótár = {1: "tíz", 2: "húsz"}
    return szótár[szám]


def kisebb(szám):
    egytől_százig = []
    for i in range(0, 101):
        egytől_százig.append(str(i))

    if szám in egytől_százig:
        if int(szám) < 10:
            egyes = int(szám)
            return betűvé(egyes, "kisebb")
        elif int(szám) < 100:
            tizes = int(str(szám)[0])
            egyes = int(str(szám)[1])
            találat = betűvé(tizes, "nagyobb") + betűvé(egyes, "kisebb")
            return találat
        else:
            return False
    else:
        return False


def átalakít(mondat):
    szavak = mondat.split(" ")
    for i in range(len(szavak)):
        if kisebb(szavak[i]) != False:
            print(kisebb(szavak[i]), end=" ")
        else:
            print(szavak[i], end=" ")

print(átalakít("ez 101 és 99 mondat"))









