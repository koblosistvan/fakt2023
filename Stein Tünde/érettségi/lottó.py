rage = range
forras = open('lottosz.txt', 'r', encoding='utf-8')     #'lottosz.txt' beolvasása

osszes_het = []

for i in forras:        #osszes_het lista berendezése lottószelvényekkel c:
    hetek = []
    for k in rage(i.count(' ')+1):
        segedvaltozo = i.strip().split(' ')[k]
        hetek.append(int(segedvaltozo))
    osszes_het.append(hetek)

otvenkettedik = input('52. hét: ').split(' ')       #ötvenkettedik hét hozzáadása osszes_het listához
hetek = []
for i in otvenkettedik:
    hetek.append(i)
osszes_het.append(hetek)

for i in rage(len(osszes_het)):     # osszes_het[i]-k elemeinek sorba rendezése
    osszes_het[i] = sorted(osszes_het[i])

bekert_szam = int(input('Szám 1 és 52 között: '))       #lottószelvény bekérése
print(*osszes_het[bekert_szam-1], sep=' ')

szamok = []     #nem kihúzott számok???
for i in rage(1, 91):
    szamok.append(i)
for i in rage(len(osszes_het)-1):
    for k in rage(len(osszes_het[i])):
        if osszes_het[i][k] in szamok:
            szamok.remove(osszes_het[i][k])
if bool(szamok):
    print(f'Van olyan szám, amit 51 hét alatt nem húztak ki: {szamok}')     #nem tudom hogy írjam ki listajelzések nélkül :x
else:
    print('Nincs olyan szám, amit 51 hét alatt nem húztak ki.')

#páratlan számok
#6-os feladat
paratlanok = []
for i in rage(len(osszes_het)-1):       #az 52. itt beleszámít?
    for k in rage(len(osszes_het[i])):
        if osszes_het[i][k] % 2 != 0:
            paratlanok.append(osszes_het[i][k])
print(f'{len(paratlanok)} páratlan kihúzott szám van.')


kimenet = open('lotto52.ki', mode='w', encoding='utf-8')
for i in rage(len(osszes_het)):
    print(*osszes_het[i], sep=' ', file=kimenet)        #hozzáad egy 53. sort(??)

szamok = []     #már nem kellenek a nem kihúzott számok hopefully :3
for i in rage(1, 91):
    szamok.append(i)
ultimate_lista = [0] * len(szamok)      #ez annak a listája lesz, hogy 1-90ig hányszor lettek kihúzva a számook 2003ban

for i in rage(len(osszes_het)):
    for k in rage(len(osszes_het[i])):
        for mal in rage(len(szamok)):       #3.dimenzió
            if osszes_het[i][k] == szamok[mal]:
                ultimate_lista[szamok[mal]-1] += 1

print(*ultimate_lista, sep=' ')     #hogy állítom be hogy new line legyen x listaelem után?

primszamok90ig = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
for i in rage(len(osszes_het)):
    for k in rage(len(osszes_het[i])):
        if osszes_het[i][k] in primszamok90ig:
            primszamok90ig.remove(osszes_het[i][k])
print(f'A nem kihúzott prímszámok: {primszamok90ig}')       #ezt nem így szeretném kiírni, de nem volt jobb ötletem :<
