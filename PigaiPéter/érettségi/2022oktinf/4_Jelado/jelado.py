forras = open("PigaiPéter\\érettségi\\2022oktinf\\4_Jelado\\jel.txt", mode="r", encoding="utf-8")
ido = []
kord = []
for sor in forras:
    adat = sor.strip().split(" ")
    ido.append([int(adat[0]), int(adat[1]), int(adat[2])])
    kord.append([int(adat[3]), int(adat[4])])
forras.close()
#2
print("2. feladat")
bekertsorszam = int(input(" Adja meg a jel sorszámát!"))-1
print(f"x={kord[bekertsorszam][0]} y={kord[bekertsorszam][1]} ")

#3
def eltelt(idopont1, idopont2):
    return (idopont1[0]*3600 + idopont1[1]*60 + idopont1[2])-(idopont2[0]*3600 + idopont2[1]*60 + idopont2[2])

#4
print(f"4. feladat \nIdőtartam: {eltelt(ido[-1], ido[0])//3600}:{eltelt(ido[-1], ido[0])//60%60}:{eltelt(ido[-1], ido[0])%60} ")

#5
minx = kord[0][0]
maxx = kord[0][0]
miny = kord[0][1]
maxy = kord[0][1]
for i in range(len(kord)):
    if kord[i][0] < minx:
        minx = kord[i][0]
    if kord[i][0] > maxx:
        maxx = kord[i][0]
    if kord[i][1] < miny:
        miny = kord[i][1]
    if kord[i][1] > maxy:
        maxy = kord[i][1]
print(f"5. feladat \nBal alsó: {minx} {miny}, jobb felső: {maxx} {maxy} ")

#6
elmozdulas = 0
for i in range(len(kord)-1):
    elmozdulas += pow((kord[i][0]-kord[i+1][0])**2+(kord[i][1]-kord[i+1][1])**2, 0.5)
print(f"6. feladat \nElmozdulás: {round(elmozdulas,3)} egység ")

#7
