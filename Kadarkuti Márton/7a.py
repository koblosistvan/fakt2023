def vonal():
    print("-"*30)

forras = open("7a-lakas-arak.txt", "r", encoding="utf-8")
forras.readline() #rossz sor

teruletek = []
arak = []

for sor in forras:
    adat = sor.strip().split(' ')
    teruletek.append(int(adat[0]))
    arak.append(int(adat[1]))
forras.close()
vonal()

print(teruletek)
print(arak)

#+1 feladat
legdragabbSorszama = arak.index(max(arak)) + 1

#nyelvhelyesség:
def névelő(x):  #bemenet: sorszám | kimenet: névelő
    if x in (1,5,50,51,52,53,54,55,56,57,58,59):
        return "az"
    else:
        return "a"

print(f"A legdrágább lakás {névelő(legdragabbSorszama)} {legdragabbSorszama}. sorszámú, és {arak[legdragabbSorszama-1]} millió Ft.-ba kerül.")
vonal()

#2+ feladat
dragabb500Mforintnal = False
for i in range(len(arak)):
    if arak[i] > 500:
        dragabb500Mforintnal = True
        break
if dragabb500Mforintnal:
    print("<Van> olyan lakás a listán, amelyik drágább 500 millió Ft.-nál.")
else:
    print("<Nincs> olyan lakás a listán, amelyik drágább 500 millió Ft.-nál.")
vonal()

#3+ feladat
m2_arak = []
for i in range(len(arak)):
    m2_arak.append(arak[i] / teruletek[i])

print(f"A legdrágább lakás négyzetméter ár szempontjából {névelő(m2_arak.index(max(m2_arak))+1)} {m2_arak.index(max(m2_arak))}. sorszámú lakás.")
print(f"({arak[m2_arak.index(max(m2_arak))]} millió Ft)")
vonal()


#4+ feladat
szamlalo_20millioAlatt = 0
for i in range(len(arak)):
    if arak[i] < 20:
        szamlalo_20millioAlatt += 1
if bool(szamlalo_20millioAlatt):
    print(f"A 20 millió Ft.-nál alacsonyabb árú ingatlanok száma {szamlalo_20millioAlatt} db.")
else:
    print("Minden ingatlan legalább 20 millió Ft.-ba kerül.")
vonal()

#5+ feladat
try:
    open("árak.txt", "x", encoding="utf-8")
    index_txt = []    # 50 és 60 m2 közötti ingatlanok indexei
    for i in range(len(teruletek)):
        if 50 < teruletek[i] < 60:
            index_txt.append(i)
    with open("árak.txt", "a", encoding="utf-8") as t:
        t.write("~ 50m² és 60m² közötti alapterületű lakások listája ~\n\n")
        t.write("Sorszám | Alapterület |     Ár")
        for i in range(len(index_txt)):
            t.write(f"\n[{index_txt[i]+1}.] -=- [{teruletek[index_txt[i]]} m²] -=- [{arak[index_txt[i]]} millió Ft]")
    print("A dokumentum [árak.txt] sikeresen le lett generálva.")
except FileExistsError:
    print("A dokumentum [árak.txt] már megtekinthető.")
except:
    print("Probléma történt a dokumentum létrehozásakor.")
vonal()
#6+ feladat
print("A program ki fog írni árlistát a felhasználó által megadott intervallum alapján.")
validUserInput = False
while not validUserInput:
    try:
        temp = input("[>] Adj meg egy [ár] tartományt vesszővel elválasztva: ")
        vonal()
    except:
        print("  **Érvénytelen bemenet. Próbáld újra.\n")
        continue

    try:
        temp = temp.strip().split(",")
        a,b = int(temp[0]), int(temp[1])  #zárt intervallum: [a,b]
    except:
        print("  **Az ártartományt vesszővel elválasztva, más karakterek nélkül kell megadni.\n")
        continue
    if a == b:
        print("  **A tartomány határai különbözőek.\n")
        continue

    if a > b:
        a,b = b,a
    if a < min(arak) or b > max(arak):
        print("A megadott intervallum az árak tartományán kívülre esik.")
        print("  **Az ártartományt [millió Ft]-ban kell megadni.\n")
        continue

    validUserInput = True  #ha a szűrés sikeres, kilép

hatos_feladat_indexek = []
for i in range(len(arak)):
    if a <= arak[i] <= b:
        hatos_feladat_indexek.append(i)


if bool(len(hatos_feladat_indexek)):
    print(f"\nLakások {a} és {b} millió Ft közötti árral:")
    print(f"({len(hatos_feladat_indexek)} találat)")
    for i in range(len(hatos_feladat_indexek)):
        print(f"[{hatos_feladat_indexek[i]+1}.] -=- {arak[hatos_feladat_indexek[i]]} millió Ft")
else:
    print(f"\nLakások {a} és {b} millió Ft közötti árral:")
    print(f"(Nincs találat)")
vonal()

#8b feladat




#7+ feladat
loop = True  #a program innentől határozott kereső, van lehetőség kilépni
while loop:
    print("A program rá fog keresni egy konkrét ingatlanra [ár] és [alapterület] függvényében, amit a felhasználó ad meg.")
    print("Először az [alapterület] és utána az [ár] értéke kell, vesszővel elválasztva.")
    validUserInput = False
    while not validUserInput:
        try:
            temp = input("[>] Adj meg egy [alapterület] és egy [ár] értéket: ")
            vonal()
        except:
            print("  **Érvénytelen bemenet. Próbáld újra.\n")
            continue
        try:
            temp = temp.strip().split(",")
            a,b = int(temp[0]), int(temp[1])  # a: TERÜLET | b: ÁR
        except:
            print("  **Az értékeket vesszővel elválasztva, más karakterek nélkül kell megadni.\n")
            continue
        if abs(a) != a or abs(b) != b or a == 0 or b == 0:
            print("  **Érvénytelen bemenet. Próbáld újra.\n")
            continue

        print("\nBEMENET MEGERŐSÍTÉS")
        print(f"Keresés erre: {a}m² | {b} millió Ft.")
        try:
            temp = input("[>] Keresés indítása [y / n] : ")
            if temp == "y":
                validUserInput = True
                print("\n~KERESÉSI EREDMÉNY~")
            else:
                print(" **Felhasználó által megszakítva.\n")
                continue
        except:
            print("  **Érvénytelen bemenet.")
            continue

    keres_lista = []
    for i in range(len(arak)):
        if a == teruletek[i] and b == arak[i]:
            keres_lista.append(i)

    if not bool(keres_lista):
        print("  0 találat")
    else:
        print(f"{len(keres_lista)} találat")
        for i in range(len(keres_lista)):
            print(f"[{keres_lista[i] + 1}.] -=- {teruletek[keres_lista[i]]}m² | {arak[keres_lista[i]]} millió Ft")
    vonal()
    temp = input("[>] KERESÉS ISMÉT? [y / n] :")
    if temp != "y":
        print("A program leállt.")
        quit()
