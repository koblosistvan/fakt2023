forras = open('5b-homerseklet.txt', mode='r', encoding='utf-8')

ido = []
homerseklet = []

for sor in forras:
    adat = sor.strip().split('\t')
    ido.append(adat[0])
    homerseklet.append(float(adat[1]))
print(ido)
print(homerseklet)
forras.close()

harmincfelett = 0

legnagyobb = homerseklet[0]
legnagyobb_ido = ''
legkisebb = homerseklet[0]
legkisebb_ido = ''

nott = 0
csokkent = 0

legnagyobb_emelkedes = 0
jelenlegi_emelkedes = 0
legnagyobb_emelkedes_ido =''

homerseklet_osszeg = 0
hom_atlag = 0

for i in range(len(homerseklet)):
    if homerseklet[i] > 30:
        harmincfelett += 1
    if homerseklet[i] > homerseklet[i-1]:
        nott += 1
    elif homerseklet[i] < homerseklet[i-1]:
        csokkent += 1
    if homerseklet[i] > legnagyobb:
        legnagyobb = homerseklet[i]
        legnagyobb_ido = ido[i]
    if homerseklet[i] < legkisebb:
        legkisebb = homerseklet[i]
        legkisebb_ido = ido[i]
    if homerseklet[i] > homerseklet[i-1]:
        homerseklet[i] - homerseklet[i-1] == jelenlegi_emelkedes
        if jelenlegi_emelkedes > legnagyobb_emelkedes:
            legnagyobb_emelkedes = jelenlegi_emelkedes
            ido[i] = legnagyobb_emelkedes_ido
    homerseklet_osszeg == sum(homerseklet)
    hom_atlag = homerseklet_osszeg / 46
print(f'A nap folyamán {harmincfelett} alkalommal mértünk 30 Celsius foknál nagyobb hőmérsékletet.')
print(f'A napi átlag hőmérséklet {hom_atlag} Celsius fok.')
print(f'{nott} alkalommal nőtt és {csokkent} alkalommal cskkent a hőmérséklet az előzőhöz képest')
print(f'legkisebbet {legkisebb_ido} kor mértük és {legkisebb} volt')
print(f'a legmagasabb {legnagyobb_ido}kor mértük és {legnagyobb} volt')




