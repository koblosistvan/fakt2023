#1
forras = open("PigaiPéter/érettségi/2021maj/4_godrok/melyseg.txt", mode="r", encoding="utf-8")
melysegek = []
for adat in forras:
    melysegek.append(int(adat.strip()))
SZELESSEG = 10
forras.close()

print("1. feladat")
print(f"A fájl adatainak száma: {len(melysegek)}")

#2
print("2. feladat")
tavinput = int(input("Adjon meg egy távolságértéket!"))
print(f"Ezen a helyen a felszín {melysegek[tavinput - 1]} méter mélyen van.")

#3
print("3. feladat")
print(f"Az érintetlen terület aránya {round(melysegek.count(0)/len(melysegek) * 100, 2)}%.")

#4
fajl = open("PigaiPéter/érettségi/2021maj/4_godrok/godrok.txt", mode="w", encoding="utf-8")
kiirando = []
godor = []
meter = []
godrok = []
kezdo = []
veg = []
for i in range(len(melysegek)):
    if melysegek[i] != 0 and melysegek[i-1] == 0:
        kezdo.append(i+1)
    if melysegek[i] != 0:
        godor.append(str(melysegek[i]))
        meter.append(i+1)
        if melysegek[i+1] == 0:
            kiirando.append(" ".join(godor))
            godrok.append([godor])
            veg.append(i+1)
    else:
        godor = list()
fajl.write("\n".join(kiirando))
fajl.close()

#5
print("5. feladat")
print(f"A gödrök száma: {len(kiirando)}")

#6
print("6. feladat\na)")
for i in range(len(kezdo)):
    if kezdo[i] <= tavinput <= veg[i]:
        print(f"A gödör kezdete: {kezdo[i]} méter, a gödör vége: {veg[i]} méter.")

print("b)")
