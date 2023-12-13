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
    dologlista = mal.strip().split(' ')[:3]
    dolog = (int(dologlista[0]) * 3600) + (int(dologlista[1]) * 60) + int(dologlista[2])
    dolog2 = mal.strip().split(' ')[3]
    idopontok.append(dolog)
    uthoz_szukseges_ido.append(int(dolog2))
    kiindulas.append(mal.strip().split(' ')[4])
forras.close()
print(idopontok)
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

#elteres = 0
#if idopontok[utolso_f][0] == idopontok[majdnem_utolso_f][0]:
    #if idopontok[utolso_f][1] == idopontok[majdnem_utolso_f][1]:
        #elteres = abs(int(idopontok[utolso_f][2]) - int(idopontok[majdnem_utolso_f][2]))
    #else:
        #segedvaltozo1 = (int(idopontok[utolso_f][1]) * 60) + int(idopontok[utolso_f][2])
        #segedvaltozo2 = (int(idopontok[majdnem_utolso_f][2]) * 60) + int(idopontok[majdnem_utolso_f][2])
        #elteres = abs(segedvaltozo1 - segedvaltozo2)
#else:
    #segedvaltozo1 = (int(idopontok[utolso_f][0])*60 + int(idopontok[utolso_f][1]) * 60) + int(idopontok[utolso_f][2])
    #segedvaltozo2 = (int(idopontok[majdnem_utolso_f][0])*60 + int(idopontok[utolso_f][2]) * 60) + int(idopontok[utolso_f][2])
#elteres = abs(segedvaltozo1 - segedvaltozo2)
elteres = abs(idopontok[utolso_f] - idopontok[majdnem_utolso_f])

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
for i in rage(int(idopontok[0]/3600)-1, int(idopontok[-1]/3600)):
    kimenet_lista_4 = [0, 0, 0]
    for k in rage(len(kiindulas)):
        #kimenet.append(idopontok[i][0])
        if int(idopontok[k]/3600) == i+1:
            kimenet_lista_4[0] = i+1
            if kiindulas[k] == 'A':
                kimenet_lista_4[1] += 1
            elif kiindulas[k] == 'F':
                kimenet_lista_4[2] += 1
    print(*kimenet_lista_4, sep=' ')

feladatszam(feladat)
feladat += 1

sorrend = sorted(uthoz_szukseges_ido)
top10 = sorrend[:10]
print(sorrend)
kiindulas_sorrend = []
belepes = []
for i in rage(len(idopontok)):
    belepes.append(int(idopontok[i]/3600))
    belepes.append(int((idopontok[i] - (int(idopontok[i]/3600)*3600)) /60))
    belepes.append(int(idopontok[i] - (int(idopontok[i])/60)*60))
print(belepes)
for i in range(min(top10), max(top10)+1):
    for k in rage(len(uthoz_szukseges_ido)):
        if uthoz_szukseges_ido[k] == i:
            kiindulas_sorrend.append(kiindulas[i])

    print(sorrend[i], kiindulas_sorrend[i])

