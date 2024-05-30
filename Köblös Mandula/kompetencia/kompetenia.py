class kompetencia:
    def __init__(self, azonosito: str, tavalyi_kepessegpont: str, tavalyi_kepessegszint: str, elozetes_kepessegpont: str, elozetes_kepessegszint: str, vegleges_kepessegpont: str, vegleges_kepessegszint: str):
        self.azonosito = azonosito
        self.tavalyi_kepessegpont = tavalyi_kepessegpont
        self.tavalyi_kepessegszint = tavalyi_kepessegszint
        self.elozetes_kepessegpont = elozetes_kepessegpont
        self.elozetes_kepessegszint = elozetes_kepessegszint
        self.vegleges_kepessegpont = None if vegleges_kepessegpont == 'Nincs' else int(vegleges_kepessegpont)
        self.vegleges_kepessegszint = None if vegleges_kepessegszint == 'Nincs' else vegleges_kepessegszint
        self.pont = vegleges_kepessegpont if vegleges_kepessegpont != 'Nincs' else elozetes_kepessegpont
        self.szint = vegleges_kepessegszint if vegleges_kepessegszint != 'Nincs' else elozetes_kepessegszint

matematika = []
szovegertes = []
forras = open("okm-2023-7.csv", mode='r', encoding='utf-8')
forras.readline()
forras.readline()
forras.readline()
for sor in forras:
    adat = sor.strip().split(';')
    szovegertes.append(kompetencia(azonosito=str(adat[2]), tavalyi_kepessegpont=adat[3], tavalyi_kepessegszint=adat[4], elozetes_kepessegpont=adat[5], elozetes_kepessegszint=adat[6], vegleges_kepessegpont=adat[7], vegleges_kepessegszint=adat[8]))
    matematika.append(kompetencia(azonosito=str(adat[2]), tavalyi_kepessegpont=adat[9], tavalyi_kepessegszint=adat[10], elozetes_kepessegpont=adat[11], elozetes_kepessegszint=adat[12], vegleges_kepessegpont=adat[13], vegleges_kepessegszint=adat[14]))
forras.close()

# 2. feladat
print(len(set(szovegertes)))

# 3. feladat
legmagasabb_pontszám = szovegertes[0].pont
legmagasabb_pontszám_id = 0
for i in range(len(szovegertes)):
    if szovegertes[i].pont > legmagasabb_pontszám:
        legmagasabb_pontszám = szovegertes[i].pont
        legmagasabb_pontszám_id = i
print(f'A legmagsabb pontszámot elérő diák azonosítója: {szovegertes[legmagasabb_pontszám_id].azonosito}')

# 4. feladat
valtozas = 0
for i in range(len(szovegertes)):
    if szovegertes[i].elozetes_kepessegpont == szovegertes[i].vegleges_kepessegpont:
        valtozas += 1
print(f'{64 - valtozas} tanulonak váztozott az eredménye.')