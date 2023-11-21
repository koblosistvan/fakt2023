a=1
b=1

print(a)
print(b)
c = a + b

while c < 1000:
    print(c)
    a = b
    b = c
    c = a + b