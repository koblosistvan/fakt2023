forras = open("PigaiPéter\grafok\labirintus.txt", "r", encoding="utf-8")
csucsok = set()
elek = []
for i in forras:
    i = i.strip().split("--")
    csucsok.add(i[0])
    

csucsok = sorted(list(csucsok))
print(f'{csucsok=}')
print(f'{elek=}')

start = 0
sor = [start]
megvolt = [False] * len(csucsok)
szulo = [None] * len(csucsok)
while len(sor) > 0:
    start = sor[0]
    print(start)
    for csucs in elek[start]:
        if not megvolt[csucs]:
            megvolt[csucs] = True
            sor.append(csucs)
            szulo[csucs] = start
    sor.remove(start)
