forras = open('Vtabla.dat')
tabla = []

for sor in forras:
    tabla.append(sor.strip())



forras.close()

#############################

szoveg = 'Ez a próba szöveg, amit kódolunk!'
kulcs = 'auto'
#############################
ekezetes = 'ÁÉÍÓÖŐÜÚŰ'
ekezetmentes = 'AEIOOOUUU'
szoveg = szoveg.upper()

for i in range(len(ekezetes)):
    szoveg = szoveg.replace(ekezetes[i],ekezetmentes[i])

joszoveg = ''
for i in range(len(szoveg)):
    if szoveg[i] in tabla[0]:
        joszoveg += szoveg[i]

print(f'Szöveg: \t\t\t{joszoveg}')

##############################
kulcs = 'auto'
kulcs = kulcs.upper()
kulcs = kulcs * (len(szoveg) // len(kulcs)+1)
kulcs = kulcs[:len(joszoveg)]
print(f'Kulcs: \t\t\t\t{kulcs}')

kodolt = ''

for i in range(len(joszoveg)):
    oszlop = tabla[0].find(joszoveg[i])
    sor = 0
    while tabla[sor][0] != kulcs[i]:
        sor += 1
    kodkarakter = tabla[sor][oszlop]
    kodolt += kodkarakter

print(kodolt)







