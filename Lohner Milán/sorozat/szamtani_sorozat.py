def a(n):
    return 3+2*n


print(a(3))
print(a(10))


def b(n):
    if n == 1:
        return 5
    else:
        return b(n-1)+2
print(b(1))
print(b(10))