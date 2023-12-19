forras = open('imdb.txt', mode='r', encoding='utf-8')
filmek = []
datum = []
idotartam = []
ertekeles = []
rendezo = []
forras.readline()
for i in forras:
    sor = i.strip('').split('\t')
    filmek.append(sor[5])
    datum.append(sor[0])
    idotartam.append(int(sor[1]))
    ertekeles.append(float(sor[2]))
    rendezo.append(sor[3])
#1
print(len(filmek))

#2
print(datum[0])

#3
hosszabb = 0
for i in range(len(idotartam)):
    if idotartam[i] > 2:
        hosszabb += 1
if hosszabb == 0:
    print('Nincs ilyen film')
else:
    print(hosszabb)

#4
van = False
for i in range(len(ertekeles)):
    if ertekeles[i] > 9:
        van = True
if van:
    print('Van')

#5
legjobb = max(ertekeles)
for i in range(len(rendezo)):
    if ertekeles[i] == legjobb:
        print(rendezo[i])

#6
bekert = input(':')
a = bekert.split(' ')
vezeteknev = a[0]
f = open(f'{vezeteknev}.txt', 'w')
for i in range(rendezo):
    if rendezo == bekert:
        f.write(filmek[i])

#7
a = 1900
for i in range(1900, 2030):
    if datum[i] == a
