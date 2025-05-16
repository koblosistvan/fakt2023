KI = 0
BE = 1
forras = open('autok.txt', mode='r', encoding='utf-8')

nap = []
ido = []
rendszam = []
azonosito = []
kilometer = []
ki_be_hajtas = []

for sor in forras:
    adat = sor.strip().split(' ')
    nap.append(int(adat[0]))
    ido.append(adat[1])
    rendszam.append(adat[2])
    azonosito.append(int(adat[3]))
    kilometer.append(int(adat[4]))
    ki_be_hajtas.append(int(adat[5]))

forras.close()

print('2. feladat')
szam = rendszam[0]
for i in range(len(nap)):
    if ki_be_hajtas[i] == KI:
        szam = rendszam[i]

for i in range(len(nap)-1,-1, -1):
    if ki_be_hajtas[i] == KI:
        print(rendszam[i])
        break

print(f'30. nap rendszám: {szam}')

print('3. feladat')
be_nap = int(input('Nap: '))
print(f'Forgalom a {be_nap}. napon:')
for i in range(len(nap)):
    if nap[i] == be_nap:
        if ki_be_hajtas[i] == KI:
            print(f'{ido[i]} {rendszam[i]} {kilometer[i]} ki')
        elif ki_be_hajtas[i] == BE:
            print(f'{ido[i]} {rendszam[i]} {kilometer[i]} be')

print('4. feladat')
parkolo = []
for i in range(len(nap)):
    if ki_be_hajtas[i] == KI:
        parkolo.append(rendszam[i])
    elif rendszam[i] in parkolo and ki_be_hajtas[i] == BE:
        parkolo.remove(rendszam[i])
print(f'A hónap végén {len(parkolo)} autót nem hoztak vissza.')

print('5. feladat')
autok = list(set(rendszam))


for rsz in sorted(autok):
    t = [kilometer[i] for i in range(len(nap)) if rendszam[i] == rsz]

    print(f'{rsz} {max(t)-min(t)} km')

def tavolsag(sor):
    ind_km = kilometer[sor]
    rsz = rendszam[sor]
    while sor < len(nap) and (rendszam[sor] != rsz or ki_be_hajtas[sor] != BE):
        sor += 1
    if sor < len(nap):
        return kilometer[sor] - ind_km
    else:
        return 0

maximum = tavolsag(0)
szemely = azonosito[0]
for i in range(len(nap)):
    if tavolsag(i) > maximum:
        maximum = tavolsag(i)
        szemely = azonosito[i]
print(f'Leghosszabb út: {maximum} km, személy: {szemely}')

rsz = input('Rendszám: ')

kiiras = open(f'{rsz}_menetlevel.txt', mode='w', encoding='utf-8')

for i in range(len(nap)):
    if rendszam[i] == rsz and ki_be_hajtas[i] == KI:
        print(f'{azonosito[i]}\t{nap[i]}.\t{ido[i]}\t{kilometer[i]} km', end='\t', file=kiiras)
    elif rendszam[i] == rsz and ki_be_hajtas[i] == BE:
        print(f'{nap[i]}.\t{ido[i]}\t{kilometer[i]} km', end='\n', file=kiiras)

kiiras.close()