forras = open('lottosz.dat', mode='r', encoding='utf-8')
hetiszamok = []
for i in forras:
    szamok = i.strip().split(' ')
    hetiszamok.append(szamok)
hianyzo = input('Add meg az 52.heti számokat:')
hianyzo = hianyzo.split(' ')
hianyzo = list(hianyzo)
hianyzo = [eval(i) for i in hianyzo]
hianyzo = sorted(hianyzo)
print(' '.join(map(str, hianyzo)))
bekert = int(input('Adj meg egy számot 1-51 között:'))
print(hetiszamok[bekert-1])
nemhuzott = False
for sor in forras:
    for szám in sor:



