forras = open("jel.txt", mode='r', encoding='utf-8')

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

print("2. feladat")
sorszam = int(input("Adja meg a jel sorszámát! "))
print(f'x={x_koordinata[sorszam-1]}, y={y_koordinata[sorszam-1]}')

def eltelt(ora1, perc1, masodperc1, ora2, perc2, masodperc2):
    return (ora2*3600+perc2*60+masodperc2)-(ora1*3600+perc1*60+masodperc1)

print("4. feladat")
masodperc_4f = eltelt(ora[0], perc[0], masodperc[0], ora[-1], perc[-1], masodperc[-1])
ido_o = int(masodperc_4f/3600)
ido_p = int((masodperc_4f-(int(masodperc_4f/3600)*3600))/60)
ido_m = masodperc_4f-((int((masodperc_4f-(int(masodperc_4f/3600)*3600))/60)*60)+(int(masodperc_4f/3600)*3600))
print(f'Időtartam: {ido_o}:{ido_p}:{ido_m}')

print("5. feladat")
print(f'Bal alsó: {min(x_koordinata)} {min(y_koordinata)}, jobb felső: {max(x_koordinata)} {max(y_koordinata)}')

kimenet = open("kimaradt.txt", mode='w', encoding='utf-8')

kimenet.close()