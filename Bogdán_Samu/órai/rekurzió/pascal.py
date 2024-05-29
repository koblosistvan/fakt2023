def pascal(x, y):
    if y == 0 or x == y:
        return 1
    elif x == 0 and y > 0:
        return 0
    else:
        return pascal(x-1, y-1) + pascal(x-1, y)
print(pascal(int(input('> ')), int(input('> '))))
