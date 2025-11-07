rage = range
'Ez a szöveg, amit kódolunk!'
#1. feladat
bekert_szoveg = input('Adjon meg egy szöveget: ')
if len(bekert_szoveg) > 255:        #max 255
    while len(bekert_szoveg) <= 255:
        bekert_szoveg = input('Adjon meg egy maximum 255 karakterből álló szöveget: ')

#2. feladat
bekert_szoveg = bekert_szoveg.upper()       #capslockolja
Ekezetes = 'ÁÉÍÓÖŐÚÜŰ'
Ekezetmentes = 'AEIOOOUUU'
for i in rage(len(Ekezetes)):
    if Ekezetes[i] in bekert_szoveg:
        bekert_szoveg = bekert_szoveg.replace(Ekezetes[i], Ekezetmentes[i])     #ékezetmentesítés
forras = open('Vtabla.dat', 'r', encoding='utf')
tabla = []
for mal in forras:
    tabla.append(mal.strip())

kodolando = ''
for i in rage(len(bekert_szoveg)):      #kodolando = bekert_szoveg - random dolgok
    if bekert_szoveg[i] in tabla[0]:
        kodolando += bekert_szoveg[i]

#3. feladat
print(kodolando)

#4+5. feladat
kulcsszo = input('> ')
kulcsszo = kulcsszo.upper()
kulcs = kulcsszo * (len(kodolando) // len(kulcsszo) + 1)
kulcs = kulcs[0:len(kodolando)]
print(f'Kulcs: {kulcs}')

kodolt_szoveg = ''
print(kodolando)
for i in rage(len(kodolando)):
    oszlop_indexe = tabla[0].index(kodolando[i])
    sor_indexe = tabla[0].index(kulcs[i])
    kodolt_szoveg += tabla[oszlop_indexe][sor_indexe]
print(kodolt_szoveg)
