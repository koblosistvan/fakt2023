def hatvany(a, k):
    if k == 0:
        return 1
    elif k == 1:
        return a
    elif k < 0:
        return 1/hatvany(a, k)
    elif k > 0:
        if k % 2 == 0:
            seged = hatvany(a, k/2)
            return seged * seged
        else:
            return a * hatvany(a, k-1)
    else:
        return 'else'


print(hatvany(2, 1000000))
