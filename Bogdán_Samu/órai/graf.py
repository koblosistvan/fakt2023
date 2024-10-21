forras = open('Bogdán_Samu\\órai\\labirintus.txt', 'r')
csucsok = []
elek = [0,0,0,0,0,0,0,0,0,0]
for i in forras:
    el = []
    el.append(int(i.strip().split(' -- ')[0]))
    el.append(int(i.strip().split(' -- ')[1]))
    csucsok.append(int(el[0]))
    csucsok.append(int(el[1]))
    elek.append(el)
forras.close()
csucsok = list(set(csucsok))
csucsok.sort()
print(f'{csucsok = }')
print(f'{elek = }')

start = 10
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
    sor.remove(start)