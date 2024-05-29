def palindrom(s):
    s = str(s)
    if len(s) < 2:
        return True
    elif s[0] == s[-1] and palindrom(s[1:-1]):
        return True
    else:
        return False

print(palindrom('annapanna'))