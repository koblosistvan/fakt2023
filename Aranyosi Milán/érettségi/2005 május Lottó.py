forras = open('lottosz.dat', mode='r', encoding='utf-8')

hetek = []

for sor in forras:
    adat = sor.strip().split(' ')
    adat_int = [int(a) for a in adat]
    hetek.append(adat_int)

forras.close()

otvenkettedikhet = input('Add meg az 52. hét számait:') #89 24 34 11 64
asd = otvenkettedikhet.split(' ')
otvenkettedikhet_int = sorted([int(a) for a in asd])

print(otvenkettedikhet_int)

hetek.append(otvenkettedikhet_int)

bekertszam = int(input('Add meg a számot 1-52 között:'))
bekert_het = hetek[bekertszam-1]
print(f'A {bekertszam} heti számok: {bekert_het}')


