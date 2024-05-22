def a(n):
    return 3 + 2*n

print(a(3))
print(a(10))

def b(n):
    if n == 1:
        eredmeny = 5
        return eredmeny
    else:
        eredmeny = b(n-1) + 2
        return eredmeny

print(b(3))
print(b(10))
