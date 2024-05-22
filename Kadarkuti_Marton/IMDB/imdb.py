feladat_count = 0

def feladat():
    global feladat_count
    print('')
    print('-'*30)
    print('')
    feladat_count+= 1
    print(f'#{feladat_count}. feladat:')

class Record:
    def __init__(self, ev, idotartam, ertekeles, rendezo, bevetel, cim):
        self.ev = ev
        self.idotartam = idotartam
        self.ertekeles = ertekeles
        self.rendezo = rendezo
        self.bevetel = bevetel
        self.cim = cim

records = []

with open('Kadarkuti_Marton\\IMDB\\imdb.txt','r',encoding='utf-8') as f:
    f.readline()
    for sor in f:
        adat = sor.strip().split('\t')
        records.append( Record(int(adat[0]), int(adat[1]), float(adat[2]), adat[3], int(adat[4]), adat[5]) )

# 1.
feladat()
print(f'{len(records)} film adatai vannak az adatbázisban.')

# 2.
feladat()
legelso = 10000
for i in records:
    if (i.ev < legelso):
        legelso = i.ev
print(f'Az első film kiadási éve {legelso}.')

# 3.
feladat()
print(f'{len([i for i in records if i.idotartam>120])} olyan film van, ami két óránál hosszabb.')

# 4.
feladat()
negyes_feladat = False
for i in records:
    if (i.ertekeles > 9):
        negyes_feladat = True
        break
negyes_feladat = ('Van' if negyes_feladat else 'Nincsen')
print(f'{negyes_feladat} olyan film, ami 9-es értékelésnél magasabbat pontszámot kapott.')

# 5.
feladat()
ertekelesek_list = [i.ertekeles for i in records]
print(f'A legmagasabb értékelés {max(ertekelesek_list)} pontszám.')

# 6.
feladat()
ertekelesek = sorted(list(set([i.ertekeles for i in records])))
ertekelesek_darab = []

for i in range(len(ertekelesek)):
    ertekelesek_darab.append( len( [1 for j in records if (j.ertekeles == ertekelesek[i]) ]) )

for i in range(len(ertekelesek)):
    print(f'{ertekelesek_darab[i]} film van {ertekelesek[i]} pontszámmal.')


# 7.
feladat()
legmagasabb_rendezo = records[ertekelesek_list.index(max(ertekelesek_list))].rendezo
print(f'A legmagasabb értékelést kapott film rendezője {legmagasabb_rendezo}')

# 8.
feladat()
while True:
    print("Rendező?")
    prompt = input("> ")
    if bool(prompt):
        break
results = [i.cim for i in records if (i.rendezo == prompt)]
if (len(results) == 0):
    print("Nincs ilyen rendező az adatbázisban")
else:
    print(f"Ezeket rendezte {prompt}:")
    for i in range(len(results)):
        print(results[i])

# 9.
feladat()
# ROSSZ
evek = sorted(list(set([i.ev for i in records])))
evek_data = [[0,0]]*len(evek) # [darabszám, bevétel]
print(evek_data)
for i in range(len(evek)):
    for record in records:
        if (record.ev == evek[i]):
            evek_data[i][0] += 1
            evek_data[i][1] += record.bevetel
print(evek_data)