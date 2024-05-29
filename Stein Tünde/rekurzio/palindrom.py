def palindrom(n):
    n = (str(n))
    ans = True
    for i in range(len(n)):
        if n[i] == n[-1-i]:
            ans = True
        else:
            ans = False
    return ans


def rekurz_palindrom(n):
    n = str(n)
    ans = True
    if n[0] == n[-1] and rekurz_palindrom(n[1:-1]):
        ans = True
    else:
        ans = False
    return ans


print(input('>'))
