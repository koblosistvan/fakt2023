def valt(n, k):
    if n < k:
        print(n, end='')
    else :
        valt(n // k, n)
        print(n % k, end='')
