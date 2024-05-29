def szr(x, y):
    if x < y:
        print(x, end=' ')
    else:
        szr(x//y, x)
        print(x % y, end=' ')