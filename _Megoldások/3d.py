# Írjuk ki a Fibonacci számokat 1000-ig! Ha nem tudod, mik a Fibonacci számok, nézz utána!

# első megoldás (átláthatóbb)
a = 1
b = 1
print(a)
print(b)
c = a + b
while c < 1000:
    print(c)
    a = b
    b = c
    c = a + b


# második megoldás (pythonosabb)
a = 1
b = 1
print(a)
while b < 1000:
    print(b)
    a, b = b, a+b
