def keplet(n,k):
    if k == 0:
        return 1
    elif n == k:
        return 1
    elif n == 0:
        return 0
    else:
        return keplet(n-1,k-1)+n-1,k



print(keplet(90, 5))