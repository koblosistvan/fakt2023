forras = open("PigaiPéter\grafok\labirintus.txt", "r", encoding="utf-8")
csucsok = set()
elek = []
for i in range(100):
    csucsok.add(i)
csucsok = sorted(list(csucsok))

for i in csucsok:
    elek.append([])

forras = open("PigaiPéter\grafok\labirintus.txt", "r", encoding="utf-8")

for el in forras:
    el = el.strip().split(" -- ")
    elek[csucsok.index(int(el[0]))].append(int(el[1]))

forras.close()

start = 10
sor = [start]
megvolt = [False] * 100
szulo = [-1] * 100
while len(sor) > 0:
    start = sor[0]
    #print(start)
    for csucs in elek[start]:
        if not megvolt[csucs]:
            megvolt[csucs] = True
            sor.append(csucs)
            szulo[csucs] = start
    sor.remove(start)
start = max(szulo)
megvot = []
utvonal = []
while start not in megvot:
    utvonal.append(str(start))
    megvot.append((start))
    start = szulo[start]
utvonal = reversed(utvonal)
print('-'.join(utvonal))


    