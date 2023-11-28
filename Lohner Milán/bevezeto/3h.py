import random

# Konstansok az intervallumhoz
INTERVALLUM_ALJA = 1
INTERVALLUM_FELSO = 100
MAX_PROBALKOZASOK = 10
FIGYELMEZTES_HATAR = 5

# Véletlen szám generálása az intervallumban
gondolt_szam = random.randint(INTERVALLUM_ALJA, INTERVALLUM_FELSO)

print(f"Üdvözöllek a játékban! A szám {INTERVALLUM_ALJA} és {INTERVALLUM_FELSO} között van.")

probalkozasok = 0

while probalkozasok < MAX_PROBALKOZASOK:
    probalkozasok += 1
    tipp = int(input("Tippelj egy számot: "))

    if tipp == gondolt_szam:
        print(f"Gratulálok, kitaláltad a számot! A helyes válasz: {gondolt_szam}")
        break
    elif tipp < gondolt_szam:
        print("A tipp kisebb, mint a gondolt szám.")
    else:
        print("A tipp nagyobb, mint a gondolt szám.")

    # Figyelmeztetés, ha kevés próbálkozás van hátra
    maradek_probalkozasok = MAX_PROBALKOZASOK - probalkozasok
    if maradek_probalkozasok <= FIGYELMEZTES_HATAR:
        print(f"Figyelem! Már csak {maradek_probalkozasok} próbálkozásod maradt.")

if probalkozasok >= MAX_PROBALKOZASOK:
    print(f"Sajnálom, elfogytak a próbálkozásaid. A gondolt szám: {gondolt_szam}")
