def fel(a):
    print(f"{a}. feladat:", end=" ")

forras = open("jackie.txt", mode="r", encoding="UTF-8")

forras.readline()

év = []
verseny_db = []
nyereségek_db = []
dobogós = []
első_helyről_db = []
leggyorsabb = []

for sor in forras:
    adat = sor.strip().split("\t")
    év.append(int(adat[0]))
    verseny_db.append(int(adat[1]))
    nyereségek_db.append(int(adat[2]))
    dobogós.append(int(adat[3]))
    első_helyről_db.append(int(adat[4]))
    leggyorsabb.append(int(adat[5]))

forras.close()

#3. feadat
fel(3)

print(len(év))

#4. feladat
fel(4)

print(év[verseny_db.index(max(verseny_db))])

#5. feladat
fel(5)

#for i in range(len(év)):









