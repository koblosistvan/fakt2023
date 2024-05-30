okm = open('Bogdán_Samu\órai\okm\okm.txt', 'r', encoding='utf-8')

azon = []
Spont1 = []
Sszint1 = []
Spont2 = []
Sszint2 = []
Spont3 = []
Sszint3 = []
Mpont1 = []
Mszint1 = []
Mpont2 = []
Mszint2 = []
Mpont3 = []
Mszint3 = []

for i in okm:
    sor = i.strip().split('\t')
    for j in range(len(sor)):
        if sor[j] == 'Nincs':
            sor[j] = 0
    azon.append(sor[0])
    Spont1.append(int(sor[1]))
    Sszint1.append(int(sor[2]))
    Spont2.append(int(sor[3]))
    Sszint2.append(int(sor[4]))
    Spont3.append(int(sor[5]))
    Sszint3.append(int(sor[6]))
    Mpont1.append(int(sor[7]))
    Mszint1.append(int(sor[8]))
    Mpont2.append(int(sor[9]))
    Mszint2.append(int(sor[10]))
    Mpont3.append(int(sor[11]))
    Mszint3.append(int(sor[12]))

print('\n'+'> 1. feladat'+'\n'+'> Adatok beolvasva')

print('\n'+'> 2. feladat'+'\n'+f'> {len(set(azon))} diák eredményei vannak a fájlban')

print('\n'+'> 3. feladat'+'\n'+f'> {azon[Spont3.index(max(Spont3))]} azonosítójú diáknak a legmagasabb az idei szövegértési pontszáma')

print('\n'+'> 4. feladat')
x = 0
for i in range(len(azon)):
    if (Spont2 != 0) and (Spont3 != 0) and (Spont2 != Spont3):
        x += 1
print(f'> {x} diáknak változott a szövegértés pontszáma az előzetes eredményéhez képest')

print('\n')
