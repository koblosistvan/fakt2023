forras = open("sielés.txt", mode='r', encoding='utf-8')
forras.readline()
indulas = []
tav = []
szint = []
idotartam = []
for sor in forras:
    indulas.append(sor.strip().split(' ')[0])
    segedvaltozo = sor.strip().split(' ')[1]
    tav.append(int(segedvaltozo))
    segedvaltozo = sor.strip().split(' ')[2]
    szint.append(int(segedvaltozo))
    segedvaltozo = sor.strip().split(' ')[3]
    idotartam.append(int(segedvaltozo))
forras.close()

# 1. Hány lesiklása volt aznap?
print(f'1. feladat:\n{len(indulas)} lesiklása volt aznap.\n')
# 2. Mekkora távolságot tett meg összesen ezalatt?
ossztav = 0
for i in tav:
    ossztav += i
print(f'2. feladat:\n{ossztav} távolságot tett meg összesen.\n')
# 3. Volt-e 2000 m-nél hosszabb lesiklása?
volte = "Nem volt"
for i in tav:
    if i > 2000:
        volte = "Volt"
print(f'3. feladat:\n{volte} 2000 méternél hosszabb lesiklása.\n')
# 4. Mikor kezdődött a leggyorsabb lesiklás?
leggyorsabb = 0
for i in range(len(tav)):
    if tav[i]/idotartam[i] > leggyorsabb:
        leggyorsabb = tav[i]/idotartam[i]
        index4 = i
print(f'4. feladat:\nA leggyorsabb lesiklás {indulas[index4]} időpontban kezdődött.')
# 5. Listázd ki a lesiklas.txt fájlba, azokat a lesiklásokat, melyk 4 percnél tovább tartottak!
kimenet = open("lesiklas.txt", mode='w', encoding='utf-8')
for i in range(len(idotartam)):
    if idotartam[i]/60 > 4:
        print(f'Indulás: {indulas[i]}\tidőtartam: {idotartam[i]}', file=kimenet)
kimenet.close()
