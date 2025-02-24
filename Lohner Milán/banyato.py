forras = open("melyseg.txt", mode="r", encoding="utf-8")

sorok_szama = int(forras.readline().strip())
oszlopok_szama = int(forras.readline().strip())
melysegek = [list(map(int, forras.readline().split())) for _ in range(sorok_szama)]
forras.close()

sor = int(input("A meres soranak azonositoja="))
oszlop = int(input("A meres oszlopanak azonositoja="))
print(f"A mért mélység az adott helyen {melysegek[sor - 1][oszlop - 1]} dm")

felszin = sum(1 for sor in melysegek for ertek in sor if ertek > 0)
osszmelyseg = sum(ertek for sor in melysegek for ertek in sor if ertek > 0)
atlag = osszmelyseg / felszin if felszin > 0 else 0
print(f"A tó felszíne: {felszin} m2, átlagos mélysége: {round(atlag / 10, 2)} m")

max_melyseg = max(max(sor) for sor in melysegek)
koordinatak = [(i + 1, j + 1) for i, sor in enumerate(melysegek) for j, ertek in enumerate(sor) if ertek == max_melyseg]
print(f"A tó legnagyobb mélysége: {max_melyseg} dm")
print("A legmélyebb helyek sor-oszlop koordinátái:", " ".join(f"({s}; {o})" for s, o in koordinatak))

iranyok = [(-1, 0), (1, 0), (0, -1), (0, 1)]
partvonal = 0
for i in range(1, sorok_szama - 1):
    for j in range(1, oszlopok_szama - 1):
        if melysegek[i][j] > 0:
            for di, dj in iranyok:
                ni, nj = i + di, j + dj
                if melysegek[ni][nj] == 0:
                    partvonal += 1
print(f"A tó partvonala {partvonal} m hosszú")

oszlop = int(input("A vizsgált szelvény oszlopának azonosítója="))
kimenet = open("diagram.txt", "w")
for i, sor in enumerate(melysegek, start=1):
    csillagok = "*" * round(sor[oszlop - 1] / 10)
    kimenet.write(f"{i:02}{csillagok}\n")
kimenet.close()
print("állomány elkészült.")
