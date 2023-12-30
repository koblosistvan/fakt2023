forras = open('kozut.txt')
forras.readline()

ido = []
rendszam = []
sebesseg = []

for sor in forras:
    adat = sor.strip().split()
    egyautideje = [adat[0], adat[1], adat[2]]
    ido.append(egyautideje)
    sebesseg.append(int(adat[3]))
    rendszam.append(adat[4])
print(ido)
print(rendszam)
print(sebesseg)

forras.close()

print(f'A kozut.txt fájlból beolvastam {len(rendszam)} sort.')


#1.feladat
tobbelment50 = 0
for i in range(len(sebesseg)):
    if sebesseg[i] > 50:
        tobbelment50 += 1
print('1. feladat')
print(f'{tobbelment50} autó ment gyorsabban a megengedett 50 km/h-nál.')

#2.feladat,
print('2. feladat')
for i in range(len(sebesseg)):
    if sebesseg[i] > 55:
        print('Igen volt 55 km/h-nál gyorsabb autó.')
        break
    else:
        print('Nem volt 55 km/h-nál gyorsabb autó.')

#3.feladat
print('3.feladat')

leggyorsabb = sebesseg[0]
leggyorsabb_id = rendszam[0]
for i in range(len(sebesseg)):
    if sebesseg[i] > leggyorsabb:
        leggyorsabb = sebesseg[i]
        leggyorsabb_id = rendszam[i]

print(f'A leggyorsabb autó rendszáma: {leggyorsabb_id}, {leggyorsabb} km/h sebességgel ment.')

#4.feladat
osszes_seb = 0
for i in range(len(sebesseg)):
    osszes_seb += sebesseg[i]

atlag = osszes_seb // len(sebesseg)
print('4.feladat')
print(f'Az áthaladó autók átlagsebessége {atlag} km/h volt.')

#5.feladat
kimenet = open('kozut-kimenet', mode='w', encoding='utf-8')

lassabbak_seb = []
lassabbak_rendsz = []
lassabbak_ido = []
for i in range(len(sebesseg)):
    if sebesseg[i] < 30:
        lassabbak_seb.append(sebesseg[i])
        lassabbak_rendsz.append(rendszam[i])
        lassabbak_ido.append(ido[i])
#asd
