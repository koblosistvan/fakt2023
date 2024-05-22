def binominalis(n, k):
    if k == 0:
        return 1
    elif k == n:
        return 1
    elif n == 0:
        return 0
    else:
        return binominalis(n-1, k-1) + binominalis(n-1, k)

print(binominalis(90, 5))
print(binominalis(31, 3))