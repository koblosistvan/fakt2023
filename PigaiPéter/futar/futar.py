forras = open('futar.txt', mode='r', encoding='utf-8')
napok = []
fuvarszam = []
km = []
forras.readline()
for i in forras:
    a = i.strip().split(' ')
    napok.append(int(a[0]))
    fuvarszam.append(int(a[1]))
    km.append(int(a[2]))

# 1
leghoszabb = 0
for i in range(len(km)):
    if km[i] > leghoszabb:
        leghoszabb = km[i]
print(napok[km.index(leghoszabb)], fuvarszam[km.index(leghoszabb)], leghoszabb)

# 2
ossz = 0
for i in range(len(km)):
    if napok[i] == 3:
        ossz += km[i]
print(ossz)

# 3
telsesitett = 0
for i in range(len(fuvarszam)):
    if napok[i] == 4:
        if telsesitett < fuvarszam[i]:
            telsesitett = fuvarszam[i]
print(telsesitett)

# 4
volt = False
for i in range(len(km)):
    if km[i] > 20:
        volt = True
print(volt)

# 5
kiirt = open('futar-kimenet.txt', 'w')
a = 0
for i in range(len(fuvarszam)):
    sor = []
    if fuvarszam[i] == 1:
        sor.append(str(napok[i]))
        sor.append(str(fuvarszam[i]))
        sor.append(str(km[i]))
        sor.append('\n')
        sor = " ".join(sor)
        kiirt.write(sor)
