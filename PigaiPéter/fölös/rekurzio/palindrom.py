def palindrom(n):
    n = str(n)
    if len(n) == 0:
        return True
    elif len(n) == 1:
        return True
    elif len(n) > 1:
        if n[0] == n[-1] and palindrom(n[1:-1]):
            return True
        else:
            return False