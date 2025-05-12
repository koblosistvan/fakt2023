# 1
forras1 = open('dobasok1.txt', 'r')
forras2 = open('osvenyek.txt', 'r', encoding='utf-8')
dobasok = []
osvenyek = []
for sor in forras1:
    i = sor.strip().split(' ')
    for k in i:
        dobasok.append(int(k))
forras1.close()
for sor in forras2:
    i = sor.strip()
    osvenyek.append(i)
forras2.close()

# 2
print(f'2. feladat\n'
      f'A dobások száma: {len(dobasok)}\n'
      f'Az ösvények száma: {len(osvenyek)}')

# 3
leghosszabb = len(osvenyek[0])
index3 = osvenyek.index(osvenyek[0])
for i in range(len(osvenyek)):
    if len(osvenyek[i]) > leghosszabb:
        leghosszabb = len(osvenyek[i])
        index3 = i
print(f'3. feladat\n'
      f'Az egyik leghosszabb a(z) {index3+1}. ösvény, hossza: {leghosszabb}')

# 4
print('4. feladat')
osveny = int(input('Adja meg egy ösvény sorszámát! '))
jatekosok_szama = int(input('Adja meg a játékosok számát! '))

# 5
m = osvenyek[osveny-1].count('M')
v = osvenyek[osveny-1].count('V')
e = osvenyek[osveny-1].count('E')
print('5. feladat')
if m:
    print(f'M: {m} darab')
if v:
    print(f'V: {v} darab')
if e:
    print(f'E: {e} darab')

# 6
kimenet = open('kulonleges.txt', 'w', encoding='utf-8')
for i in range(len(osvenyek[osveny])):
    if osvenyek[osveny][i] != 'M':
        print(f'{i+1}\t{osvenyek[osveny][i]}', file=kimenet)
kimenet.close()

# 7
eredmeny_jatekosonkent = [len(osvenyek[osveny])]*jatekosok_szama
futtatasindex7 = -1
jatekosindex7 = []
for i in range(len(dobasok)):
    for k in range(len(eredmeny_jatekosonkent)):
        if (i+1) % jatekosok_szama == (k+1):
            eredmeny_jatekosonkent[k] -= dobasok[i]
        elif (i+1) % jatekosok_szama == 0 and k+1 == len(eredmeny_jatekosonkent):
            eredmeny_jatekosonkent[k] -= dobasok[i]
            if eredmeny_jatekosonkent[k] < 0 and k+1 not in jatekosindex7:
                jatekosindex7.append(k+1)
                if futtatasindex7 < 0:
                    futtatasindex7 = int(i/jatekosok_szama)+1
print(f'7. feladat\n'
      f'A játék a(z) {futtatasindex7+1}. körben fejeződött be. A legtávolabb jutó(k) sorszáma:', end=' ')
print(*jatekosindex7)

# 8
eredmeny_jatekosonkent = [len(osvenyek[osveny])]*jatekosok_szama
futtatasindex8 = -1
jatekosindex8 = []
for i in range(len(dobasok)):
    for k in range(len(eredmeny_jatekosonkent)):
        if i > futtatasindex8:
            break
        elif (i+1) % jatekosok_szama == 0 and k+1 == len(eredmeny_jatekosonkent):
            eredmeny_jatekosonkent[k] -= dobasok[i]
            if eredmeny_jatekosonkent[k] < 0 and k+1 not in jatekosindex8:
                jatekosindex8.append(k+1)
                if futtatasindex8 < 0:
                    futtatasindex8 = i
print(f'8. feladat\n'
      f'Nyertes(ek): {jatekosindex8}\n'
      f'A többiek pozíciója:')
for i in range(len(eredmeny_jatekosonkent)):
    print(f'{i+1}. játékos, {len(osvenyek[osveny])-eredmeny_jatekosonkent[i]}. mező')




"""
8. feladat
Nyertes(ek): 4 5
A többiek pozíciója:
1. játékos, 153. mező
2. játékos, 185. mező
3. játékos, 183. mező"""