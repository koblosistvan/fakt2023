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
for i in range(dobozszam):
    ajandekok.append([])
j = 0
for sor in forras:
    tagok = sor.strip().split(' ')
    dobozonkentijatekok.append(tagok[0])
    for i in range(len(tagok)-1):
        ajandekok[j].append(int(tagok[i + 1]))
    j += 1

összjatek = 0
for i in range(len(ajandekok)):
    összjatek += len(ajandekok[i])
átlag = összjatek/dobozszam
legtöbbjatek = []

for i in range(len(dobozonkentijatekok)):
    if dobozonkentijatekok[i] == max(dobozonkentijatekok):
        legtöbbjatek.append(str(i + 1))

legnepszerubb = 0
for ajandektipus in range(15):
    for i in range(len(ajandekok)):
        if ajandekok[i].count(ajandektipus) > legnepszerubb



if (átlag * 10) % 10 != 0:
    print(f"A játékokat nem lehet egyenletesen elosztani a dobozokban.\nJátékok dobozonkénti átlagos száma: {összjatek/dobozszam}")
else:
    print(f"A játékokat egyenletesen el lehet osztani a dobozokban.\nJátékok dobozonkénti átlagos száma: {int(összjatek/dobozszam)}")
print(f"Legtöbb játék egy dobozban ({max(dobozonkentijatekok)} db) a következő dobozokban volt: {' '.join(legtöbbjatek)}")
