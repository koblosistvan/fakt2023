class Imdb:
    def __init__(self, ev, ido, ertekeles, rendezo, bevetel, cim):
        self.ev = ev
        self.ido = ido
        self.ertekeles = ertekeles
        self.rendezo = rendezo
        self.bevetel = bevetel
        self.cim = cim


filmek = []
forras = open('imdb', encoding='utf-8', mode='r')
forras.readline()
for sor in forras:
    adat = sor.strip().split('\t')
    filmek.append(Imdb(ev=int(adat[0]), ido=int(adat[1]), ertekeles=float(adat[2]), rendezo=adat[3], bevetel=int(adat[4]), cim=adat[5]))
forras.close()

#1.feladat
print(f'{len(filmek)} film adatai vannak az állományban.')

#2. feladat
legkorabbi = filmek[0].ev
for i in range(len(filmek)):
    if filmek[i].ev < legkorabbi:
        legkorabbi = filmek[i].ev
print(f'Az első film megjelenési éve: {legkorabbi}')

#3.feladat
szamlalo = 0
for i in range(len(filmek)):
    if filmek[i].ido > 120:
        szamlalo += 1

if szamlalo == 0:
    print('Nincs ilyen film.')
else:
    print(f'{szamlalo} film tart tovább 2 óránál.')

#4.feladat
for i in range(len(filmek)):
    if filmek[i].ertekeles > 9:
        print('Van ilyen film.')
        break
    else:
        print('Nincs ilyen film.')

#5.feladat
legmagasabb = filmek[0].ertekeles
for i in range(len(filmek)):
    if filmek[i].ertekeles > legmagasabb:
        legmagasabb = filmek[i].ertekeles
print(f'A legmagasabb értékelésű film értékelése: {legmagasabb}')
