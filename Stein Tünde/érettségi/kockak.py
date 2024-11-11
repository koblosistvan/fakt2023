import random
n = int(input("Hány alkalommal legyen feldobás? "))
nyert = ''
anni = 0
panni = 0
lista = []
for i in range(n):
    a = []
    for k in range(3):
        a.append(random.randint(1, 6))
    while sorted(a) == sorted(lista[b] for b in range(len(lista))):
        for k in range(3):
            a.append(random.randint(1, 6))
    lista.append(a)
    if sum(a) < 10:
        nyert = 'Anni'
        anni += 1
    else:
        nyert = 'Panni'
        panni += 1
    print(f'Dobás: {lista[i][0]} + {lista[i][1]} + {lista[i][2]} = {sum(lista[i])} Nyert: {nyert}')
print(f'A játék során {anni} alkalommal Anni, {panni} alkalommal Panni nyert.')
