forras = open('melyseg.txt', mode='r', encoding='utf-8')
melysegek = [int(sor.strip()) for sor in forras]
forras.close()

print("1. feladat")
print(f"A fájl adatainak száma: {len(melysegek)}")

tav = int(input("2. feladat\nAdjon meg egy távolságértéket! "))
print(f"Ezen a helyen a felszín {melysegek[tav]} méter mélyen van.")

erintetlen = melysegek.count(0)
arany = (erintetlen / len(melysegek)) * 100
print("3. feladat")
print(f"Az érintetlen terület aránya {arany:.2f}%.")

godrok = []
godor = []
for m in melysegek:
    if m > 0:
        godor.append(m)
    elif godor:
        godrok.append(godor)
        godor = []
if godor:
    godrok.append(godor)

f = open("godrok.txt", "w")
for g in godrok:
    f.write(" ".join(map(str, g)) + "\n")
f.close()

print("5. feladat")
print(f"A gödrök száma: {len(godrok)}")

if melysegek[tav] == 0:
    print("6. feladat\nAz adott helyen nincs gödör.")
else:
    kezd, veg = tav, tav
    while kezd > 0 and melysegek[kezd - 1] > 0:
        kezd -= 1
    while veg < len(melysegek) - 1 and melysegek[veg + 1] > 0:
        veg += 1

    print("6. feladat")
    print(f"a) A gödör kezdete: {kezd} méter, a gödör vége: {veg} méter.")

    max_melyseg = max(melysegek[kezd:veg + 1])
    print(f"c) A legnagyobb mélysége {max_melyseg} méter.")

    terfogat = sum(melysegek[kezd:veg + 1]) * 10
    print(f"d) A térfogata {terfogat} m^3.")

    vizszint = max_melyseg - 1
    vizmennyiseg = sum(max(0, m - vizszint) for m in melysegek[kezd:veg + 1]) * 10
    print(f"e) A vízmennyiség {vizmennyiseg} m^3.")

    melyules = all(melysegek[i] >= melysegek[i - 1] for i in range(kezd + 1, tav + 1)) and all(
        melysegek[i] <= melysegek[i - 1] for i in range(tav, veg + 1))
    print("b) " + ("Folyamatosan mélyül." if melyules else "Nem mélyül folyamatosan."))

