def hatvany(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y < 1:
        return 1 / hatvany(x, -y)
    elif y % 2 == 0:
        z = hatvany(x, y//2)
        return z * z
    elif y % 2 == 1:
        return x * hatvany(x, y-1)
print(hatvany(int(input('> ')), int(input('> '))))
