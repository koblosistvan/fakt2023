forras = open('Bogdán_Samu\\órai\\labirintus.txt', 'r', encoding='utf-8')
csucsok = list(range(100))
elek = [[] for _ in range(100)]
for i in forras:
    el = i.strip().split(' -- ')
    elek[int(el[0])].append(int(el[1]))
forras.close()
print(f'{csucsok = }')
print(f'{elek = }')
start = 10
sor = [start]
megvolt = [False] * 100
szulo = [None] * 100
while len(sor) > 0:
    start = sor[0]
    for csucs in elek[start]:
        if not megvolt[csucs]:
            megvolt[csucs] = True
            szulo[csucs] = start
            sor.append(csucs)
    print(f'szülő: {szulo[start]}, csúcs: {start}')
    sor.remove(start)