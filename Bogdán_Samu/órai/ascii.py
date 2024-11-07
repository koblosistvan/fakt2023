a = list(input('> '))
for i in range(len(a)):
    a[i] = chr(ord(a[i])+3)
print(f"> {''.join(a)}")