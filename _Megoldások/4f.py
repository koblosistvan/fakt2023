intervallum = input('Adj meg két számot, közöttük számolom a prímeket: ').split(' ')
a = int(intervallum[0])
b = int(intervallum[1])
def príme(szám):
    # algotritmus, ami eldönti, hogy prím-e
    prím = True
    for i in range(2, round(szám/2) + 1):
        if szám % i == 0:
            prím = False
            break
    return prím

prímek_száma = 0
for i in range(a, b+1):
    if príme(i):
        prímek_száma += 1
print(f'A [{a}, {b}] intervallumban {prímek_száma} prímszám van.')