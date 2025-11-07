def man(n, a1, q):
    if n==1:
        return a1
    else:
        return q*man(n-1,a1,q)

print(man(4,2,2))