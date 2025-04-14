def hatvany(a, k):
    if a == 0:
        return 0
    elif k == 1:
        return 1
    elif k % 2:
        (hatvany(a, k/2))**2