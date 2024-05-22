class imdb:
    def __init__(self, ev, ido, ertekeles, rendezo, bevetel, cim):
        self.ev=ev
        self.ido=ido
        self.ertekeles=ertekeles
        self.rendezo=rendezo
        self.bevetel=bevetel
        self.cim=cim


forras=open('imdb.txt')

forras.readline()

filmek=[]

for sor in forras:
    adat=sor.strip().split('\t')
    filmek.append(imdb(ev=int(adat[0]), ido=int(adat[1]), ertekeles=float(adat[2]), rendezo=(adat[3]), bevetel=(adat[4]), cim=(adat[5])))
forras.close()

#1. feladat

print(len(filmek), 'film van az állományban')

#2. feladat


#3. feladat

hosszabb = 0

for i in range(len(filmek)):
    if filmek[i].ido > 120:
        hosszabb +=1
    if hosszabb == 0:
        print('Nincs 2 oránál hosszabb film')
print(hosszabb,'film van ami hosszabb mint 2 óra')

#4. feladat
ertszaml=0

for i in range(len(filmek)):
    if filmek[i].ertekeles  > 9.00:
        ertszaml+=1
    if ertszaml==0:
        print('Nincs olyan film ami 9 nél jobb értékelést kapott')

print(ertszaml,'film ami 9-nél jobb értékelést kapott')

#5. feladat


filmek[i].ertekeles

