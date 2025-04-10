def h(a,k):
    if k%2:
        return a*h(a,k)-1
    else:
        return 