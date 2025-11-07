forras = open("PigaiPéter/érettségi/Informatika_emelt_gyakorlati_forrasok_1811/4_Sorozatok/lista.txt", mode="r", encoding="utf-8")
kiadas = []
nev = []
epizod = []
hossz = []
latta = []
i = 1
for sor in forras:
    adat = sor.strip()
    if i % 5 == 0:
        latta.append(int(adat))
    elif i % 5 == 4:
        hossz.append(int(adat))
    elif i % 5 == 3:
        adat = adat.split("x")
        epizod.append([int(adat[0]), int(adat[1])])
    elif i % 5 == 2:
        nev.append(adat)
    else:
        if adat == "NI":
            kiadas.append(adat)
        else:
            adat = adat.split(".")
            kiadas.append([int(adat[0]), int(adat[1]), int(adat[2])])
    i += 1
forras.close()

#2
print(f"2. feladat\nA listában {len(kiadas)-kiadas.count('NI')} db vetítési dátummal rendelkező epizód van.")

#3
print(f"3. feladat\nA listában lévő epizódok {latta.count(1)/len(latta):.2%}-át látta.")

#4
osszora = 0
for i in range(len(hossz)):
    if latta[i] == 1:
        osszora += hossz[i]
nap = osszora//(60*24)
ora = osszora//60-osszora//(60*24)*24
perc =osszora - nap*60*24 - ora*60
print(f"4. feladat\nSorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")

#5
bekertdatum = input("5. feladat\nAdjon meg egy dátumot! Dátum= ")
bekertdatum = bekertdatum.split(".")
for i in range(len(nev)):
    if kiadas[i] != "NI":
        if int(bekertdatum[0]) >= kiadas[i][0] and int(bekertdatum[1]) >= kiadas[i][1] and int(bekertdatum[2]) >= kiadas[i][2] and latta[i] != 1:
            print(f"{epizod[i][0]}x{epizod[i][1]:02}\t{nev[i]}")
#6
def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze","cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1
    hetnapja = napok[(ev + ev // 4 – ev // 100 +
    ev // 400 + honapok[ho-1] + nap) % 7]
    return hetnapja