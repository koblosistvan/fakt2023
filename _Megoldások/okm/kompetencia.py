class Pont:
    def __init__(self, pont: int, szint: int):
        self.pont = pont if pont != 'Nincs' else None
        self.szint = szint if szint != 'Nincs' else None


class Meres:
    def __init__(self, sor: str):
        adat = sor.strip().split(';')
        self.azonosito = adat[2]
        self.szoveg_tavaly = Pont(adat[3], adat[4])
        self.szoveg_elozetes = Pont(adat[5], adat[6])
        self.szoveg_vegleges = Pont(adat[7], adat[8])
        self.szoveg = Pont(adat[7], adat[8]) if adat[7] != 'Nincs' else Pont(adat[5], adat[6])
        self.matek_tavaly = Pont(adat[9], adat[10])
        self.matek_elozetes = Pont(adat[11], adat[12])
        self.matek_vegleges = Pont(adat[13], adat[14])
        self.matek = Pont(adat[13], adat[14]) if adat[13] != 'Nincs' else Pont(adat[11], adat[12])


def feladat(s):
    print(f'\n{s}. feladat')


forras = open('okm-2023-7.csv', encoding='utf-8', mode='r')
meresek = []
for sor in list(forras)[3:]:
    meresek.append(Meres(sor))

feladat(2)
azonositok = set([meres.azonosito for meres in meresek])
print(f'A fájlban {len(azonositok)} diák eredményei vannak')

feladat(3)
szoveg = [[meres.azonosito, meres.szoveg] for meres in meresek]
szoveg.sort(key=lambda a: a[1].pont)
szoveg_leg = szoveg[-1]
print(f'A legmagasabb szövegértés pontszámot {szoveg_leg[0]} érte el: {szoveg_leg[1].pont} pont.')

print('Vége.')