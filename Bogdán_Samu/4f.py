intervallum = input('Intervallum: ')
xy = intervallum.split(':')
x = int(xy[0])
y = int(xy[1])
a = True
szam = 0
def prim(szam):
    for i in range(y - x):
        szam = x
        szam += 1
    for i in range(2, szam):
        if (szam % i == 0) or (szam / i <= 2):
            a = False
            break
    return a
primek = 0
if a and (x <= szam <= y):
    primek += 1
print(f'{primek} darab prímszám van a megadott intervallumban.')