forras = open("utasadat.txt", mode="r", encoding="utf-8")

allomas = []
ido = []
kartya_azonosito = []
berlet_fajta = []
ervenyesseg = []

for sor in forras:
    adat = sor.strip().split(" ")
    allomas.append(int(adat[0]))
    ido.append(adat[0])
    kartya_azonosito.append(int(adat[2]))
    berlet_fajta.append(adat[3])
    ervenyesseg.append(adat[4])

forras.close()

