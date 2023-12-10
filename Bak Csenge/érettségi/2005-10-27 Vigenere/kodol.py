
forras = open("Vtabla.dat", mode="r")

kódtábla = []

for sor in forras:
    kódtábla.append(sor.strip())

forras.close()

szöveg = "Ez a szöveg"
kulcs = "auto"
kulcs.upper()

ékezetes = "ÖÜÓŐÚÉÁŰÍ"
ékezetmentes = "OUOOUEAUI"
szöveg.upper()

for i in range(len(ékezetes)):
    szöveg = szöveg.replace(ékezetes[i], ékezetmentes[i])


"""i = 0
while i < len(szöveg):
    if szöveg[i] not in kódtábla[0]:
        szöveg = szöveg.replace(ékezetes[i], "")

    i += 1

print(szöveg)"""

kodolando = ""
for i in range(len(szöveg)):
    if szöveg[i] in kódtábla[0]:
        kodolando += szöveg


kulcs = "auto"
kulcs = kulcs * (len(szöveg) // len(kulcs)+1)
kulcs = kulcs[:len(kodolando)]
print(f"Kulcs: {kulcs}")

kódolt = ""
for i in range(len(kodolando)):
    oszlop = kódtábla[0].find(kodolando[i])
    sor = 0
    while kódtábla[sor][0] != kulcs[i]:
        sor += 1
    kód_karakter = kódtábla[sor][oszlop]
    kódolt += kód_karakter

print(kódolt)

