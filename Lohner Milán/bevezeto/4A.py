import random

dobások = []

for i in range(100):
    dobások.append(random.randint(1,6))

print(dobások)

hatosok = 0

paros=0
paratlan=0

for i in range(len(dobások)):
    if dobások[i] == 6:
        hatosok += 1    #muvelet
print(f'{hatosok}' 'db hatost találtam')

for i in range(len(dobások)):
    if dobások[i] %2 == 0:
        paros += 1

print(paros)


egyketto=0

for i in range(len(dobások)):
    if dobások[i-1] == 1 and dobások[i] ==2:
        egyketto += 1

print(egyketto)

nagyobb=0





szamlalo = [0,0,0,0,0,0]


for i in range(len(dobások)):
    szamlalo[dobások[i] -1] +=1

print(szamlalo)




