# 1
forras = open('inf2022emeltokt/4_Jelado/jel.txt', 'r', encoding='utf-8')
ora = []
perc = []
mp = []
x_koordinata = []
y_koordinata = []
for i in forras:
    sor = i.strip().split(' ')
    ora.append(int(sor[0]))
    perc.append(int(sor[1]))
    mp.append(int(sor[2]))
    x_koordinata.append(int(sor[3]))
    y_koordinata.append(int(sor[4]))
forras.close()
orapercmp = []
for i in range(len(ora)):
    orapercmp.append(f'{ora[i]}:{perc[i]}:{mp[i]}')

# 2
sorszam = int(input('2. feladat\nAdja meg a jel sorszámát! '))
print(f'x={x_koordinata[sorszam-1]} y={y_koordinata[sorszam-1]}')

# 3

def eltelt(ido1, ido2):
    ido1mpben = ora[ido1]*3600 + perc[ido1]*60 + mp[ido1]
    ido2mpben = ora[ido2] * 3600 + perc[ido2] * 60 + mp[ido2]
    return abs(ido1mpben-ido2mpben)


# 4
elteltki = []
elteltelsotolutolso = eltelt(0, -1)
elteltki.append(str(int(elteltelsotolutolso/3600)))
elteltelsotolutolso -= int(elteltki[-1])*3600
elteltki.append(str(int(elteltelsotolutolso/60)))
elteltelsotolutolso -= int(elteltki[-1])*60
elteltki.append(str(int(elteltelsotolutolso)))
elteltelsotolutolso -= int(elteltki[-1])

print(f'4. feladat\n'
      f'Időtartam: {":".join(elteltki)}')

# 5
legkisebb_y = y_koordinata[0]
legnagyobb_y = y_koordinata[0]
legkisebb_x = x_koordinata[0]
legnagyobb_x = x_koordinata[0]
for i in range(len(y_koordinata)):
    if y_koordinata[i] < legkisebb_y:
        legkisebb_y = y_koordinata[i]
    elif y_koordinata[i] > legnagyobb_y:
        legnagyobb_y = y_koordinata[i]
    if x_koordinata[i] < legkisebb_x:
        legkisebb_x = x_koordinata[i]
    elif x_koordinata[i] > legnagyobb_x:
        legnagyobb_x = x_koordinata[i]
print(f'5. feladat\n'
      f'Bal alsó: {legkisebb_x} {legkisebb_y}, jobb felső: {legnagyobb_x} {legnagyobb_y}')

# 6
osszelmozdulas = 0
for i in range(len(x_koordinata)-1):
    segedvaltozo = (x_koordinata[i] - x_koordinata[i+1])**2 + (y_koordinata[i] - y_koordinata[i+1])**2
    segedvaltozo **= (1/2)
    osszelmozdulas += segedvaltozo
print(f'6. feladat\n'
      f'Elmozdulás: {round(osszelmozdulas, 3)} egység')

# 7
kimenet = open('kimaradt.txt', 'w', encoding='utf-8')
for i in range(len(x_koordinata)-1):
    xvaltozas = x_koordinata[i] - x_koordinata[i + 1]
    yvaltozas = y_koordinata[i] - y_koordinata[i + 1]
    if eltelt(i, i+1) > 5*60:
        print(f'{ora[i]} {perc[i]} {mp[i]} {"irőeltérés"} {int(eltelt(i, i+1)/(5*60))}', file=kimenet)
    elif abs(xvaltozas) > 10:
        print(f'{ora[i]} {perc[i]} {mp[i]} {"koordináta-eltérés"} {int(xvaltozas/10)}', file=kimenet)
    elif abs(yvaltozas) > 10:
        print(f'{ora[i]} {perc[i]} {mp[i]} {"koordináta-eltérés"} {int(yvaltozas/10)}', file=kimenet)

forras.close()


"""4 25 33 időeltérés 1
4 55 33 koordináta-eltérés 1"""

"""2. feladat
Adja meg a jel sorszámát! 3
x=126 y=639
4. feladat
Időtartam: 18:52:40
5. feladat
Bal alsó: 4 639, jobb felső: 147 727
6. feladat
Elmozdulás: 2007.677 egység"""