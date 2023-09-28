intervallum = input("2 szám: ").split(" ")
a = int(intervallum[0])
b = int(intervallum[1])
prímek_száma = 0

def príme(szám):
    prím = True
    for i in range(2, round(szám/2)+1):
        if szám % i == 0:
            prím = False
            break
    return prím

for i in range(a, b+1):
    if príme(i):
        prímek_száma += 1

print(prímek_száma)

#saját
szám = 103

prím = False
for i in range(2, szám):
    if szám % i != 0:
        prím = True
    if prím and szám == i:
        print(f"{szám[i]} egy prím szám")
        break
    prím = False















