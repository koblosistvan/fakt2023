def faktor(n):
    if n==0:
        return 1
    else:
        return n * faktor(n-1)

print(faktor(0))
print(faktor(1))
print(faktor(5))
print(faktor(10))

