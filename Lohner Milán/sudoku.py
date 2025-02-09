konnyu = open('konnyu.txt', mode='r', encoding='utf-8')
kozepes = open('kozepes.txt', mode='r', encoding='utf-8')
nehez = open('nehez.txt', mode='r', encoding='utf-8')

konnyu9 = ''
kozepes9 = ''
nehez9 = ''

tartalom = konnyu.readlines()

for i in range(9):
    konnyu9 += tartalom[i]

print(konnyu9)

valaszt = input('Könnyű, közepes vagy nehéz: ')

def fajl_olvasas(fajlnev):
    with open(fajlnev, 'r', encoding='utf-8') as f:
        sorok = f.readlines()

    tabla = [list(map(int, sor.split())) for sor in sorok[:9]]
    lepessorok = [tuple(map(int, sor.split())) for sor in sorok[9:]]

    return tabla, lepessorok

def resztabla_index(sor, oszlop):
    return (sor // 3) * 3 + (oszlop // 3) + 1

def ures_helyek_szazalek(tabla):
    osszes_hely = 81
    ures_hely = sum(sor.count(0) for sor in tabla)
    return round((ures_hely / osszes_hely) * 100, 1)

def ervenyes_lepes(tabla, szam, sor, oszlop):
    if tabla[sor][oszlop] != 0:
        return "A helyet már kitöltötték"
    if szam in tabla[sor]:
        return "Az adott sorban már szerepel a szám"
    if szam in [tabla[r][oszlop] for r in range(9)]:
        return "Az adott oszlopban már szerepel a szám"

    sorstart = (sor // 3) * 3
    alattsorstart = (oszlop // 3) * 3

    for r in range(sorstart, sorstart + 3):
        for c in range(alattsorstart, alattsorstart + 3):
            if tabla[r][c] == szam:
                return "Az adott résztáblázatban már szerepel a szám"

    return "A lépés megtehető"

# Kiválasztott fájl betöltése
fajlnev = valaszt + ".txt"
sor = int(input("Adja meg egy sor számát! ")) - 1
oszlop = int(input("Adja meg egy oszlop számát! ")) - 1

tabla, lepessorok = fajl_olvasas(fajlnev)

# 3. feladat
if tabla[sor][oszlop] == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {tabla[sor][oszlop]}")

print(f"A hely a(z) {resztabla_index(sor, oszlop)} résztáblázathoz tartozik.")

# 4. feladat
print(f"Az üres helyek aránya: {ures_helyek_szazalek(tabla)}%")

# 5. feladat
for szam, lepessor, lepesoszlop in lepessorok:
    lepessor -= 1
    lepesoszlop -= 1
    print(f"A kiválasztott sor: {lepessor + 1} oszlop: {lepesoszlop + 1} a szám: {szam}")
    print(ervenyes_lepes(tabla, szam, lepessor, lepesoszlop))
