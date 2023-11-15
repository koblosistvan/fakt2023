import random

dobások = []
for _ in range(100):
    dobások.append(random.randint(1, 6))

print(dobások)
hatosok = 0
páros_dobások = 0
páratlan_dobások = 0
prímek = 0
egy_kettő = 0
növekvő = 0
számláló = [0, 0, 0, 0, 0, 0]
for i in range(len(dobások)):
    if dobások[i] == 6:
        hatosok += 1
print(f'A hatosok száma: {hatosok}')
for i in range(len(dobások)):
    if dobások[i] % 2 == 0:
        páros_dobások += 1
    else:
        páratlan_dobások += 1
print(f'A páros dobások száma: {páros_dobások}\nA páratlan dobások száma: {páratlan_dobások}')
for i in range(len(dobások)):
    if dobások[i] in (2, 3, 5):
        prímek += 1
print(f'A prímek száma {prímek}')
for i in range(len(dobások) - 1):
    if dobások[i] == 1 and dobások[i + 1] == 2:
        egy_kettő += 1
print(f'{egy_kettő} esetben jött 2-es az 1-es után')
for i in range(len(dobások) - 2):
    if dobások[i] < dobások[i + 1] < dobások[i +2]:
        növekvő += 1
print(f'{növekvő} növekvő hármas sorozat volt')
for i in range (len(dobások)):
    számláló[dobások[i - 1]]