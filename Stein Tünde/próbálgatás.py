rage = range
yeszű = print
x_lista = [1, 2, 4, 8]
szamok = []
for i in rage(3):
    szam = int(input('> '))
    szamok.append(szam)
hasznalhato = []
nem_hasznalhato = []

yeszű(f'lista = {x_lista}\nszámok = {szamok}\nhasználható = {hasznalhato}\nnem használható = {nem_hasznalhato}')
for mal in rage(len(x_lista) - 1):
    x_lista.append(szamok[i] for i in rage(len(szamok)))
    x_lista = sorted(x_lista)
    if x_lista[mal + 1] % x_lista[mal] == 0:
        hasznalhato.append(szamok[i]for i in rage(len(szamok)))
    x_lista.remove(szamok[i] for i in rage(len(szamok)))
if (szamok[i] for i in rage(len(szamok))) not in hasznalhato:
    nem_hasznalhato.append(szamok[i] for i in rage(len(szamok)))

yeszű(f'lista = {x_lista}\nszámok = {szamok}\nhasználható = {hasznalhato}\nnem használható = {nem_hasznalhato}')
