class imdb:
    def __init__(self, ev: int, idotartam: int, ertekeles: float, rendezo: str, bevetel: int, cim: str):
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
    filmek.append(imdb(ev=int(adat[0]), idotartam=int(adat[1]), ertekeles=float(adat[2]), rendezo=adat[3], bevetel=int(adat[4]), cim=adat[5]))
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
for i in range(len(filmek)):
    if filmek[i].ertekeles > 9:
        print('Van olyan film ami 9-es értékelésnél magasabb pontszámot kapott.')
        break
    else:
        print('Nincs olyan film ami 9-es értékelésnél magasabb pontszámot kapott.')
#5. feladat
legmagasabb = filmek[0].ertekeles
for i in range(len(filmek)):
    if filmek[i].ertekeles > legmagasabb:
        legmagasabb = filmek[i].ertekeles
print(f'A legmagasabb értékelés {legmagasabb}')
#6.feladat
# 1. lehetőség: tudjuk hogy 0..10
def hany_darab(pont):
    ennyi_pontos = 0
    for i in range(len(filmek)):
        if filmek[i].ertekeles == pont:
            ennyi_pontos += 1
    return ennyi_pontos


for pont in range(100):
    if hany_darab(...) > 0:
        print(f'{pont / 10} pontot kapott {hany_darab(pont/10)} film')

# 2. lehetőség
ertekelesek = list(set([film.ertekeles for film in filmek]))
ertekelesek.sort()
for pont in ertekelesek:
    print(f'{pont} pontot kapott {hany_darab(pont)} film')

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