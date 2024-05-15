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
    if i.ev < legelso:
        legelso = i.ev
print(f'Az első film kiadási éve {legelso}.')

# 3.
feladat()
print(f'{len([i for i in records if i.idotartam>120])} olyan film van, ami két óránál hosszabb.')

# 4.
feladat()
