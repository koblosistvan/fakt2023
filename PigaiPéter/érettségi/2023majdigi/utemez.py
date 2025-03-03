forras1 = open("PigaiPéter\\érettségi\\2023majdigi\\taborok.txt", mode="r", encoding="utf-8")
kezdhonap = []
kezdnap = []
veghonap = []
vegnap = []
jel = []
foglalkozas = []
for sor in forras1:
    adat = sor.strip().split("\t")
    kezdhonap.append(int(adat[0]))
    kezdnap.append(int(adat[1]))
    veghonap.append(int(adat[2]))
    vegnap.append(int(adat[3]))
    jel.append(adat[4])
    foglalkozas.append(adat[5])
forras1.close()
#2
print(f"2. feladat\nAz adatsorok száma: {len(jel)}\nAz először rögzített tábor témája: {foglalkozas[0]}\nAz utoljára rögzített tábor témája: {foglalkozas[-1]}")

#3
print("3. feladat")
zeneiindex = []
for i in range(len(foglalkozas)):
    if foglalkozas[i] == "zenei":
        zeneiindex.append(i)
if len(zeneiindex) != 0:
    for index in zeneiindex:
        print(f"Zenei tábor kezdődik {kezdhonap[index]}. hó {kezdnap[index]}. napján.")
else:
    print("Nemvolt zenei tábor.")

#4
legtobb = len(jel[0])
for i in range(len(jel)):
    if len(jel[i]) > legtobb:
        legtobb = len(jel[i])
legtobbindex = []
for i in range(len(jel)):
    if len(jel[i]) == legtobb:
        legtobbindex.append(i)
print(f"4. feladat")
for index in legtobbindex:
    print(f"Legnépszerűbbek:\n{kezdhonap[index]} {kezdnap[index]} {foglalkozas[index]}")

#5
def sorszam(honap, nap):
    if honap == 6:
        honap = 0
    elif honap == 7:
        honap = 30
    else:
        honap = 61
    ossznap = honap + nap
    return ossznap - 16 + 1

#6
print("6. feladat")
bekertho = int(input("hó:"))
bekertnap = int(input("nap:"))
taborszam = 0
for i in range(len(kezdnap)):
    if sorszam(kezdhonap[i], kezdnap[i]) <= sorszam(bekertho, bekertnap) <= sorszam(veghonap[i], vegnap[i]):
        taborszam += 1
print(f"Ekkor éppen {taborszam} tábor tart.")

#7
bekertjel = input(f"7. feladat\nAdja meg egy tanuló betűjelét:")
taborkezdesindex = []
for i in range(len(jel)):
    if jel[i].count(bekertjel) != 0:
        taborkezdesindex.append(i)

taborkezdes = []
for i in range(len(taborkezdesindex)):
    taborkezdes.append(sorszam(kezdhonap[taborkezdesindex[i]], kezdnap[taborkezdesindex[i]]))
taborkezdessorted = sorted(taborkezdes.copy())

egytanulo = open("PigaiPéter\\érettségi\\2023majdigi\\egytanulo.txt", mode="w", encoding="utf-8")
for i in range(len(taborkezdessorted)):
    egytanulo.write(f"{kezdhonap[taborkezdes.index(taborkezdessorted[i])]}.{kezdnap[taborkezdes.index(taborkezdessorted[i])]}.-{veghonap[taborkezdes.index(taborkezdessorted[i])]}.{vegnap[taborkezdes.index(taborkezdessorted[i])]}. {foglalkozas[taborkezdes.index(taborkezdessorted[i])]}\n")

    