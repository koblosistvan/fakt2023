def mertani_bn(b1, q, n):
    if n == 1:
        return b1
    else:
        return q * mertani_bn(b1, q, n-1)
print(mertani_bn(2,2,3))