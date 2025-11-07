def mosszeg(n, a1, q):
    if n==1:
        return a1
    else:
        return a1*(q**(n-1)) + mosszeg(n-1, a1, q)

print(mosszeg(4,2,2))