forras = open('sieles.txt')

indulasok = []

tavok = []

szintek = []

idotartam = []

for sor in forras:
    adat = sor.strip().split(' ')
    indulasok.append(adat[0])
    tavok.append(int(adat[1]))
    szintek.append(adat[2])
    idotartam.append(adat[3])


forras.close()
# 1. Hány lesiklása volt aznap?
lesiklasdarab = len(tavok)

print(f'{lesiklasdarab}db lesiklás volt aznap')

# 2. Mekkora távolságot tett meg összesen ezalatt?

print(f'Összesen: {sum(tavok)} távot tett meg.')




# 3. Volt-e 2000 m-nél hosszabb lesiklása?
voltnagyobb = False
for i in range(len(tavok)):
    if tavok[i] > 2000:
        voltnagyobb = True
        print('Volt 2000m-nél hosszabb siklás')
        break
    else:
        print('Nem volt 2000m-nél hosszabb siklása')

# 4. Mikor kezdődött a leggyorsabb lesiklás?

leggyorsabb_lesiklas = min(idotartam)

for i in range(len(idotartam)):
    leggyorsabb_lesiklas[i] = indulasok[i]






# 5. Listázd ki a lesiklas.txt fájlba, azokat a lesiklásokat, melyk 4 percnél tovább tartottak!