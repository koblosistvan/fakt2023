forras = open('kozut.txt', mode='r', encoding='utf-8')
autok_szama = forras.readline()
idopont = []
sebesseg = []
rendszam = []
for i in forras:
    adat = i.strip().split(' ')
    idopont.append(adat[:3])
    sebesseg.append(int(adat[3]))
    rendszam.append(adat[4])
forras.close()
#print(idopont, sebesseg, rendszam)

gyorsabb = 0
volte = 'Nem volt'
for i in sebesseg:
    if i > 50:
        gyorsabb += 1
        if i > 55:
            volte = 'Volt'
print(f'1. feladat:\n{gyorsabb} autó volt gyorsabb a megegedett 50km/h sebességnél.\n')
print(f'2. feladat:\n{volte} olyan autó, ami gyorsabban ment 55 km/h-nál.\n')

leggyorsabb = 0
for i in range(len(sebesseg)):
    if sebesseg[i] > leggyorsabb:
        leggyorsabb = sebesseg[i]
        index_3 = i
print(f'3. feladat:\nA leggyorsabb autó rendszáma {rendszam[index_3]}, sebessége {leggyorsabb} km/h.\n')

atlag = 0
for i in sebesseg:
    atlag += i
atlag = atlag/len(sebesseg)
print(f'4. feladat:\nAz autók átlagsebessége {atlag} km/h volt.\n')

kimenet = open('kozut-kimenet.txt', mode='w', encoding='utf-8')
#for i in range(len(idopont)):
    #segedvaltozo = idopont[i].split(' ')
    #idopont[i] = ' '.join(segedvaltozo)
for i in rendszam:
    i = i.split('-')
print('30 km/h-nál lassabb járművek adatai:', file=kimenet)
for i in range(len(sebesseg)):
    if sebesseg[i] < 30:
        print(*(':'.join(idopont[i]), rendszam[i], sebesseg[i]), sep=' - ', file=kimenet)
kimenet_extra = open('kozut-rendezett.txt', mode='w', encoding='utf-8')
print('Szabálytalan gépkocsik:', file=kimenet_extra)
idopont_formazott = []
sebesseg_formazott = []
rendszam_formazott = []
for i in range(len(sebesseg)):
    if sebesseg[i] > 50:
        idopont_formazott.append(idopont[i])
        sebesseg_formazott.append(sebesseg[i])
        rendszam_formazott.append(rendszam[i])
#for i in range(len(rendszam_formazott)):
    #if rendszam[i]
