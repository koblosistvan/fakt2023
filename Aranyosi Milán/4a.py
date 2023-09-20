import random

dobasok = []

for _ in range(100):
    dobasok.append(random.randint(1, 6))

print(dobasok)

hatos_dobasok = 0

for i in range(len(dobasok)):
    if dobasok[i] == 6:
        hatos_dobasok += 1

print(dobasok.count(6))

print(hatos_dobasok)

paros = 0
paratlan = 0

for i in range(len(dobasok)):
    if dobasok[i] % 2 == 0:
        paros += 1
    else:
        paratlan += 1
print(paros, paratlan)

prim = 0
for i in range(len(dobasok)):
    if dobasok[i] in (2, 3, 5):
        prim += 1
print(prim)

egy_ketto = 0

for i in range(len(dobasok) - 1):
    if dobasok[i] == 1 and dobasok[i + 1] == 2:
        egy_ketto += 1
print(egy_ketto)

egy_kettoa = 0
for i in range(1, len(dobasok)):
    if dobasok[i] == 1 and dobasok[i + 1] == 2:
        egy_kettoa += 1
print(egy_kettoa)

egyrenagyobb = 0
for i in range(len(dobasok) - 2):
    if dobasok[i] < dobasok[i + 1] < dobasok[i + 2]:
        egyrenagyobb += 1
print(egyrenagyobb)

szamlalo = [0, 0, 0, 0, 0, 0]
for i in range(len(dobasok)):
    szamlalo[dobasok[i] - 1] += 1
print(szamlalo)
