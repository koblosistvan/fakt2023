def binom(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return binom(n-1, k) + binom(n-1, k-1)
print(binom(5, 2))