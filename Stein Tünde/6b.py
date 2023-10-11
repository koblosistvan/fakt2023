forras = open('6b-forgalom.txt', mode='r', encoding='utf-8')

hely = []
idopont = []
forras.readline()
for sor in forras:
    adat = sor.strip().split( )
    hely.append(int(adat[0]))
    idopont.append(int(adat[1])*60 + int(adat[2]))
forras.close()

def ora_perc(x):
    idoertek = idopont[x]
    ora =idoertek // 60
    perc = idoertek % 60
    return f'{ora}:{perc}'

#1. feladat
leghosszabb_id = 0
leghosszabb_ido = idopont[1] - idopont[0]
for i in range(len(hely) - 1):
    if idopont[i+1] - idopont[i] > leghosszabb_ido:
        leghosszabb_id = i
        leghosszabb_ido = idopont[i+i] - idopont[i]

#2. feladat
_50es_meresi_pontok = 0
for i in range(len(hely)):
    if hely[i] == 50:
        _50es_meresi_pontok += 1
#3.feladat



print(f'A leghosszabb szünet {leghosszabb_ido} perc volt,{ora_perc(i)} és {ora_perc(i+1)} között.')
print(f'')
