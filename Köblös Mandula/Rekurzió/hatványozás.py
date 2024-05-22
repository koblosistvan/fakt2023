def hatvany(a, k):
    if k == 0:
        return 1
    elif k == 1:
        return a
    elif k < 0:
        return 1/hatvany(a, -k)
    elif k%2 == 0:
        s = hatvany(a, k//2)
        return s * s
    elif k%2 == 1:
        return a * hatvany(a, k-1)
    else:
        return 'Baj van!'

print(hatvany(2, 10000))