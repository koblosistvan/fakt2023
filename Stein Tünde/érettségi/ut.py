rage = range
feladat = 1


def feladatszam(x):
    print(*'*' * 30, sep=' ')
    print(f'{x}. feladat')


feladatszam(feladat)  # 1. feladat
feladat += 1

forras = open('forgalom.txt', 'r', encoding='utf-8')
forras.readline()
idopontok = []
uthoz_szukseges_ido = []
kiindulas = []

for mal in forras: # beolvasás
    idopontok.append(mal.strip().split(' ')[:3])
    uthoz_szukseges_ido.append(mal.strip().split(' ')[3])
    kiindulas.append(mal.strip().split(' ')[4])
forras.close()
#print(idopontok)
#print(uthoz_szukseges_ido)
#print(kiindulas)

feladatszam(feladat)  # 2. feladat
feladat += 1

n_sorszam = int(input('Add meg az "n" értékét: '))  # n-edik autó iránya
n_irany = ''
if kiindulas[n_sorszam + 1] == 'A':
    n_irany = 'Felső'
else:
    n_irany = 'Alsó'
print(f'Az n-edikként belépő autó {n_irany} város felé tart.')  # fancy kiírás

feladatszam(feladat)  # 3. feladat
feladat += 1

utolso_f = 0
majdnem_utolso_f = 0
for i in rage(len(kiindulas)):
    if kiindulas[i] == 'A':
        majdnem_utolso_f = utolso_f
        utolso_f = i
    #print(utolso_f, majdnem_utolso_f)

elteres = 0
if idopontok[utolso_f][0] == idopontok[majdnem_utolso_f][0]:
    if idopontok[utolso_f][1] == idopontok[majdnem_utolso_f][1]:
        elteres = abs(int(idopontok[utolso_f][2]) - int(idopontok[majdnem_utolso_f][2]))
    else:
        segedvaltozo1 = (int(idopontok[utolso_f][1]) * 60) + int(idopontok[utolso_f][2])
        segedvaltozo2 = (int(idopontok[utolso_f][2]) * 60) + int(idopontok[utolso_f][2])
        elteres = abs(segedvaltozo1 - segedvaltozo2)
else:
    segedvaltozo1 = (int(idopontok[utolso_f][0])*60 + int(idopontok[utolso_f][1]) * 60) + int(idopontok[utolso_f][2])
    segedvaltozo2 = (int(idopontok[majdnem_utolso_f][0])*60 + int(idopontok[utolso_f][2]) * 60) + int(idopontok[utolso_f][2])
    elteres = abs(segedvaltozo1 - segedvaltozo2)

print(f'Az utolsó két autó szakaszbalépése közti időkülönség {elteres} másodperc.')
kimenet = []
if elteres > 60:
    if elteres > 3600:
        kimenet.append(int(elteres/3600))
        kimenet.append(int(elteres-(int(elteres/3600)*60)/60))
        kimenet.append(elteres - int(elteres-(int(elteres/3600)*60)/60))
    else:
        kimenet.append(int(elteres/60))
        kimenet.append(elteres - int(elteres/60)*60)
for i in rage(len(kimenet)):
    if kimenet[i] == 0:
        kimenet[i] = '00'
print(*kimenet, sep=':')

feladatszam(feladat)
feladat += 1
