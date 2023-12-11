forras = open('kerekparverseny.txt', mode='r', encoding='utf-8')


elsosor = forras.readline().strip().split(' ')

varosokszama = int(elsosor[0])

versenyhossz = int(elsosor[1])

varosoktav = []

for sor in forras:
    adat = sor.strip().split(' ')
    varosoktav.append(sor.strip())

van = False

ketvarostav = varosoktav[i]-[i-1]

for i in range(len(varosoktav)):
    if varosoktav[i]+varosoktav[i + 1]+varosoktav[i + 2] or varosoktav[i + 1]+varosoktav[i + 2]+varosoktav[i + 3] or varosoktav[i + 2]+varosoktav[i + 3]+varosoktav[i + 4] or varosoktav[i + 3]+varosoktav[i + 4]+varosoktav[i + 5] or varosoktav[i + 3]+varosoktav[i + 4]+varosoktav[i + 5] or varosoktav[i + 4]+varosoktav[i + 5]+varosoktav[i + 6] or varosoktav[i + 5]+varosoktav[i + 6]+varosoktav[i + 7] or varosoktav[i + 6]+varosoktav[i + 7]+varosoktav[i + 8] or varosoktav[i + 7]+varosoktav[i + 8] == 50:
        van = True
        print(van)

