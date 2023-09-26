import random
dobasok = int(input("Dobások száma: "))
egy_hat = (1, 2, 3, 4, 5, 6)
lista = []
hat = 0
paros = 0
paratlan = 0
primek = (2, 3, 5)
prim = 0
egyketto = 0
novekvo = 0
szamok = [0, 0, 0, 0, 0, 0]
for i in range(dobasok):
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
for i in range(dobasok - 1):
    if lista[i] == 1 and lista[i + 1] == 2:
        egyketto += 1
for i in range(dobasok - 2):
    if lista[i] < lista[i + 1] < lista[i + 2]:
        novekvo += 1
for i in range(dobasok):
    szamok[lista[i] - 1] += 1
print(f"Dobások: {lista}")
print(f"Hatos: {hat}")
print(f"Páros: {paros}")
print(f"Páratlan: {paratlan}")
print(f"Prím: {prim}")
print(f"1-es után 2-es: {egyketto}")
print(f"3 növekvő egymás után: {novekvo}")
print(f"Számok 1-től 6-ig: {szamok}")
