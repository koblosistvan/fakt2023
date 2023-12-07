forrás = open('Vtabla.dat', mode='r', encoding='utf-8')
kódtábla = []
for sor in forrás:
    kódtábla.append(sor.strip())
forrás.close()


szöveg = 'Ez a próba szöveg, amit kódolunk!'


# 2. feladat
print(f'Eredeti szöveg: \t{szöveg}')
ékezetes = 'ÁÉÍÓÖŐÚÜŰ'
ékezetmentes = 'AEIOOOUUU'
szöveg = szöveg.upper()
for i in range(len(ékezetes)):
    szöveg = szöveg.replace(ékezetes[i], ékezetmentes[i])

kódolandó = ''
for i in range(len(szöveg)):
    if szöveg[i] in kódtábla[0]:
        kódolandó += szöveg[i]

print(f'Kódolandó szöveg: \t{kódolandó}')

# 4-5 feladat
kulcs = 'auto'

kulcs = kulcs.upper()
kulcs = kulcs * (len(szöveg) // len(kulcs) + 1)
kulcs = kulcs[:len(kódolandó)]
print(f'Kulcs: \t\t\t\t{kulcs}')

# 6. feladat
kódolt = ''
for i in range(len(kódolandó)):
    oszlop = kódtábla[0].find(kódolandó[i])
    sor = 0
    while kódtábla[sor][0] != kulcs[i]:
        sor += 1
    kód_karakter = kódtábla[sor][oszlop]
    kódolt += kód_karakter
print(f'Kódolt: \t\t\t{kódolt}')
