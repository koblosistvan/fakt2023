class Filmek:
    def __init__(self, ev: int, idotartam: int, ertekeles: float, rendezo: str, bevetel: int, cim: str):
        self.ev = ev
        self.idotartam = idotartam
        self.ertekeles = ertekeles
        self.rendezo = rendezo
        self.bevetel = bevetel
        self.cim = cim


forras = open('PigaiPéter\\imdb.txt', mode='r', encoding='utf-8')
imdb = []
forras.readline()
for sor in forras:
    adat = sor.strip().split('\t')
    imdb.append(Filmek(ev=int(adat[0]), idotartam=int(adat[1]), ertekeles=float(adat[2]), rendezo=str(adat[3]), bevetel=int(adat[4]), cim=str(adat[5])))
forras.close

#1
print(f'{len(imdb)} van összesen')

#2
legkisebb = imdb[0].ev
for i in imdb:
    if legkisebb > i.ev:
        legkisebb = i.ev
print(f'{legkisebb} évben jött ki a legrégebbi film')

#
hoszabb = 0
for i in imdb:
    if i.idotartam > 120:
        hoszabb += 1
if hoszabb == 0:
    print('Nincs két óránál hosszabb film.')
else:
    print(f'{hoszabb} db 2 óránál hoszabb film van')

#
van = False
for i in imdb:
    if i.ertekeles > 9:
        van = True
        break
if van == True:
    print('Van 9-es értékelésnél magasabb film')
else:
    print('Nincs 9-es értékelésnél magasabb film')

#
legmagasabb = imdb[0].ertekeles
for i in imdb:
    if i.ertekeles > legmagasabb:
        legmagasabb = i.ertekeles
print(f'A legmagasabb értékeles:{legmagasabb}')

#
ertekelesek = set()
ratings = []
for i in range(len(imdb)):
        ertekelesek.add(imdb[i].ertekeles)
        ratings.append(imdb[i].ertekeles)
ertekelesek = sorted(list(ertekelesek))
for i in range(len(ertekelesek)):
    print(f'{ertekelesek[i]} értékelésből {ratings.count(ertekelesek[i])} db van')

#
legjobb = imdb[0].ertekeles
index = 0
for i in imdb:
    if i.ertekeles > legjobb:
        legjobb = i.ertekeles
        index = i
print(f'A legjobb filmet {imdb[index].rendezo} írta')

#
bekertr = input('Adj meg egy rendezőt:')
rfilm = []
for i in imdb:
    if i.rendezo == bekertr:
        rfilm.append(str(i.cim))
        rfilm.append(' (')
        rfilm.append(str(i.ev))
        rfilm.append(') - ')
        rfilm.append(str(i.idotartam))
        rfilm.append(' perc\n')
rfilm = ''.join(rfilm)
rnev = bekertr.split(' ')
f = open(f'PigaiPéter\\{rnev[1]}', 'w')
f.write(rfilm)

#

    
