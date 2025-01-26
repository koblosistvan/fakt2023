# 1
forras = open('jel.txt', 'r', encoding='utf-8')
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

"""def eltelt(ido1, ido2):
    if orapercmp[ido1] < orapercmp[ido2]:
        orapercmp[ido1], orapercmp[ido2] = orapercmp[ido2], orapercmp[ido1]
    c = orapercmp[]
    percmod = perc[ido1]
    oramod = ora[ido1]
    mpmod = mp[ido1]
    elteltmp = 0
    elteltossz = [0]*3
    if mp[ido1] >= mp[ido2]:
        elteltmp += (mp[ido1]-mp[ido2])
        elteltossz[2] = str(mp[ido1]-mp[ido2])
    else:
        elteltmp += (60 + mp[ido1] - mp[ido2])
        elteltossz[2] = str(60 + mp[ido1] - mp[ido2])
        percmod -= 1
    b = perc[ido2]
    if percmod >= perc[ido2]:
        elteltmp += (percmod-mp[ido2])*60
        elteltossz[1] = str(percmod-mp[ido2])
    else:
        elteltmp += (60 + percmod - perc[ido2])
        elteltossz[1] = str(60 + percmod - perc[ido2])
        oramod -= 1

    elteltmp += (oramod-ora[ido2])*3600
    elteltossz[0] = str(oramod-ora[ido2])
    return f'{":".join(elteltossz)}'
print(eltelt(0, 1))


"""


"""2. feladat
Adja meg a jel sorszámát! 3
x=126 y=639
4. feladat
Időtartam: 18:52:40
5. feladat
Bal alsó: 4 639, jobb felső: 147 727
6. feladat
Elmozdulás: 2007.677 egység"""