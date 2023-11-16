forras = open('kerekparverseny.txt', mode='r', encoding='utf-8')


elsosor = forras.readline().strip().split(' ')

varosokszama = int(elsosor[0])

versenyhossz = int(elsosor[1])

varosoktav = []

for sor in forras:
    adat = sor.strip().split(' ')
    varosoktav.append(sor.strip())

tavok = set(varosoktav)

ketvarostav = tavok[i]-tavok[i-1]

for i in range(len(varosoktav)):
    if tavok[i]+tavok[i+1]+tavok[i+2] or tavok[]