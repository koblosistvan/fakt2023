def fakt(n):
    if n == 0:
        return 1
    else:
        return n * fakt(n-1)

print(fakt(0))
print(fakt(1))
print(fakt(5))
print(fakt(100))