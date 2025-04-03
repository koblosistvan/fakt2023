forras = open('bedat.txt', mode='r', encoding='utf-8')

tanulok = []
idopontok = []
esemeny = []


for sor in forras:
    adat = sor.strip().split(' ')
    tanulok.append(adat[0])
    idopontok.append(adat[1])
    esemeny.append(int(adat[2]))

print('2.feladat')

for i in range(len(esemeny)):
    if esemeny[i] == 1:
        print(f'Az első tanuló {idopontok[i]}-kor lépett be a főkapun.')
        break

for i in range(len(esemeny)):
    if esemeny[i] == 2:
        utolso_kilepo_ideje = idopontok[i]

print(f'Az utolsó {utolso_kilepo_ideje}-kor lépett ki a főkapun.')

kimenet = open('kesok.txt', mode='w', encoding='utf-8')

idopontok_orapercben = []

for i in range(len(idopontok)):
    oraperc = idopontok[i].split(':')
    for i in range(len(oraperc)):
        oraperc[i] = int(oraperc[i])
    idopontok_orapercben.append(oraperc)

for i in range(len(esemeny)):
    if esemeny[i] == 1:
        if idopontok_orapercben[i][0] == 7 and idopontok_orapercben[i][1] > 50:
            print(f'{idopontok[i]} {tanulok[i]}', file=kimenet)
        elif idopontok_orapercben[i][0] == 8 and idopontok_orapercben[i][1] <= 15:
            print(f'{idopontok[i]} {tanulok[i]}', file=kimenet)

print('4.feladat')

aznap_ebedeltek_lista = []

for i in range(len(esemeny)):
    if esemeny[i] == 3:
        if tanulok[i] not in aznap_ebedeltek_lista:
            aznap_ebedeltek_lista.append(tanulok[i])

aznap_ebedeltek = len(aznap_ebedeltek_lista)

print(f'A menzán aznap {aznap_ebedeltek} tanuló ebédelt.')

print('5.feladat')

aznap_kolcsonoztek_lista = []


for i in range(len(esemeny)):
    if esemeny[i] == 4:
        if tanulok[i] not in aznap_kolcsonoztek_lista:
            aznap_kolcsonoztek_lista.append(tanulok[i])

aznap_kolcsonoztek = len(aznap_kolcsonoztek_lista)

print(f'Aznap {aznap_kolcsonoztek} tanuló kölcsönzött a könyvtárban.')

if aznap_kolcsonoztek > aznap_ebedeltek:
    print('Többen voltak, mint a menzán.')
else:
    print('Nem voltak többen, mint a menzán.')

print('6.feladat')

beert_azonosito = []

for i in range(len(idopontok_orapercben)):
    if idopontok_orapercben[i][0] == 10 and idopontok_orapercben[i][1] >= 50 and esemeny[i] == 1:
        beert_azonosito.append(tanulok[i])

beert_tanulok_indexei = []
beert_tanulok_indexei_egyszeres = []

for i in range(len(tanulok)):
    if tanulok[i] in beert_azonosito:
        if esemeny[i] == 1:
            beert_tanulok_indexei.append(tanulok[i])
            if tanulok[i] not in beert_tanulok_indexei_egyszeres:
                beert_tanulok_indexei_egyszeres.append(tanulok[i])

for i in range(len(beert_tanulok_indexei_egyszeres)):
    if beert_tanulok_indexei_egyszeres[i] in beert_tanulok_indexei:
        beert_tanulok_indexei.remove(beert_tanulok_indexei_egyszeres[i])

print('Az érintett tanulók')

kimentek = ''

for i in range(len(beert_tanulok_indexei)):
    kimentek += f'{beert_tanulok_indexei[i]} '

print(kimentek)

print('7.feladat')

adott_tanulo = input('Egy tanuló azonosítója=')

adott_tanulo_bejovetel = []
adott_tanulo_kimenetel = []

if adott_tanulo in tanulok:
    for i in range(len(tanulok)):
        if tanulok[i] == adott_tanulo:
            if esemeny[i] == 1:
                adott_tanulo_bejovetel.append(idopontok_orapercben[i])
            elif esemeny[i] == 2:
                adott_tanulo_kimenetel.append(idopontok_orapercben[i])
    elso_bemenetel = adott_tanulo_bejovetel[0]
    utolso_kimentel = adott_tanulo_kimenetel[-1]

    kimenetel = utolso_kimentel[0] * 60 + utolso_kimentel[1]
    bemenetel = elso_bemenetel[0] * 60 + elso_bemenetel[1]

    idopercben = kimenetel - bemenetel
    ora = idopercben // 60
    perc = idopercben % 60

    print(f'A tanuló érketzése és távozása között {ora} óra {perc} perc telt el.')
else:
    print('Ilyen azonosítójú tanuló aznap nem volt iskolában.')

