class vizibicikli:
    def __init__(self, nev, azonosito, elvora, elvperc, visszora, visszperc ):
        self.nev=nev
        self.azonosito=azonosito
        self.elvora=elvora
        self.elvperc=elvperc
        self.visszora=visszora
        self.visszperc=visszperc


kolcsonzes=[]

forras=open('kolcsonzesek.txt', mode='r', encoding='utf-8')

forras.readline()

for sor in forras:
    adat=sor.strip().split(';')
    kolcsonzes.append(vizibicikli(nev=(adat[0]), azonosito=(adat[1]), elvora=(adat[2]), elvperc=(adat[3]), visszora=(adat[4]), visszperc=(adat[5])))

forras.close()

#5. feladat

print(f'{len(kolcsonzes)} adat található')

#6. feladat

nevkeres=input('Add meg a keresendő nevet: ')
szamlal=0
for i in range(len(kolcsonzes)):
    if kolcsonzes[i].nev==nevkeres:
        print(f'{nevkeres} név megtalálható a listában és {kolcsonzes[i].elvora} óra {kolcsonzes[i].elvperc} perctől {kolcsonzes[i].visszora} óra {kolcsonzes[i].visszperc} percig')
        szamlal +=1
if szamlal == 0:
    print('Nincs ilyen')

#7. feladat

idokeres=input('Add meg a keresendő időt (óra:perc): ')


for i in range(len(kolcsonzes)):
    teljeselora=kolcsonzes[i].elvora, kolcsonzes[i].elvperc
    teljesvisszora=kolcsonzes[i].visszora, kolcsonzes[i].visszperc

    if teljeselora and teljesvisszora ==idokeres:
        print(f'{idokeres} óra és perckor {teljeselora} kölcsönzési idővel {kolcsonzes[i].nev} ')


