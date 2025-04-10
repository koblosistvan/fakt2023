def szamjegyossz(x):
    if x < 10:
        return x
    else:
        return ( x % 10 + szamjegyossz(x // 10) )
                
print(szamjegyossz(12))