forras = open('Bogdán_Samu\\órai\\labirintus.txt', 'r')
csucsok = []
elek = []
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

s = [0]
v = [False] * len(csucsok)
while len(s):
    q = s.pop(s[0])
    if not v[q]:
        v[q] = True
        for i in elek[q]:
            s.append(i)
print(v)
