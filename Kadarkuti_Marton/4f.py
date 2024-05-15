interval = input("Adj meg két a számot intervallumnak, <szóközzel> elválasztva: ")
l = interval.split(" ")
a, b = int(l[0]), int(l[1])
print(a)
print(b)
prímszámláló = 0
prímlista = []

def prímteszt(szám):
    prím = True
    for i in range(2, round(szám/2) +1):
        if szám % i == 0:
            prím = False
            break
    return prím

for i in range(a, b+1):
    if prímteszt(i):
        prímszámláló += 1
        prímlista.append(i)

if 1 in prímlista:
    prímlista.remove(1)
    prímszámláló -= 1
print(f'Az adott intervallumban [{a}; {b}] {prímszámláló} prímszám van.')