forras = open("PigaiPéter\\érettségi\\2022majinfo\\Informatika_forras_E2211\\4_Epitmenyado\\utca.txt")
adat = forras.readline().strip().split(" ")
A = int(adat[0])
B = int(adat[1])
C = int(adat[2])
adoszam = []
utca = []
hazszam = []
adosav = []
alapterulet = []
for sor in forras:
    adat = sor.strip().split(" ")
    adoszam.append(int(adat[0]))
    utca.append(adat[1])
    hazszam.append(adat[2])
    adosav.append(adat[3])
    alapterulet.append(int(adat[4]))
forras.close()

#2
print(f"2. feladat. A mintában {len(adoszam)} telek szerepel.")

#3
van = False
print("3. feladat.")
bekertadoszam = int(input("Egy tulajdonos adószáma:"))
for i in range(len(adoszam)):
    if adoszam[i] == bekertadoszam:
        print(f"{utca[i]} {hazszam[i]}")
        van = True
if not van:
    print("Nem szerepel az adatállományban.")
#4
def ado(adósáv, alapterület):
    if adósáv * alapterület < 10000:
        return 0
    else:
        return adósáv * alapterület

#5
print("5. feladat")
adoa = 0
adob = 0
adoc = 0
for i in range(len(adoszam)):
    if adosav[i] == "A":
        adoa += ado(A, alapterulet[i])
    elif adosav[i] == "B":
        adob += ado(B, alapterulet[i])
    else:
        adoc += ado(C, alapterulet[i])
print(f"A sávba {adosav.count('A')} telek esik, az adó {adoa} Ft.")
print(f"A sávba {adosav.count('B')} telek esik, az adó {adob} Ft.")
print(f"A sávba {adosav.count('C')} telek esik, az adó {adoc} Ft.")

#6
print("6. feladat. A több sávba sorolt utcák:")
vizsgalt = []
for i in range(len(adoszam)):
    if utca[i] not in vizsgalt:
        for j in range(len(adosav)):
            if utca[i] == utca[j] and adosav[i] != adosav[j]:
                print(utca[i])
                break
    vizsgalt.append(utca[i])

#7
fizetendo = open("PigaiPéter\\érettségi\\2022majinfo\\Informatika_forras_E2211\\4_Epitmenyado\\fizetendo.txt", mode="w", encoding="utf-8")
tulajok = set(adoszam)
tulajok = list(tulajok)
for i in range(len(tulajok)):
    fizetendoado = 0
    for j in range(len(adoszam)):
        if tulajok[i] == adoszam[j]:
            if adosav[j] == "A":
                fizetendoado += ado(A, alapterulet[i])
            elif adosav[j] == "B":
                fizetendoado += ado(B, alapterulet[i])
            else:
                fizetendoado += ado(C, alapterulet[i])
    fizetendo.write(f"{tulajok[i]} {fizetendoado}\n")
