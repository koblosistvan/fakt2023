def polindrom(s):
    s=str(s)
    if len(s)<2:
        return True
    elif s[0] == s[-1] and polindrom(s[1:-1]):
        return True
    else:
        return False

print(polindrom('anna'))
print(polindrom('indulagorogaludni'))
