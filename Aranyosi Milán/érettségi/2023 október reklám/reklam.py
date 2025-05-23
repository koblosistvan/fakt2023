forras = open('rendel.txt', mode='r', encoding='utf-8')

napszam = []
varos = []
rendeles_db = []

for sor in forras:
    adat = sor.strip().split(' ')
    napszam.append(int(adat[0]))
    varos.append(adat[1])
    rendeles_db.append(int(adat[2]))

forras.close()

def osszes(varosnev, megadottnap):
    szamlaloosszes = 0
    for i in range(len(napszam)):
        if napszam[i] == int(megadottnap):
            if varos[i] == varosnev:
                szamlaloosszes += rendeles_db[i]
    return szamlaloosszes


print('2. feladat:')
print(f'A rendelések száma: {len(varos)}')

print('3. feladat:')
adott_nap = input('Kérem, adjon meg egy napot: ')
szamlalo = 0
for i in range(len(napszam)):
    if napszam[i] == adott_nap:
        szamlalo += 1
print(f'A rendelések száma az adott napon: {szamlalo}')

print('4. feladat:')
szamlalo2 = 0

reklamnelkuli_napok = []

for i in range(len(napszam)):
    if varos[i] == 'NR':
        reklamnelkuli_napok.append(napszam[i])

for j in range(1, max(napszam)+1):
    if j not in reklamnelkuli_napok:
        szamlalo2 += 1
print(f'{szamlalo2} nap nem volt a reklámban nem érintett városból rendelés')

print('5. feladat:')
legn_rendeles = max(rendeles_db)
legn_rendeles_index = napszam[0]

for i in range(len(rendeles_db)):
    if rendeles_db[i] == legn_rendeles:
        legn_rendeles_index = napszam[i]
        break

print(f'A legnagyobb darabszám: {legn_rendeles}, a rendelés napja: {legn_rendeles_index}')

print('7. feladat:')
megadottnap = 21
print(f'A rendelt termékek darabszáma a {megadottnap}. napon PL: {osszes("PL", megadottnap)} TV: {osszes("TV", megadottnap)}  NR: {osszes("NR", megadottnap)}')

print('8. feladat:')

pl = []
tv = []
nr = []

seged_pl = 0
seged_tv = 0
seged_nr = 0

seged_pl2 = 0
seged_tv2 = 0
seged_nr2 = 0

seged_pl3 = 0
seged_tv3 = 0
seged_nr3 = 0

for i in range(len(napszam)):
    if napszam[i] in range(1, 11):
        if varos[i] == "PL":
            seged_pl += 1
        elif varos[i] == "TV":
            seged_tv += 1
        else:
            seged_nr += 1
    if napszam[i] > 10:
        pl.append(seged_pl)
        tv.append(seged_tv)
        nr.append(seged_nr)
        break

for i in range(len(napszam)):
    if napszam[i] in range(11, 21):
        if varos[i] == "PL":
            seged_pl2 += 1
        elif varos[i] == "TV":
            seged_tv2 += 1
        else:
            seged_nr2 += 1
    if napszam[i] > 20:
        pl.append(seged_pl2)
        tv.append(seged_tv2)
        nr.append(seged_nr2)
        break


for i in range(len(napszam)):
    if napszam[i] in range(21, 31):
        if varos[i] == "PL":
            seged_pl3 += 1
        elif varos[i] == "TV":
            seged_tv3 += 1
        else:
            seged_nr3 += 1

pl.append(seged_pl3)
tv.append(seged_tv3)
nr.append(seged_nr3)

print('Napok\t1..10\t11..20\t21..30')
print(f'PL\t\t{pl[0]}\t\t{pl[1]}\t\t{pl[2]}')
print(f'TV\t\t{tv[0]}\t\t{tv[1]}\t\t{tv[2]}')
print(f'NR\t\t{nr[0]}\t\t{nr[1]}\t\t{nr[2]}')



kimenet = open('kampany.txt', mode='w', encoding='utf-8')

print('Napok\t1..10\t11..20\t21..30', file=kimenet)
print(f'PL\t\t{pl[0]}\t\t{pl[1]}\t\t{pl[2]}', file=kimenet)
print(f'TV\t\t{tv[0]}\t\t{tv[1]}\t\t{tv[2]}', file=kimenet)
print(f'NR\t\t{nr[0]}\t\t{nr[1]}\t\t{nr[2]}', file=kimenet)
