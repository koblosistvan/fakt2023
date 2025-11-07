# 1
forras = open("Stein Tünde/érettségi/info/2020infemelttav/tavirathu13.txt", 'r', encoding='utf-8')
telepules = []
ido = []
szel = []
hom = []
for i in forras:
    sor = i.strip().split(' ')
    telepules.append(sor[0])
    ido.append(sor[1])
    szel.append(sor[2])
    hom.append(int(sor[3]))
forras.close()

# 2
bekert_tel = input('2. feladat\nAdja meg egy település kódját! Település: ')
for i in range(len(ido)):
    if telepules[-1-i] == bekert_tel:
        print(f'Az utolsó mérési adat a megadott településről {ido[-1-i][0:2]}:{ido[-1-i][2:4]}-kor érkezett.')
        break

# 3
legnagyobbindex = hom.index(max(hom))
legkisebbindex = hom.index(min(hom))
print(f'A legalacsonyabb hőmérséklet: {telepules[legkisebbindex]} {ido[legkisebbindex][0:2]}:{ido[legkisebbindex][2:4]} {hom[legkisebbindex]} fok.\n'
      f'A legmagasabb hőmérséklet: {telepules[legnagyobbindex]} {ido[legnagyobbindex][0:2]}:{ido[legnagyobbindex][2:4]} {hom[legnagyobbindex]} fok.')

# 4
van = False
for i in range(len(szel)):
    if szel[i] == '00000':
        print(f'{telepules[i]} {ido[i][0:2]}:{ido[i][2:4]}')
        van = True
if not van:
    print('Nem volt szélcsend a mérések idején.')

# 5
print('5. feladat')
telepulesek = []
for i in telepules:
    if i not in telepulesek:
        telepulesek.append(i)
for i in range(len(telepulesek)):
    osszeg = 0
    oszto = 0
    orak = []
    maximum = 0
    minimum = 100
    for k in range(len(hom)):
        if telepules[k] == telepulesek[i] and ido[k][0:2] in ('01', '07', '13', '19'):
            osszeg += hom[k]
            oszto += 1
            if hom[k] > maximum:
                maximum = hom[k]
            if hom[k] < minimum:
                minimum = hom[k]
            orak.append(ido[k][0:2])
    if '01' in orak and '07' in orak and '13' in orak and '19' in orak:
        atlag = f'Középhőmérséklet: {round(osszeg/oszto)}'
    else:
        atlag = 'NA'
    print(f'{telepulesek[i]} {atlag}; Hőmérséklet-ingadozás: {maximum-minimum}')
# sírok

# 6

    




""""
2. feladat
Adja meg egy település kódját! Település: SM
Az utolsó mérési adat a megadott településről 23:45-kor érkezett.
3. feladat
A legalacsonyabb hőmérséklet: SM 23:45 16 fok.
A legmagasabb hőmérséklet: DC 13:15 35 fok.
4. feladat
BP 01:00
DC 02:15
SN 03:15
BC 04:45
DC 04:45
SN 05:15
SN 05:45
KE 08:45
BC 11:45
5. feladat
BP Középhőmérséklet: 23; Hőmérséklet-ingadozás: 8
DC Középhőmérséklet: 29; Hőmérséklet-ingadozás: 15
SM Középhőmérséklet: 22; Hőmérséklet-ingadozás: 8
PA Középhőmérséklet: 21; Hőmérséklet-ingadozás: 7
SN Középhőmérséklet: 26; Hőmérséklet-ingadozás: 13
PR Középhőmérséklet: 21; Hőmérséklet-ingadozás: 8
BC NA; Hőmérséklet-ingadozás: 14
PP NA; Hőmérséklet-ingadozás: 6
KE NA; Hőmérséklet-ingadozás: 13
6. feladat
A fájlok elkészültek. """