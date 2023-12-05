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
for i in rage(len(osszes_het)):
    for k in rage(len(osszes_het[i])):
        if osszes_het[i][k] in szamok:
            szamok.remove(osszes_het[i][k])

print(szamok)