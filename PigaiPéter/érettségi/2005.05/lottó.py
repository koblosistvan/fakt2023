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
for j in hetiszamok:
    for szám in j:
        for i in range(100):
            if i != szám:
                nemhuzott = True
if nemhuzott:
    print('Van')
else:
    print('Nincs')
páratlan = 0
for j in hetiszamok:
    for szám in j:
        if int(szám) % 2 != 0:
            páratlan += 1
print(páratlan)
hetiszamok.append(hianyzo)

f = open('lotto52.ki', 'a')
for i in range(len(hetiszamok)):
    sor = hetiszamok[i]
    sor = " ".join(sor)
    f.write(sor)
    f.write('\n')