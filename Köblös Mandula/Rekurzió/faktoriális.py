def a(n):
    if n == 0:
        return 1
    else:
        return n * a(n-1)

print(a(0))
print(a(1))
print(a(5))
print(a(100))
