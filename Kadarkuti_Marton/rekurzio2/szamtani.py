def szan(n, a1, d):
    if n == 1:
        return a1
    else:
        return d + szan(n-1, a1, d)

print(szan(4,2,3))