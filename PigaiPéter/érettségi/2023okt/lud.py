forrasdob = open("PigaiPéter\\érettségi\\2023okt\\dobasok.txt", mode="r", encoding="utf-8")
forrasosv = open("PigaiPéter\\érettségi\\2023okt\\osvenyek.txt", mode="r", encoding="utf-8")

dobasok = []
for char in forrasdob:
    char = char.strip().split(" ")
    for i in range(len(char)):
        dobasok.append(int(char[i]))
forrasdob.close()

osvenyek = []
for sor in forrasosv:
    osvenyek.append([])
    char = sor.strip()
    for i in range(len(char)):
        osvenyek[-1].append(char[i])
forrasosv.close()
print(f"2. feladat \nA dobások száma: {len(dobasok)} \nAz ösvények száma: {len(osvenyek)} ")

maxhossz = len(osvenyek[0])
maxosveny = 0
for i in range(len(osvenyek)):
    if len(osvenyek[i]) > maxhossz:
        maxhossz = len(osvenyek[i])
        maxosveny = i +1

print(f"3. feladat \nAz egyik leghosszabb a(z) {maxosveny}. ösvény, hossza: {maxhossz}")


print(f"4. feladat")
helytelen = True
while helytelen:
    bekertosveny = int(input(f"Adja meg egy ösvény sorszámát!(max {len(osvenyek)}):"))
    jatekosszam = int(input(f"Adja meg a játékosok számát!(min 2, max 5):"))
    if len(osvenyek) >= bekertosveny > 0 and 6 > jatekosszam > 1:
        helytelen = False

print("5. feladat")
m = osvenyek[bekertosveny - 1].count("M")
v = osvenyek[bekertosveny - 1].count("V")
e = osvenyek[bekertosveny - 1].count("E")

if m:
    print(f"M: {m} darab")
if v:
    print(f"V: {m} darab")
if e:
    print(f"E: {e} darab")

kulonleges = open("PigaiPéter\\érettségi\\2023okt\\kulonleges.txt", mode="w", encoding="utf-8")
for i in range(len(osvenyek[bekertosveny - 1])):
    if osvenyek[bekertosveny - 1][i] != "M":
        kulonleges.write(f"{i + 1}\t{osvenyek[bekertosveny - 1][i]}\n")

jatekosok = []
for i in range(jatekosszam):
    jatekosok.append([])
nyert = False
i = 0
j = 0
while not nyert:
    if i == jatekosszam:
        i = 0
    jatekosok[i].append(dobasok[j])
    if sum(jatekosok[i]) >= len(osvenyek[bekertosveny - 1]):
        nyert = True
    i += 1
    j += 1
print(f"7. feladat \nA játék a(z) {j + 1}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {i + 1}")
