import random

hatosok = 0
dobások = []
for i in range(100):
    dobások.append(random.randint(1, 6))

print(dobások)

for i in range(len(dobások)):
    if dobások[i] == 6:
        hatosok += 1
print(hatosok)
páros = 0
páratlan = 0

for i in range(len(dobások)):
    if dobások[i] % 2 == 0:
        páros += 1
    else:
        páratlan += 1
print(páros)
print(páratlan)
prím = 0

for i in range(len(dobások)):
    if dobások[i] == 2 or dobások[i] == 3 or dobások[i] == 5:
        prím += 1
print(prím)
egykettő = 0
for i in range(len(dobások) - 1):
    if dobások[i] == 1 and dobások[i + 1] == 2:
        egykettő += 1
print(egykettő)
nagyobb = 0
for i in range(len(dobások) - 2):
    if dobások[i] < dobások[i + 1] < dobások[i + 2]:
        nagyobb += 1
print(nagyobb)
számok = [0, 0, 0, 0, 0, 0, ]
for i in range(len(dobások)):
    számok[dobások[i] - 1] += 1
print(számok)
