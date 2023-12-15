bemenet = int(input("Add meg a 'K' Számot: "))

lista = []
i = 0

lista.append(bemenet)

while lista[-1] != 1:
    if lista[i] % 2 == 0:        #páros
        lista.append(int(lista[i] / 2))
    else:                         #páratlan
        lista.append(int(lista[i] * 3 + 1))
    i += 1

print(*lista, sep="; ")

print("Igen, van nagyobb" if max(lista) > bemenet else "Nincs nagyobb")

#for i in range(1, 1000001):














