def szosszeg(n,a1,d):
    if n==1:
        return a1
    else:
        return a1 + (n-1)*d + szosszeg(n-1,a1,d)

print(szosszeg(5,1,1))