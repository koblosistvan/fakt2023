forras = open('Vtabla.dat', mode='r', encoding='utf-8')

tablazat = []

for sor in forras:
    tablazat.append(sor.strip())
forras.close()

szoveg = 'Ez a próba szöveg, amit kódolunk.'
kulcs = 'auto'

print(f'Eredeti szöveg: {szoveg}')

#2.feladat
ekezetes = 'ÁÉÍÓÖŐÚÜŰ'
ekezetmentes = 'AEIOOOUUU'
szoveg = szoveg.upper()
for i in range(len(ekezetes)):
    szoveg = szoveg.replace(ekezetes[i], ekezetmentes[i])


uj_szoveg = ''
for a in range(len(szoveg)):
    if szoveg[a] in tablazat[0]:
        uj_szoveg += szoveg[a]

#3.feladat
print(f'Kódolt szöveg: \t\t{uj_szoveg}')

#4.feladat
kulcs = input('Add meg a kulcsszót:')
kulcs = kulcs.upper()

kulcs = kulcs * (len(uj_szoveg) // len(kulcs) + 1)
kulcs = kulcs[:len(uj_szoveg)]

print(f'Kulcs: \t\t\t\t{kulcs}')

#6.feladat
kodolt = ''
for i in range(len(uj_szoveg)):
    oszlop = tablazat[0].find(uj_szoveg[i])
    sor = 0
    while tablazat[sor][0] != kulcs[i]:
        sor += 1
    kod_karakter = tablazat[sor][oszlop]
    kodolt += kod_karakter
print(kodolt)


