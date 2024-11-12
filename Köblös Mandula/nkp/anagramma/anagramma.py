forrás = open('szavak1.txt', mode='r', encoding='utf-8')

szavak1 = []

for sor in forrás:
    adat = sor.strip()
    szavak1.append(adat)

forrás.close()

forrás2 = open('szavak2.txt', mode='r', encoding='utf-8')

szavak2 = []

for sor in forrás2:
    adat = sor.strip()
    szavak2.append(adat)

forrás2.close()


for i in range(len(szavak1)):
    for j in range(len(szavak2)):
        if sorted(szavak1[i]) == sorted(szavak2[j]) and szavak2[j] != szavak1[i]:
            print(f'{szavak1[i]} - {szavak2[j]}')

for szo1 in szavak1:
    for szo2 in szavak2:
        if sorted(szo1) == sorted(szo2) and szo1 != szo2:
            print(f'{szo1} - {szo2}')