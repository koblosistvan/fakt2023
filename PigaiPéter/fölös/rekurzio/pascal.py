def pascal(n, k):
    if k == 0 or k == n:
        return 1
    elif n == 0 and k > 0:
        return 0
    else:
        return pascal(n-1, k-1) + pascal(n - 1, k)

print(pascal(30, 3))