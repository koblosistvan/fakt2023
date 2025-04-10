def h(a,k):
    if k==1:
        return a
    if k%2:
        return a*h(a,k-1)
    else:
        return h(a*a,k//2)

print(h(2,16))