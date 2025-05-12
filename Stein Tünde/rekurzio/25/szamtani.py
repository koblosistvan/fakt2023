def an(a1, d, n):
    if n == 1:
        return a1
    else:
        return an(a1, d, n-1) + d
print(an(1,1,3))