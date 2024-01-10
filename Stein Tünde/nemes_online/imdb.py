forras = open('imdb.txt', mode='r', encoding='utf-8')
forras.readline()
ev = []
idotartam = []
ertekeles = []
rendezo = []
bevetel = []
cim = []
for sor in forras:
    ev.append(sor.strip().split('\t')[0])
    segedvaltozo = sor.strip().split('\t')[1]
    idotartam.append(int(segedvaltozo))
    segedvaltozo = sor.strip().split('\t')[2]
    ertekeles.append(float(segedvaltozo))
    rendezo.append(sor.strip().split('\t')[3])
    segedvaltozo = sor.strip().split('\t')[4]
    bevetel.append(int(segedvaltozo))
    cim.append(sor.strip().split('\t')[5])
forras.close()

print(f'1. feladat:\nAz állomány {len(ev)} adatot tartalmaz.\n')

print(f'2. feladat\nAz első film a listában a(z) {ev[0]}. évben jelent meg.\n')
#print(f'2. feladat\nAz első megjelent film az {max(ev)}. évben jelent meg.')

hosszabb2oranal = 0
for i in idotartam:
    if i/60 > 2:
        hosszabb2oranal += 1
if bool(hosszabb2oranal):
    print(f'3. feladat\n{hosszabb2oranal} két óránál hosszabb film van.\n')
else:
    print('3. feladat\nNincs két óránál hosszabb film.\n')

nagyobb9 = 0
for i in ertekeles:
    if i > 9:
        nagyobb9 += 1
if bool(nagyobb9):
    print(f'4. feladat\nVan 9-esnél magasabb értékelés.\n')
else:
    print('4. feladat\nNincs 9-esnél magasabb értékelés.\n')

#legjobb_ertekelesek = []
legjobb_erteke = 0
indexek_5 = []
for i in range(len(ertekeles)):
    if ertekeles[i] > legjobb_erteke:
        legjobb_erteke = ertekeles[i]
        index_5 = i
if ertekeles.count(legjobb_erteke) > 1:
    for i in range(len(ertekeles)):
        if ertekeles[i] == legjobb_erteke:
            #legjobb_ertekelesek.append(ertekeles[i])
            indexek_5.append(i)
    print('5. feladat\A legjobb értékelést kapott filmek:')
    for i in range(len(indexek_5)):
        print(f'{cim[indexek_5]} ({rendezo[indexek_5]})')
else:
    print(f'5. feladat\nA legjobb értékelést kapott film:\n{cim[index_5]} ({rendezo[index_5]})')

bekert_redezo = input('6. feladat\nAdj meg egy rendezőt: ')
vezeteknev = bekert_redezo.split(' ')[1]
indexek_6 = []
if bekert_redezo in rendezo:
    for i in range(len(rendezo)):
        if rendezo[i] == bekert_redezo:
            indexek_6.append(i)
    kimenet = open(f'{vezeteknev}.txt', mode='w', encoding='utf-8')
    for k in indexek_6:
        print(f'{cim[k]}', file=kimenet)
    print('\n')
else:
    print('Az adatbázisban nem megtalálható vagy helytelen nevet adott meg.\n')

evszamok = sorted(list(set(ev)))
print('7. feladat')
for k in range(len(evszamok)):
    osszbevetel = 0
    for i in range(len(ev)):
        if ev[i] == evszamok[k]:
            osszbevetel += bevetel[i]
    print(f'{evszamok[k]}\t {ev.count(evszamok[k])} darab\t{osszbevetel/1000000} millió USD.')
