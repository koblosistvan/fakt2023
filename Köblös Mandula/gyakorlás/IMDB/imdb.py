class imdb:
    def __init__(self, ev: int, idotartam: int, ertekeles: str, rendezo: str, bevetel: int, cim: str):
        self.ev = ev
        self.idotartam = idotartam
        self.ertekeles = ertekeles
        self.rendezo = rendezo
        self.bevetel = bevetel
        self.cim = cim
        self.idotartam_ora = idotartam/60

filmek = []
forras = open('imdb.txt', mode='r', encoding='utf-8')
forras.readline()
for sor in forras:
    adat = sor.strip().split('\t')
    filmek.append(imdb(ev=int(adat[0]), idotartam=int(adat[1]), ertekeles=adat[2], rendezo=adat[3], bevetel=int(adat[4]), cim=adat[5]))
forras.close()


#1. feladat
print(f'{len(filmek)} film adatai vannak az állományban.')

#2. feladat
elso_film = filmek[0].ev
for i in range(len(filmek)):
    if filmek[i].ev < elso_film:
        elso_film = filmek[i].ev
print(f'Az első film {elso_film}-ben jelent meg.')

#3. feladat
hosszabb_2ora = 0
for i in range(len(filmek)):
    if filmek[i].idotartam_ora > 2:
        hosszabb_2ora += 1
if hosszabb_2ora > 1:
    print(f'{hosszabb_2ora} film hosszabb mint 2 óra.')
else:
    print(f'Nincs két óránál hosszabb film.')

#4. feladat

#5. feladat

#6.feladat

#7. feladat

#8. feladat
rendezo = input("Melyik rendező filmei érdekelnek? ")
for i in range(len(filmek)):
    if filmek[i].rendezo == rendezo:
        print(filmek[i].cim)

#9. feladat

#10. feladat
atlagos_bevetel = 0
for i in range(len(filmek)):
    atlagos_bevetel += filmek[i].bevetel
print(f'Az átlagos bevétele egy filmnek {atlagos_bevetel/len(filmek)} USD.')