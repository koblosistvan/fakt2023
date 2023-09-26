import random

dobások = []
for _ in range(100):
    dobások.append(random.randint(1, 6))

print(dobások)

hatosok = 0
páros = 0
prím = 0
for i in range(len(dobások)):
    if dobások[i] == 6:
        hatosok += 1
    if dobások[i] % 2 == 0:
        páros += 1
    if dobások[i] in (2, 3, 5):
        prím += 1

print(f'{hatosok} darab hatost dobtam.')
print(f'{páros} darab páros és {len(dobások) - páros} darab páratlan dobás volt.')
print(f'{prím} dobás volt prímszám.')

egy_ketto = 0
for i in range(len(dobások) - 1):
    if dobások[i] == 1 and dobások[i+1] == 2:
        egy_ketto += 1
print(f'{egy_ketto} esetben jött 2-es az 1-es után.')

növekvő = 0
for i in range(len(dobások) - 2):
    if dobások[i] < dobások[i+1] < dobások[i+2]:
        növekvő += 1
print(f'{növekvő} növekvő hármas sorozat volt.')

számláló = [0, 0, 0, 0, 0, 0]
for i in range(len(dobások)):
    számláló[dobások[i] - 1] += 1

    if dobások[i] == 1:
        számláló[0] += 1
    elif dobások[i] == 2:
        számláló[1] += 1
    elif dobások[i] == 3:
        számláló[2] += 1
    elif dobások[i] == 4:
        számláló[3] += 1
    elif dobások[i] == 5:
        számláló[4] += 1
    elif dobások[i] == 6:
        számláló[5] += 1

print(f'{számláló} volt a dobások száma.')

