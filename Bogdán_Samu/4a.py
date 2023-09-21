import random
egy_hat = (1, 2, 3, 4, 5, 6)
lista = []
hat = 0
paros = 0
paratlan = 0
primek = (2, 3, 5)
prim = 0
for i in range(100):
    szam = random.choice(egy_hat)
    lista.append(szam)
    if szam == 6:
        hat += 1
    if (szam % 2) == 0:
        paros += 1
    else:
        paratlan = paratlan + 1
    if lista[i] in primek:
        prim += 1
print(hat)
print(paros)
print(paratlan)
print(prim)