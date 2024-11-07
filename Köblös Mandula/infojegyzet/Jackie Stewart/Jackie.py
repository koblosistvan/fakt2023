forras = open('jackie.txt', encoding='utf-8', mode='r')
forras.readline()
evek = []
versenyek = []
gyozelmek = []
dobogos = []
elsorol = []
leggyorsabb_kor = []

for sor in forras:
    adat = sor.strip().split('\t')
    evek.append(int(adat[0]))
    versenyek.append(int(adat[1]))
    gyozelmek.append(int(adat[2]))
    dobogos.append(int(adat[3]))
    elsorol.append(int(adat[4]))
    leggyorsabb_kor.append(int(adat[5]))
forras.close()

#3. feladat
print(f'3. feladat:{len(evek)}')

#4. feladat
legtobb_index = evek[0]
legtobb = versenyek[0]
for i in range(len(versenyek)):
    if versenyek[i] > legtobb:
        legtobb = versenyek[i]
        legtobb_index = evek[i]

print(f'4. feladat: {legtobb_index}')

#5. feladat
hatvanas = 0
hetvenes = 0
for i in range(len(evek)):
    if evek[i] >= 1970:
        hetvenes += gyozelmek[i]
    else:
        hatvanas += gyozelmek[i]

print(f'5. feladat \n\t 60-as évek: {hatvanas} \n\t 70-es évek: {hetvenes}')

# 6. feladat




