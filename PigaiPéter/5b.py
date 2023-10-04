forras = open('5b-homerseklet.txt', mode='r', encoding='utf8')

ido = []
hom = []

for sor in forras:
    adat = sor.strip().split('\t')
    ido.append(adat[0])
    hom.append(float(adat[1]))

forras.close()

harmincfelett = 0

legnagyobb = hom[0]
legnagyobb_ido = ''
legkisebb = hom[0]
legkisebb_ido = ''

no = 0
csokken = 0

legnagyobb_emel = 0
jelenlegi_emel = 0
legnagyobb_emel_ido =''

hom_osszeg = 0
hom_atlag = 0

for i in range(len(hom)):
    if hom[i] > 30:
        harmincfelett += 1
    if hom[i] > hom[i-1]:
        no += 1
    elif hom[i] < hom[i-1]:
        csokken += 1
    if hom[i] > legnagyobb:
        legnagyobb = hom[i]
        legnagyobb_ido = ido[i]
    if hom[i] < legkisebb:
        legkisebb = hom[i]
        legkisebb_ido = ido[i]
    if hom[i] > hom[i-1]:
        hom[i] - hom[i-1] == jelenlegi_emel
        if jelenlegi_emel > legnagyobb_emel:
            legnagyobb_emel = jelenlegi_emel
            ido[i] = legnagyobb_emel_ido
    hom_osszeg == sum(hom)
    hom_atlag = hom_osszeg / len(hom)
print(f' {harmincfelett} alkalommal volt 30 foknal nagyobb ')
print(f' átlag hőmérséklet {hom_atlag} fok.')
print(f'{no} alkalommal nőtt és {csokken} alkalommal csökkent')
print(f'legkisebbet {legkisebb_ido} kor mértük és {legkisebb} volt')
print(f'a legmagasabb {legnagyobb_ido}kor mértük és {legnagyobb} volt')
