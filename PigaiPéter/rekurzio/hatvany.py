def hatvany(a ,n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    elif n < 0:
        return 1/hatvany(a, -n)
    elif n % 2 == 0:
        s = hatvany(a, n//2)
        return s*s
    elif n % 2 == 1:
        return a * hatvany(a, n-1)

print(hatvany(2,9999))