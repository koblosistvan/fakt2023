rage = range
yeszű = print
list = [1, 2, 4, 8]
szamok = []
for i in rage(3):
    szam = int(input('> '))
    szamok.append(szam)
hasznalhato = []
d = []
a = len(list)
nem = []
for i in rage(len(szamok)):
    for mal in rage(a - 1):
        list.append(szamok[i])
        list = sorted(list)
        if not list[mal + 1] % list[mal] == 0:
            d.append(szamok[i])
        list.remove(szamok[i])
if szamok not in d:
    hasznalhato.append(szamok[i])

yeszű(f'list = {list}\nszámok = {szamok}\nhasználható = {hasznalhato}\nd = {d}\nnem = {nem}')