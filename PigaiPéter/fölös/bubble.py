import random
lista = []
i = 0
while i != 10:
    lista.append(random.randint(1, 99))
    i +=1
print(lista)
for i in range(len(lista)-1):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)
