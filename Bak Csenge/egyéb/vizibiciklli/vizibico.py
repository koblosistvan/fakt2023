def fel(a):
    print(f"\n{a}. feladat")

forras = open("kolcsonzesek.txt", mode="r", encoding="UTF-8")

nev = []
azon = []
elviteli_ora = []
elviteli_perc = []
visszahoz_ora = []
visszahoz_perc = []

forras.readline()

for sor in forras:
    adat = sor.strip().split(";")
    nev.append(adat[0])
    azon.append(adat[1])
    elviteli_ora.append(int(adat[2]))
    elviteli_perc.append(int(adat[3]))
    visszahoz_ora.append(int(adat[4]))
    visszahoz_perc.append(int(adat[5]))

forras.close()

def mpre(ora, perc):
    return ora*360 + perc*60

#5. feladat
fel(5)

print(f"{len(nev)} adat van.")

#6. feladat
fel(6)

#bekert = input("Adj meg egy nevet.")
bekert = "Kata"


print(f"{bekert} kölcsönzései:")

for i in range(len(nev)):
    if bekert == nev[i]:
        print(f"{elviteli_ora[i]}:{elviteli_perc[i]}-{visszahoz_ora[i]}:{visszahoz_perc[i]}")
if bekert not in nev:
    print("Nem volt ilyen nevű kölcsönző.")

#7. feladat
fel(7)

a, b = input("Adj meg egy időpontot ora:perc alakban").split(":")

h_bekért = int(a)
min_bekért = int(b)

print("Vizen levő járművek:")

for i in range(len(nev)):
    if (mpre(elviteli_ora[i], elviteli_perc[i]) <= mpre(h_bekért, min_bekért)) and (mpre(h_bekért, min_bekért) <= mpre(visszahoz_ora[i], visszahoz_perc[i])):
        print(f"{elviteli_ora[i]}:{elviteli_perc[i]}-{visszahoz_ora[i]}:{visszahoz_perc[i]} : {nev[i]}")




