forras1 = open('dobasok.txt', mode='r', encoding='utf-8')

forras2 = open('osvenyek.txt', mode='r', encoding='utf-8')

dobasok = []

for sor in forras1:
    lista = sor.split(' ')
    for szam in lista:
        dobasok.append(int(szam))

osvenyek = []
for sor in forras2:
    osvenyek.append(sor)

print(dobasok)
print(osvenyek)


print('2. feladat')
print(f'A dobások száma: {len(dobasok)}')
print(f'Az ösvények száma: {len(osvenyek)}')

print('3. feladat')

leghoszabb = len(osvenyek[1])
leghoszabb_i = 0

for i in range(len(osvenyek)):
    seged = len(osvenyek[i])
    if seged > leghoszabb:
        leghoszabb = seged
        leghoszabb_i = i

print(f'Az egyik leghosszabb a(z) {leghoszabb_i+1}. ösvény, hossza: {leghoszabb}')

print('4. feladat')
osvenyszam = int(input('Adja meg egy ösvény sorszámát!(szám)'))
jatekosszam = int(input('Adja meg a játékosok számát!(szám)'))

print('5. feladat')

m_szaml = 0
e_szaml = 0
v_szaml = 0

m_mezoi = []
e_mezoi = []
v_mezoi = []

sorszam = 0

for i in osvenyek[osvenyszam-1]:
    sorszam += 1
    if i == 'M':
        m_szaml += 1
        m_mezoi.append(sorszam)
    elif i == 'V':
        v_szaml += 1
        v_mezoi.append(sorszam)
    elif i == 'E':
        e_szaml += 1
        e_mezoi.append(sorszam)

if m_szaml > 0:
    print(f'M: {m_szaml} darab')
if e_szaml > 0:
    print(f'E: {e_szaml} darab')
if v_szaml > 0:
    print(f'V: {v_szaml} darab')

kimenet = open('kulonleges.txt', mode='w', encoding='utf-8')

for i in range(len(m_mezoi)):
    print(f'M\t{m_mezoi[i]}', file=kimenet)
for i in range(len(v_mezoi)):
    print(f'V\t{m_mezoi[i]}', file=kimenet)
for i in range(len(e_mezoi)):
    print(f'E\t{m_mezoi[i]}', file=kimenet)


print('7. feladat')
#A játék a(z) 54. körben fejeződött be. A legtávolabb jutó(k) sorszáma: 5
print('8. feladat')
#Nyertes(ek): 4 5
#A többiek pozíciója:
#1. játékos, 153. mező
#2. játékos, 185. mező
