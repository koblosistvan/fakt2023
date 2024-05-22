def palindrome(x):
    if len(x) < 2:
        return '> Palindróma'
    else:
        while len(x) > 1:
            if x[0] == x[-1]:
                x.pop(0)
                x.pop(-1)
            else:
                return '> Nem palindróma'
                break
        else:
            return '> Palindróma'
print(palindrome(list(input('> '))))
