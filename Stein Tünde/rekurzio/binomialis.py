def bin(n, k):
    if n == k or k == 0:
        return 1
    if n == 0:
        return 0
    else:
        return bin(n-1, k-1) + bin(n-1, k)


print(bin(31, 3))
