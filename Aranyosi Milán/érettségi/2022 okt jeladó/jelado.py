import math

forras = open('jel.txt', mode='r', encoding='utf-8')

ora = []
perc = []
masodperc = []
x_koordinata = []
y_koordinata = []

for sor in forras:
    adat = sor.strip().split(' ')
    ora.append(int(adat[0]))
    perc.append(int(adat[1]))
    masodperc.append(int(adat[2]))
    x_koordinata.append(int(adat[3]))
    y_koordinata.append(int(adat[4]))

forras.close()

print('2. feladat')
adott_sorszam = int(input('Adja meg a jel sorszámát! '))-1
print(f'x={x_koordinata[adott_sorszam]} y={y_koordinata[adott_sorszam]}')

def eltelt(ora, perc, masodperc, ora2, perc2, masodperc2):
    elsoido = ora * 3600 + perc * 60 + masodperc
    masodikido = ora2 * 3600 + perc2 * 60 + masodperc2
    return masodikido-elsoido

print('\n4. feladat')
eltelt_ido = eltelt(ora[0], perc[0], masodperc[0], ora[-1], perc[-1], masodperc[-1])
eltelt_ora = eltelt_ido // 3600

eltelt_perc = (eltelt_ido % 3600) // 60
eltelt_masodperc = eltelt_ido % 60

print(f'{eltelt_ora}:{eltelt_perc}:{eltelt_masodperc}')

print('\n5. feladat')

print(f'Bal alsó: {min(x_koordinata)} {min(y_koordinata)}, jobb felső: {max(x_koordinata)} {max(y_koordinata)}')

print('\n6. feladat')
def elmozdulas(adottx, kovix, adotty, koviy):
    eredmeny = math.sqrt(((adottx-kovix)*(adottx-kovix))+((adotty-koviy)*(adotty-koviy)))
    return eredmeny

osszes_elmozdulas = 0

for i in range(len(x_koordinata)-1):
    osszes_elmozdulas += elmozdulas(x_koordinata[i], x_koordinata[i+1], y_koordinata[i], y_koordinata[i+1])

print(f'Elmozdulás: {osszes_elmozdulas:.3f} egység')

#7.feladat
kimenet = open('kimaradt.txt', mode='w', encoding='utf-8')

ido_elteres_erteke = 0
koordinata_elteres_erteke = 0

for i in range(len(x_koordinata)-1):

    ido_elteres_erteke = 0
    koordinata_elteres_erteke = 0

    ido_elteres = eltelt(ora[i], perc[i], masodperc[i], ora[i+1], perc[i+1], masodperc[i+1])

    if ido_elteres > 300:
        ido_elteres_erteke = (ido_elteres-300) // 300

    x_koordinata_elteres = abs(x_koordinata[i] - x_koordinata[i+1])
    y_koordinata_elteres = abs(y_koordinata[i] - y_koordinata[i+1])

    if x_koordinata_elteres > y_koordinata_elteres:
        koordinata_elteres_erteke = (x_koordinata_elteres-10) // 10
    else:
        koordinata_elteres_erteke = (y_koordinata_elteres-10) // 10

    if ido_elteres_erteke > 0 or koordinata_elteres_erteke > 0:
        if ido_elteres_erteke > koordinata_elteres_erteke:
            print(f'{ora[i+1]} {perc[i+1]} {masodperc[i+1]} időeltérés {ido_elteres_erteke}', file=kimenet)
        else:
            print(f'{ora[i + 1]} {perc[i + 1]} {masodperc[i + 1]} koordinata-eltérés {koordinata_elteres_erteke}', file=kimenet)

kimenet.close()