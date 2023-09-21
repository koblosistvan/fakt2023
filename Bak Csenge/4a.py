import random

dobások = []

for _ in range(100):
    dobások.append(random.randint(1, 6))

print(dobások)

hatos = 0

for i in range(len(dobások)):
    if dobások[i] == 6:
        hatos += 1

print(hatos, end = "\n\n")

páros = 0
páratlan = 0

for i in range(len(dobások)):
    if (dobások[i] % 2) == 0:
        páros += 1
    else:
        páratlan += 1

print(páros)
print(páratlan, end="\n\n")

prím = 0

for i in range(len(dobások)):
    if dobások[i] == 2 or dobások[i] == 3 or dobások[i] == 5:
        prím += 1

print(prím)

egymás_után = 0
egymás_után_3 = 0

for i in range(1, len(dobások)-1):
    if dobások[i-1] == 1 and dobások[i] == 2:
        egymás_után += 1
    if dobások[i-1] < dobások[i] < dobások[i+1]:
        egymás_után_3 += 1

print(egymás_után)
print(egymás_után_3)

számláló = [0, 0, 0, 0, 0, 0]

for i in range(len(dobások)):
    számláló[dobások[i] - 1] += 1

print(számláló)






