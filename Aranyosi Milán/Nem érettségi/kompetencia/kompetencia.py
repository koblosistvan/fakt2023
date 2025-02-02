class Meres:
    def __init__(self, azonosito, tavalyi_kepessegpont, tavalyi_kepessegszint, ideielozetes_kepessegpont, ideielozetes_kepessegszint, ideivegleges_kepessegpont, ideivegleges_kepessegszint):
        self.azonosito = azonosito
        self.tavalyi_kepessegpont = tavalyi_kepessegpont
        self.tavalyi_kepessegszint = tavalyi_kepessegszint
        self.ideielozetes_kepessegpont = None if ideielozetes_kepessegpont == 'Nincs' else int(ideielozetes_kepessegszint)
        self.ideielozetes_kepessegszint =None if ideielozetes_kepessegszint == 'Nincs' else int(ideielozetes_kepessegszint)
        self.ideivegleges_kepessegpont = None if ideivegleges_kepessegpont == 'Nincs' else int(ideivegleges_kepessegpont)
        self.ideivegleges_kepssegszint = None if ideivegleges_kepessegszint == 'Nincs' else int(ideivegleges_kepessegszint)
        self.pont = ideivegleges_kepessegpont if ideivegleges_kepessegpont != 'Nincs' else ideielozetes_kepessegpont
        self.szint = ideivegleges_kepessegszint if ideivegleges_kepessegszint != 'Nincs' else ideielozetes_kepessegszint



szovegertes = []
matematika = []

forras = open('kompetencia', mode='r', encoding='utf-8')
forras.readline()
forras.readline()
forras.readline()
for sor in forras:
    adat = sor.strip().split(';')
    szovegertes.append(Meres(azonosito=adat[2], tavalyi_kepessegpont=adat[3], tavalyi_kepessegszint=adat[4], ideielozetes_kepessegpont=adat[5], ideielozetes_kepessegszint=adat[6], ideivegleges_kepessegpont=adat[7], ideivegleges_kepessegszint=adat[8]))
    matematika.append(Meres(azonosito=adat[2], tavalyi_kepessegpont=adat[9], tavalyi_kepessegszint=adat[10], ideielozetes_kepessegpont=adat[11], ideielozetes_kepessegszint=adat[12], ideivegleges_kepessegpont=adat[13], ideivegleges_kepessegszint=adat[14]))
forras.close()

#2. feladat
print(f'A fájlban {len(set(szovegertes))} azonosító van.')

#3. feladat
legmagasabb_i_szov = szovegertes[0].pont
legmagasabb_i_szov_id = 0
for i in range(len(szovegertes)):
    if szovegertes[i].pont > legmagasabb_i_szov:
        legmagasabb_i_szov = szovegertes[i].pont
        legmagasabb_i_szov_id = szovegertes[i].azonosito
print(f'A legtöbb pontszám a {legmagasabb_i_szov_id} azonosítójú diák volt.')

#4. feladat
valtozott = 0
for i in range(len(szovegertes)):