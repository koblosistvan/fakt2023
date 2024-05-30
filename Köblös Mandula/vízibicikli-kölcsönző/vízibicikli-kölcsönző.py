class Vizibicikli:
    def __init__(self, nev: str, jazon: str, eora: int, eperc: int, vora: int, vperc: int):
        self.nev = nev
        self.jazon = jazon
        self.eora = eora
        self.eperc = eperc
        self.vora = vora
        self.vperc = vperc
        self.eosszperc = (eora*60) + eperc
        self.vosszperc = (vora*60) + vperc

kolcsonzesek = []
forrás = open('kolcsonzesek.txt', mode='r', encoding='utf-8')
forrás.readline()
for sor in forrás:
    adat = sor.strip().split(';')
    kolcsonzesek.append(Vizibicikli(nev=str(adat[0]), jazon=str(adat[1]), eora=int(adat[2]), eperc=int(adat[3]), vora=int(adat[4]), vperc=int(adat[5])))
forrás.close()

# 5. feladat
print(f'{len(kolcsonzesek)} kölcsönzés adatai találhatóak a forrásállományan.')

# 6. feladat
kolcsonzo = input("Kinek a kölcsönzésére vagy kíváncsi? ")
kolcsonzes_db = 0
for i in range(len(kolcsonzesek)):
    if kolcsonzesek[i].nev == kolcsonzo:
        kolcsonzes_db += 1
        print(f'{kolcsonzo} a mai nap {kolcsonzesek[i].eora}:{kolcsonzesek[i].eperc}-től {kolcsonzesek[i].vora}:{kolcsonzesek[i].eperc}-ig kölcsönzött.')
if kolcsonzes_db == 0:
    print("Nem volt ilyen nevű kölcsönző.")

# 7. feladat
idopont = input("Melyik időpontban? ")
ora, perc = idopont.split(':')
bekert_osszperc = (ora*60) + perc
for i in range(len(kolcsonzesek)):
    if bekert_osszperc > kolcsonzesek[i].eosszperc and bekert_osszperc < kolcsonzesek[i].vosszperc:
        print(f'{kolcsonzesek[i].jazon}, ')