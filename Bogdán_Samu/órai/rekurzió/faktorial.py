def fakt(n):
    if n == 0:
        print('---')
        x = False
    elif n == 1:
        return 1
    else:
        return fakt(n-1) * n
print(fakt(int(input('> '))))
