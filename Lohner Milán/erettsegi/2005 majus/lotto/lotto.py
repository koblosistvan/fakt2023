forras = open('lottosz.dat', mode='r', encoding='utf-8')
szamok = []


for sor in forras:
    adat = sor.strip().split(' ')
    adat_int = [int(a) for a in adat]
    szamok.append(adat_int)

print(szamok)

forras.close()

beker = input('Add meg a szamokat 1-51 ig')
bekeros = beker.split(' ')
intel = [int(a) for a in bekeros]
print(sorted(intel))


het_szamai = int(input('Melyikre vagy kivancsi: '))
hetek_int = szamok[het_szamai-1]
print(f'A {het_szamai},{hetek_int}')




egyszersem = False

nemvoltak = [range(1, 54)].remove(szamok)
#for i in range(len(szamok)):
    #if voltak

print(nemvoltak)





