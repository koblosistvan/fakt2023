def binomial(n,k):
    if k in (n, 0):
        return 1
    else:
        return binomial(n-1, k) + binomial(n-1, k-1)

print(binomial(100,10))