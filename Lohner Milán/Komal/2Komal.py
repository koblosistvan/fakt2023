import math

def nlegnagyobb():
    n = 2
    while math.gcd(n, n + 1) != 1:
        n += 1
    return n

n = nlegnagyobb()
print(f"A legnagyobb n érték, ahol n és n+1 relatív prímek: {n}")
