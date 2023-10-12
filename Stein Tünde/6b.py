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
    ora = idoertek // 60
    perc = idoertek % 60
    return f'{ora}:{perc}'

#1. feladat
leghosszabb_id = 0
leghosszabb_ido = idopont[1] - idopont[0]
for i in range(len(hely) - 1):
    if idopont[i+1] - idopont[i] > leghosszabb_ido:
        leghosszabb_id = i
        leghosszabb_ido = idopont[i+1] - idopont[i]
        i_ertek = i
print(f'A leghosszabb szünet {leghosszabb_ido} perc volt,{ora_perc(i_ertek)} és {ora_perc(i_ertek+1)} között.')

#3. feladat
_50es_meresi_pontok = 0
for i in range(len(hely)):
    if hely[i] == 50:
        _50es_meresi_pontok += 1
print(f'{_50es_meresi_pontok} mérés történt az 50-es mérési pontnál.')

#4.feladat
bekert_idopont = input('Adj meg egy időpontot: ')
van_idopont = False
for i in range(len(idopont)):
    if bekert_idopont == ora_perc(i):
        van_idopont = True
print(van_idopont)

#5. feladat


#6-7. feladat
allomasok_db = [0] * 100
for i in range(len(hely)):
    allomasok_db[ hely[i]-1 ] += 1



print('End.')