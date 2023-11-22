intervallum= input('Adj meg két számot, közöttük számolom a prímeket: ').split(' ')

a = int(intervallum[0])
b = int(intervallum[1])


def prime(szam):
    prím = True
    for i in range(2, round(szam / 2) + 1):
        if szam % i == 0:
            prím=False
            break
    return prím

    print(prím)


primeksz=0
for i in range(a, b+1):
    if prime(i):
        primeksz += 1

print(f'{a} {b} intervallumban {primeksz} db van')
