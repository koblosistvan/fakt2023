forras=open('szallit.txt', mode='r', encoding='utf-8')

oszlop1=[]
oszlop2=[]
oszlop3=[]
oszlop4=[]

forras.readline()


elso_sor = forras.readline().strip().split(' ')
szalaghossz = int(elso_sor[0])
egyseg_ido = int(elso_sor[1])


for sor in forras:
    adat=sor.strip().split(' ')
    oszlop1.append(int(adat[0]))
    oszlop2.append(int(adat[1]))
    oszlop3.append(int(adat[2]))
    oszlop4.append(int(adat[3]))


forras.close()


#2.feladat
for i in range(len(oszlop1)):
    beker = int(input('Add meg a szállítás sorszámát: '))-1
    print(f'{oszlop2[beker]} indulással {oszlop3[beker]} célhellyel')
    break
#3.feladat
def tav(szalaghossz, indulashelye, erkezeshelye):
    if erkezeshelye >= indulashelye:
        return erkezeshelye - indulashelye
    else:
        return szalaghossz - indulashelye + erkezeshelye

max_tav = 0
max_sorszamok = []

for i in range(len(oszlop1)):
    tavolsag = tav(szalaghossz, oszlop2[i], oszlop3[i])
    if tavolsag > max_tav:
        max_tav = tavolsag
        max_sorszamok = [i + 1]
    elif tavolsag == max_tav:
        max_sorszamok.append(i + 1)

print(f"A legnagyobb távolság: {max_tav}")
print(f"A maximális távolságú szállítások sorszáma: {' '.join(map(str, max_sorszamok))}")

ossztomeg = 0

for i in range(len(oszlop1)):
    if oszlop2[i] != 0 and oszlop3[i] != 0 and (oszlop2[i] > oszlop3[i] or oszlop3[i] == 0):
        ossztomeg += oszlop4[i]

print(f"A kezdőpont előtt elhaladó rekeszek össztömege: {ossztomeg}")

egyseg_ido = 3  # Ezt szintén az első sorból olvasod
idopont = int(input("Adja meg a kívánt időpontot: "))
aktiv_rekeszek = []

for i in range(len(oszlop1)):
    indulas = oszlop1[i]
    erkezes = indulas + tav(szalaghossz, oszlop2[i], oszlop3[i]) * egyseg_ido
    if indulas <= idopont < erkezes:
        aktiv_rekeszek.append(i + 1)

if aktiv_rekeszek:
    print(f"A szállított rekeszek halmaza: {' '.join(map(str, aktiv_rekeszek))}")
else:
    print("üres")

tomeg_map = {}

for i in range(len(oszlop1)):
    indulo = oszlop2[i]
    tomeg = oszlop4[i]
    if indulo in tomeg_map:
        tomeg_map[indulo] += tomeg
    else:
        tomeg_map[indulo] = tomeg

with open("tomeg.txt", "w") as f:
    for hely, tomeg in tomeg_map.items():
        f.write(f"{hely} {tomeg}\\n")
