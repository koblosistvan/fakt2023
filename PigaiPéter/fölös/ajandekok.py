forras = open("PigaiPéter\\dobozok.txt", mode="r", encoding="utf-8")
dobozszam = 0
jatekszam = 0
dobozonkentijatekok = []
for sor in forras:
    tagok = sor.strip().split(' ')
    dobozszam = int(tagok[0])
    jatekszam = int(tagok[1])
    break
ajandekok = []
ajandekokösszes = []
for i in range(dobozszam):
    ajandekok.append([])
j = 0
for sor in forras:
    tagok = sor.strip().split(' ')
    dobozonkentijatekok.append(tagok[0])
    for i in range(len(tagok)-1):
        ajandekok[j].append(int(tagok[i + 1]))
        ajandekokösszes.append(int(tagok[i + 1]))
    j += 1
forras.close()

összjatek = 0
for i in range(len(ajandekok)):
    összjatek += len(ajandekok[i])
átlag = összjatek/dobozszam
legtöbbjatek = []

for i in range(len(dobozonkentijatekok)):
    if dobozonkentijatekok[i] == max(dobozonkentijatekok):
        legtöbbjatek.append(str(i + 1))

legnepszerubbjatek = []
legnepszerubbszam = 0
for i in range(1, jatekszam + 1):
    if ajandekokösszes.count(i) > legnepszerubbszam:
        legnepszerubbszam = ajandekokösszes.count(i)

for i in range(1, jatekszam + 1):
    if legnepszerubbszam == ajandekokösszes.count(i):
        legnepszerubbjatek.append(str(i))

if (átlag * 10) % 10 != 0:
    print(f"A játékokat nem lehet egyenletesen elosztani a dobozokban.\nJátékok dobozonkénti átlagos száma: {összjatek/dobozszam}")
else:
    print(f"A játékokat egyenletesen el lehet osztani a dobozokban.\nJátékok dobozonkénti átlagos száma: {int(összjatek/dobozszam)}")
print(f"Legtöbb játék egy dobozban ({max(dobozonkentijatekok)} db) a következő dobozokban volt: {' '.join(legtöbbjatek)}")
print(f"Legnépszerűbb játék(ok): {' '.join(legnepszerubbjatek)}")
print("Melyik dobozokból kell elvenni:\n")
for i in range(len(ajandekok)):
    if len(ajandekok[i]) > átlag:
        print(f"{i + 1}. dobozból {int(len(ajandekok[i]) - átlag)} db játékot")
print("A hiányos dobozokba melyik játék rakható:")

berakhato = open("PigaiPéter\\berakhato.txt", mode="w", encoding="utf-8")

for i in range(len(ajandekok)):
    hianyzo = []
    if len(ajandekok[i]) < átlag:
        for j in range(1, jatekszam + 1):
            if j not in ajandekok[i]:
                hianyzo.append(str(j))
        print(f"{i + 1}. doboz: {' '.join(hianyzo)}")
        berakhato.write(f"{i + 1}. doboz: {' '.join(hianyzo)}\n")

