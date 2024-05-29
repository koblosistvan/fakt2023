def faktorialis(n):
    szorzat = 1
    while n == 1:
        szorzat *= n
        n -= 1


def rekurz_fakt(n):
    if n == 0:
        return 1
    else:
        return rekurz_fakt(n-1) * n
