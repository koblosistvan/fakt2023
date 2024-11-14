import random

lista =

for i in range(lista-1):
    min = i
    for j in range(i+1, lista):
        if lista[i] < lista[min]:
            min = j

    seged = lista[i]
    lista[i] = lista[min]
    lista[min] = seged

