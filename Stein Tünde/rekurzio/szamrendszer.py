def valto(a, b):
    szam = 0
    if a < b:
        return a
    while szam > 0:
        seged = int(str(a)[-1 - i]) % b
        szam += seged * (i+1)
        a -= seged
        return szam


print(valto(210, 2))
