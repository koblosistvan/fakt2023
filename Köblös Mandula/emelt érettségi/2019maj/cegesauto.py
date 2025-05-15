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
    if ki_be_hajtas[i] == 0:
        szam = rendszam[i]

print(f'30. nap rendszám: {szam}')

print('3. feladat')
be_nap = int(input('Nap: '))
print(f'Forgalom a {be_nap}. napon:')
for i in range(len(nap)):
    if nap[i] == be_nap:
        if ki_be_hajtas[i] == 0:
            print(f'{ido[i]} {rendszam[i]} {kilometer[i]} ki')
        elif ki_be_hajtas[i] == 1:
            print(f'{ido[i]} {rendszam[i]} {kilometer[i]} be')

print('4. feladat')
parkolo = []
for i in range(len(nap)):
    if ki_be_hajtas[i] == 1:
        parkolo.append(rendszam[i])
    elif rendszam[i] in parkolo and ki_be_hajtas[i] == 0:
        parkolo.remove(rendszam[i])
print(parkolo)

print('5. feladat')
autok = []
for i in range(len(nap)):
    if rendszam[i] not in autok:
        autok.append(rendszam[i])
print(autok)

for i in range(len(autok)):
    szamlalo = 0
    for j in range(len(nap)):
        if rendszam[i] == rendszam[j]:
            szamlalo = kilometer[j]
    print(f'{rendszam[j]} {szamlalo} km')

