forrás = open('Kerubina.txt', mode='r', encoding='utf-8')

kerubina = []

for sor in forrás:
    adat = sor.strip()
    kerubina.append(adat)

forrás.close()

forrás2 = open('Triton.txt', mode='r', encoding='utf-8')

triton = []

for sor in forrás2:
    adat2 = sor.strip()
    triton.append(adat2)

forrás2.close()

sorszam = 0
metszet = []

for i in range(len(kerubina)-1):
    j= 0
    while j < len(triton) and kerubina[i] != triton[j]:
        j += 1
    if j < len(triton):
        metszet.append(kerubina[i])

print(metszet)