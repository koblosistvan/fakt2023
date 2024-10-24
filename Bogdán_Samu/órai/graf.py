forras = open('Bogdán_Samu\\órai\\labirintus.txt', 'r')
csucsok = list(range(100))
elek = [[] for _ in range(100)]
for i in forras:
    el = []
    el.append(int(i.strip().split(' -- ')[0]))
    el.append(int(i.strip().split(' -- ')[1]))
    elek[el[0]].append(el[1])
forras.close()
print(f'{csucsok = }')
print(f'{elek = }')

start = 10
sor = [start]
megvolt = [False] * 100
szulo = [None] * 100
while len(sor) > 0:
    start = sor[0]
    print(start)
    for csucs in elek[start]:
        if not megvolt[csucs]:
            megvolt[csucs] = True
            sor.append(csucs)
    sor.remove(start)