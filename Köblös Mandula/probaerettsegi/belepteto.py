forras = open('bedat.txt', mode='r', encoding='utf-8')

tanulo = []
idopont = []
esemeny = []

for sor in forras:
    adat = sor.strip().split(' ')
    tanulo.append(adat[0])
    idopont.append(adat[1])
    esemeny.append(int(adat[2]))

ora = []
perc = []
for ido in idopont:
    x = ido.split(':')
    ora.append(int(x[0]))
    perc.append(int(x[1]))

forras.close()

print('2.feladat')
print(f'Az első tanuló {idopont[0]}-kor lépett be az főkapun.')
print(f'Az utolsó tanuló {idopont[-1]}-kor lépett ki az főkapun.')

def percek(ó, p):
    orak = ó*60
    return orak+p

kiiras = open('kesok.txt', mode='w', encoding='utf-8')

for i in range(len(tanulo)):
    if esemeny[i] == 1 and percek(ora[i], perc[i]) > percek(7, 50) and percek(ora[i], perc[i]) <= percek(8, 15):
        print(f'{tanulo[i]} {idopont[i]}', file=kiiras)

ebedeltek = 0
print('4.feladat')
for i in range(len(tanulo)):
    if esemeny[i] == 3:
        ebedeltek += 1
print(f'A menzán aznap {ebedeltek} tanuló ebédelt.')

print('5.feladat')
kolcsonzott = 0
kolcsonzott_kod = []
for i in range(len(tanulo)):
    if esemeny[i] == 4 and tanulo[i] not in kolcsonzott_kod:
        kolcsonzott += 1
        kolcsonzott_kod.append(tanulo[i])
print(f'Aznap {kolcsonzott} tanuló kölcsönzött a könyvtárban.')
if kolcsonzott > ebedeltek:
    print('Többen voltak, mint a menzán.')
else:
    print('Nem voltak többen, mint a menzán.')

print('6.feladat')
reggel_jottek = []
for i in range(len(tanulo)):
    if esemeny[i] == 1 and percek(ora[i], perc[i]) <= percek(10, 50):
        reggel_jottek.append(tanulo[i])
reggel_kiment = []
for i in range(len(tanulo)):
    if esemeny[i] == 2 and percek(ora[i], perc[i]) <= percek(10, 50):
        reggel_kiment.append(tanulo[i])
megint_bejott = []
for i in range(len(tanulo)):
    if esemeny[i] == 1 and percek(ora[i], perc[i]) > percek(10, 50) and percek(ora[i], perc[i]) < percek(11, 00):
        megint_bejott.append(tanulo[i])
ketszer_bejott = []
for i in range(len(megint_bejott)):
    if megint_bejott[i] in reggel_jottek and megint_bejott[i] not in reggel_kiment:
        ketszer_bejott.append(megint_bejott[i])

print('Az érintett tanulók:')
print(' '.join(ketszer_bejott))

print('7.feladat')
azonosito = input('Egy tanuló auonosítója=')
belepes_ora = 0
belepes_perc = 0
kilepes_ora = 0
kilepes_perc = 0
if azonosito in tanulo:
    for i in range(len(tanulo)):
        if esemeny[i] == 1 and tanulo[i] == azonosito:
            belepes_ora = ora[i]
            belepes_perc = perc[i]
            break

    for i in range(len(tanulo)):
        if esemeny[i] == 2 and tanulo[i] == azonosito:
            kilepes_ora = ora[i]
            kilepes_perc = perc[i]

    eltelt_ido = percek(kilepes_ora, kilepes_perc)-percek(belepes_ora, belepes_perc)

    eltelt_ora = eltelt_ido//60
    eltelt_perc = eltelt_ido-eltelt_ora*60

    print(f'A tanuló érkezése és távozása között {eltelt_ora} óra {eltelt_perc} perc telt el.')
else:
    print('Ilyen azonosítójú tanuló aznap nem volt az iskolában.')