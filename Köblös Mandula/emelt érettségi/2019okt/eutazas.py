forras = open("utasadat.txt", mode="r", encoding="utf-8")

allomas = []
ido = []
kartya_azonosito = []
berlet_fajta = []
ervenyesseg = []

for sor in forras:
    adat = sor.strip().split(" ")
    allomas.append(int(adat[0]))
    ido.append(adat[1])
    kartya_azonosito.append(int(adat[2]))
    berlet_fajta.append(adat[3])
    ervenyesseg.append(int(adat[4]))

datum = []
ora = []
for a in ido:
    item = a.strip().split('-')
    datum.append(int(item[0]))
    ora.append(int(item[1]))

forras.close()

print(datum)
print('2. feladat')
print(f'A buszra {len(allomas)} utas akart felszállni.')

print('3. feladat')
lejart = 0
for i in range(len(datum)):
    if datum[i] > ervenyesseg[i] and ervenyesseg[i] > 10 or ervenyesseg[i] == 0:
        lejart += 1
print(f'A buszra {lejart} utas nem szállhatott fel.')

szamlalo = 0
id = 0
allomasok = []
for i in range(len(allomas)-1):
    if allomas[i] == allomas[i+1]:
        szamlalo += 1
        id = allomas[i]
    elif allomas[i] != allomas[i+1]:
        allomasok.append(szamlalo)
        szamlalo = 0
print(allomasok)

max = allomasok[0]
max_id = 0
for i in range(len(allomasok)):
    if allomasok[i] > max:
        max = allomasok[i]
        max_id = i
print(f'A legtöbb utas ({max} fő) a {max_id}. megállóban próbált felszállni.')
