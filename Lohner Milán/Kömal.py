
def oszlopok_beolvas():
    N = int(input('Adja meg az oszlopok számát:'))
    oszlopok = []
    for i in range(N):
        oszlop = list(map(int,
input(f"{i+1}. oszlop: ").split()))
        oszlopok.append(oszlop)
    return oszlopok

def szabad_korong(oszlopok):
    osszeskorong = set(range(1 , 26))
    elfoglaltkorong = set()

    for oszlop in oszlopok:
        elfoglaltkorong.update(oszlop)

    szabad_korong = sorted(list(osszeskorong - elfoglaltkorong))
    return szabad_korong

def nemhozzatehetokor(oszlopok):
    szabad = szabad_korong(oszlopok)
    nemhozzateheto = []

    for i in szabad:
        for oszlop in oszlopok:
            if all(i % szam == 0 for szam in oszlop):
                break
            else:
                nemhozzateheto.append(i)

    return nemhozzateheto

if __name__ == "__main__":
    oszlopok = oszlopok_beolvas()
    szabad = szabad_korong(oszlopok)
    nemhozateheto = nemhozzatehetokor(oszlopok)

    print("Szabad korongok: ", szabad)
    print("Nem hozzaferheto kor:",nemhozateheto)




