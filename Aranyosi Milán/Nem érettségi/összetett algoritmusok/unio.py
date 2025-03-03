k = open('Kerubina.txt', mode='r', encoding='utf-8')
t = open('Triton.txt', mode='r', encoding='utf-8')

kerubina = []
triton = []

for sor in k:
    adat = sor.strip()
    kerubina.append(adat)

for sor in t:
    adat = sor.strip()
    triton.append(adat)

unio = kerubina

sorszam = len(kerubina)

print(triton)
print(kerubina)

for i in range(len(triton)-1):
    j = 0
    while j < len(kerubina) and kerubina[j] != triton[i]:
        j += 1
    if j == len(kerubina):
        sorszam += 1
        unio[sorszam] = triton[i]
print(unio)


