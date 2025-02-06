fajl = input('Adja meg a bementi fájl nevét! ')
sor = input('Adja meg egy sor számát! ')
oszlop = input('Adja meg egy oszlop számát! ')

forras = open(fajl, mode='r', encoding='utf-8')

sorok = []
iras = []

for sor in forras:
    adat = list(sor.strip().split(' '))
    if len(adat) == 9:
        sorok.append(adat)
    else:
        iras.append(adat)

forras.close()

print(sorok)