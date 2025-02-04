
forras=open('utca.txt', mode='r', encoding='utf-8')

forras.readline()


oszlop1 = []  # Adószámok
oszlop2 = []  # Utca nevek
oszlop3 = []  # Házszámok
oszlop4 = []  # Adósávok
oszlop5 = []  # Alapterületek


for sor in forras:
    adat = sor.strip().split()
    oszlop1.append(adat[0])
    oszlop2.append(adat[1])
    oszlop3.append(adat[2])
    oszlop4.append(adat[3])
    oszlop5.append(int(adat[4]))

# 2. feladat
print(f"2. feladat. A mintában {len(oszlop1)} telek szerepel.")

# 3. feladat
keresett_adoszam = input("3. feladat. Egy tulajdonos adószáma: ")
if keresett_adoszam in oszlop1:
    print("A tulajdonos telkei:")
    for i in range(len(oszlop1)):
        if oszlop1[i] == keresett_adoszam:
            print(f"{oszlop2[i]} {oszlop3[i]}")
else:
    print("Nem szerepel az adatállományban.")


# 4. feladat
def ado(sav, terulet):
    if sav == 'A':
        osszeg = 100 * terulet
    elif sav == 'B':
        osszeg = 200 * terulet
    else:
        osszeg = 300 * terulet
    return osszeg if osszeg >= 10000 else 0


# 5. feladat
a_db = 0
a_ado = 0
b_db = 0
b_ado = 0
c_db = 0
c_ado = 0

for i in range(len(oszlop4)):
    fizetendo = ado(oszlop4[i], oszlop5[i])
    if oszlop4[i] == 'A':
        a_db += 1
        a_ado += fizetendo
    elif oszlop4[i] == 'B':
        b_db += 1
        b_ado += fizetendo
    else:
        c_db += 1
        c_ado += fizetendo

print("5. feladat")
print(f"A sávba {a_db} telek esik, az adó {a_ado} Ft.")
print(f"B sávba {b_db} telek esik, az adó {b_ado} Ft.")
print(f"C sávba {c_db} telek esik, az adó {c_ado} Ft.")

# 6. feladat
utca_savok = {}
for i in range(len(oszlop2)):
    if oszlop2[i] not in utca_savok:
        utca_savok[oszlop2[i]] = set()
    utca_savok[oszlop2[i]].add(oszlop4[i])

print("6. feladat. A több sávba sorolt utcák:")
for utca, savok in utca_savok.items():
    if len(savok) > 1:
        print(utca)

# 7. feladat
tulajdonos_ado = {}
for i in range(len(oszlop1)):
    if oszlop1[i] not in tulajdonos_ado:
        tulajdonos_ado[oszlop1[i]] = 0
    tulajdonos_ado[oszlop1[i]] += ado(oszlop4[i], oszlop5[i])

with open('fizetendo.txt', 'w', encoding='utf-8') as kimenet:
    for adoszam, osszeg in tulajdonos_ado.items():
        kimenet.write(f"{adoszam} {osszeg}\n")

######